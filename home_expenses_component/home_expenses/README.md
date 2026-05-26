# Home Expenses Tracker

Plugin para Home Assistant que permite registrar y gestionar los gastos del hogar.

## Instalación

1. Descarga el archivo `home_expenses.zip`
2. Descomprime el contenido en la carpeta `custom_components` de tu instalación de Home Assistant:
   ```
   config/custom_components/home_expenses/
   ```
3. Reinicia Home Assistant
4. Añade la siguiente configuración a tu `configuration.yaml`:
   ```yaml
   home_expenses:
   ```

## Servicios Disponibles

### `home_expenses.add_expense`
Añade un nuevo gasto al registro.

**Parámetros:**
- `category` (opcional): Categoría del gasto (por defecto: "General")
- `amount`: Cantidad del gasto en euros
- `description` (opcional): Descripción del gasto

**Ejemplo:**
```yaml
service: home_expenses.add_expense
data:
  category: Alimentación
  amount: 50.75
  description: Compra semanal supermercado
```

### `home_expenses.get_expenses`
Obtiene la lista de todos los gastos registrados.

**Ejemplo:**
```yaml
service: home_expenses.get_expenses
```

### `home_expenses.clear_expenses`
Limpia todos los gastos registrados.

**Ejemplo:**
```yaml
service: home_expenses.clear_expenses
```

## Sensores

El plugin crea automáticamente el sensor:
- `sensor.total_expenses`: Muestra el total acumulado de todos los gastos

## Uso desde Developer Tools

Puedes usar los servicios desde **Developer Tools > Services** en la interfaz de Home Assistant, o crear automatizaciones que registren gastos automáticamente.

## Almacenamiento

Los gastos se almacenan en un archivo JSON en:
```
config/home_expenses/expenses.json
```

Cada gasto incluye:
- Timestamp (fecha y hora)
- Categoría
- Importe
- Descripción

## Ejemplo de Automatización

```yaml
automation:
  - alias: "Registrar gasto mensual de internet"
    trigger:
      platform: time
      at: "09:00:00"
    condition:
      condition: template
      value_template: "{{ now().day == 1 }}"
    action:
      - service: home_expenses.add_expense
        data:
          category: Internet
          amount: 45.00
          description: Factura mensual de internet
```
