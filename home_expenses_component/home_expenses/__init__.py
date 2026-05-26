"""Home Expenses Tracker - Componente para registrar gastos del hogar en Home Assistant."""
import logging
import json
import os
from datetime import datetime
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "home_expenses"
DATA_FILE = "expenses.json"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Configuración inicial del componente."""
    hass.data.setdefault(DOMAIN, {})
    
    # Registrar servicio para añadir gasto
    async def add_expense_service(call):
        """Servicio para añadir un nuevo gasto."""
        category = call.data.get("category", "General")
        amount = call.data.get("amount", 0.0)
        description = call.data.get("description", "")
        
        expense = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "amount": float(amount),
            "description": description
        }
        
        expenses = await _load_expenses(hass)
        expenses.append(expense)
        await _save_expenses(hass, expenses)
        
        # Actualizar sensor de total
        total = sum(e["amount"] for e in expenses)
        hass.states.async_set(
            f"{DOMAIN}.total_expenses",
            total,
            {"unit_of_measurement": "€", "friendly_name": "Total Gastos"}
        )
        
        _LOGGER.info(f"Gasto añadido: {amount}€ en {category} - {description}")
    
    hass.services.async_register(DOMAIN, "add_expense", add_expense_service)
    
    # Registrar servicio para obtener gastos
    async def get_expenses_service(call):
        """Servicio para obtener los gastos registrados."""
        expenses = await _load_expenses(hass)
        return expenses
    
    hass.services.async_register(DOMAIN, "get_expenses", get_expenses_service)
    
    # Registrar servicio para limpiar gastos
    async def clear_expenses_service(call):
        """Servicio para limpiar todos los gastos."""
        await _save_expenses(hass, [])
        hass.states.async_set(
            f"{DOMAIN}.total_expenses",
            0,
            {"unit_of_measurement": "€", "friendly_name": "Total Gastos"}
        )
        _LOGGER.info("Gastos limpiados")
    
    hass.services.async_register(DOMAIN, "clear_expenses", clear_expenses_service)
    
    # Inicializar estado
    expenses = await _load_expenses(hass)
    total = sum(e["amount"] for e in expenses)
    hass.states.async_set(
        f"{DOMAIN}.total_expenses",
        total,
        {"unit_of_measurement": "€", "friendly_name": "Total Gastos"}
    )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configurar una entrada de configuración."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Descargar una entrada de configuración."""
    return True


def _get_data_path(hass: HomeAssistant) -> str:
    """Obtener la ruta del archivo de datos."""
    return os.path.join(hass.config.config_dir, DOMAIN, DATA_FILE)


async def _load_expenses(hass: HomeAssistant) -> list:
    """Cargar gastos desde el archivo JSON."""
    data_path = _get_data_path(hass)
    if os.path.exists(data_path):
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            _LOGGER.error(f"Error al cargar gastos: {e}")
    return []


async def _save_expenses(hass: HomeAssistant, expenses: list) -> None:
    """Guardar gastos en el archivo JSON."""
    data_path = _get_data_path(hass)
    data_dir = os.path.dirname(data_path)
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    try:
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(expenses, f, indent=2, ensure_ascii=False)
    except IOError as e:
        _LOGGER.error(f"Error al guardar gastos: {e}")
