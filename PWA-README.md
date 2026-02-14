# 📱 Creador de Videos - Progressive Web App (PWA)

## ✅ Archivos de la PWA

La aplicación ahora es una PWA completa con los siguientes archivos:

1. **creador-video.html** - Aplicación principal (actualizada con soporte PWA)
2. **manifest.json** - Configuración de la PWA
3. **service-worker.js** - Service Worker para funcionalidad offline
4. **icon-192.png** - Icono de 192x192px (NECESITAS CREARLO)
5. **icon-512.png** - Icono de 512x512px (NECESITAS CREARLO)

## 🎨 Crear los Iconos

Necesitas crear dos iconos PNG con fondo del color del tema (#667eea):

### Opción 1: Generador online
1. Ve a https://favicon.io/favicon-generator/
2. Texto: "VC" o "🎬"
3. Color de fondo: #667eea
4. Color de texto: #ffffff
5. Genera y descarga
6. Redimensiona a 192x192 y 512x512

### Opción 2: Usar una imagen
1. Crea o elige una imagen relacionada con video
2. Redimensiona a 192x192 píxeles → guarda como `icon-192.png`
3. Redimensiona a 512x512 píxeles → guarda como `icon-512.png`
4. Asegúrate de que tenga fondo o sea transparente

## 🚀 Desplegar la PWA

### Opción A: GitHub Pages (Gratis)

1. Crea un repositorio en GitHub
2. Sube todos los archivos:
   ```
   creador-video.html
   manifest.json
   service-worker.js
   icon-192.png
   icon-512.png
   ```
3. Ve a Settings → Pages
4. Selecciona la rama main
5. Guarda y espera unos minutos
6. Tu PWA estará en: `https://tu-usuario.github.io/tu-repo`

### Opción B: Netlify (Gratis)

1. Ve a https://netlify.com
2. Arrastra la carpeta con todos los archivos
3. ¡Listo! Tendrás una URL tipo `https://random-name.netlify.app`

### Opción C: Vercel (Gratis)

1. Ve a https://vercel.com
2. Importa desde GitHub o sube archivos
3. Despliega automáticamente

## 📱 Características de la PWA

### ✨ Funcionalidades Implementadas:

1. **Instalable** 
   - Aparece banner de instalación en navegadores compatibles
   - Botón "📱 Instalar App" en la esquina inferior derecha
   - Se puede instalar en móvil y escritorio

2. **Funciona Offline**
   - Service Worker cachea los archivos
   - Funciona sin conexión después de la primera visita
   - Las imágenes y audios del usuario se procesan localmente

3. **Standalone**
   - Se abre como aplicación nativa
   - Sin barra de navegador
   - Pantalla completa en móviles

4. **Actualizaciones Automáticas**
   - Detecta nuevas versiones
   - Pregunta si quiere actualizar
   - Actualización con un click

5. **Atajos de Aplicación**
   - Acceso directo a "Imagen + Audios"
   - Acceso directo a "Slideshow"

## 🔧 Configuración Post-Instalación

### Actualizar rutas (si es necesario)

Si tu aplicación NO está en la raíz del dominio, actualiza las rutas en:

**manifest.json:**
```json
"start_url": "/tu-carpeta/creador-video.html",
```

**service-worker.js:**
```javascript
const urlsToCache = [
  '/tu-carpeta/creador-video.html',
  '/tu-carpeta/'
];
```

**creador-video.html:**
```javascript
navigator.serviceWorker.register('/tu-carpeta/service-worker.js')
```

**manifest.json (links de iconos y manifest):**
```html
<link rel="manifest" href="/tu-carpeta/manifest.json">
<link rel="apple-touch-icon" href="/tu-carpeta/icon-192.png">
```

## 📊 Probar la PWA Localmente

### Con Python:
```bash
# Python 3
python -m http.server 8000

# Abre: http://localhost:8000/creador-video.html
```

### Con Node.js:
```bash
npx http-server -p 8000

# Abre: http://localhost:8000/creador-video.html
```

⚠️ **Nota:** La instalación de PWA solo funciona en HTTPS (excepto localhost)

## 🧪 Verificar PWA

1. Abre Chrome DevTools (F12)
2. Ve a la pestaña "Application"
3. Verifica:
   - ✅ Manifest: Debe mostrar toda la info
   - ✅ Service Workers: Debe estar "activated and running"
   - ✅ Storage: Debe mostrar caché

## 📱 Instalar en Diferentes Dispositivos

### Chrome/Edge (Desktop):
- Banner automático o
- Icono de instalar (⊕) en la barra de direcciones

### Chrome (Android):
- Banner "Agregar a pantalla de inicio"
- Menú → "Instalar app"

### Safari (iOS):
- Botón compartir
- "Agregar a pantalla de inicio"

## 🎯 Checklist de Producción

- [ ] Crear icon-192.png
- [ ] Crear icon-512.png  
- [ ] Subir todos los archivos a hosting
- [ ] Verificar que esté en HTTPS
- [ ] Probar instalación
- [ ] Probar funcionalidad offline
- [ ] Verificar en múltiples dispositivos

## 📝 Notas Importantes

1. **HTTPS Requerido:** Las PWA requieren HTTPS para funcionar (excepto localhost)
2. **Iconos Obligatorios:** Sin los iconos, la instalación puede fallar
3. **Service Worker:** Actualiza la constante `CACHE_NAME` cuando hagas cambios importantes
4. **localStorage:** Las preferencias guardadas persisten incluso instalada

## 🐛 Troubleshooting

**No aparece el banner de instalación:**
- Verifica que estés en HTTPS
- Verifica que el manifest.json esté correctamente enlazado
- Verifica que los iconos existan
- Abre DevTools → Application → Manifest para ver errores

**Service Worker no se registra:**
- Verifica la ruta en `navigator.serviceWorker.register()`
- Mira la consola para errores
- Asegúrate que el archivo service-worker.js esté en la raíz correcta

**No funciona offline:**
- Verifica que el Service Worker esté activado
- Verifica en DevTools → Application → Service Workers
- Prueba recargando la página después de instalar

## 🎉 ¡Listo!

Tu aplicación ahora es una PWA completa que se puede:
- ✅ Instalar en cualquier dispositivo
- ✅ Usar sin conexión
- ✅ Ejecutar como app nativa
- ✅ Actualizar automáticamente

---

**Creado con ❤️ - Video Creator PWA**
