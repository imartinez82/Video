# 🎬 Creador de Videos - PWA

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![PWA](https://img.shields.io/badge/PWA-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Aplicación web progresiva (PWA) para crear videos profesionales con imágenes y audio. Incluye slideshow con efectos dinámicos y texto personalizable.

## ✨ Características

### 🎥 Modo 1: Imagen + Audios
- Una imagen fija
- Hasta 5 pistas de audio (secuenciales)
- Fade in/out automático
- Duración basada en los audios

### 🎞️ Modo 2: Slideshow + Música
- Múltiples imágenes con efectos dinámicos
- Drag & drop para reordenar
- Detección automática de duplicados
- Una pista de música de fondo
- Efectos aleatorios (zoom, pan)
- Transiciones suaves configurables
- Texto superpuesto personalizable

### 📝 Configuración de Texto
- Comic Sans MS 60px (predeterminado)
- 10 fuentes disponibles
- Negrita y cursiva
- 36 colores predefinidos
- Borde personalizable (color y grosor)
- Posición: inferior derecha
- Sombra automática

### ⚙️ Configuraciones Avanzadas
- Fade in/out ajustable (0-5 segundos)
- Duración por imagen (1-60 segundos)
- Duración máxima de video (hasta 20 min)
- Formatos: MP4 / WebM
- Calidad: 48kHz, 320kbps audio, 5Mbps video
- Guardar preferencias (localStorage)

### 📱 PWA Features
- ✅ Instalable (móvil y escritorio)
- ✅ Funciona offline
- ✅ Actualizaciones automáticas
- ✅ Standalone mode
- ✅ Banner de instalación

## 🚀 Instalación Rápida

### Opción 1: GitHub Pages (Recomendado)

1. **Fork este repositorio**
2. **Añade los iconos** (Ver sección "Crear Iconos")
3. **Habilita GitHub Pages**:
   - Settings → Pages
   - Source: main branch
   - Save
4. **Accede a tu app**:
   - `https://tu-usuario.github.io/video-creator-pwa`

### Opción 2: Clonar y ejecutar localmente

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/video-creator-pwa.git
cd video-creator-pwa

# Servidor local con Python
python -m http.server 8000

# O con Node.js
npx http-server -p 8000

# Abrir en navegador
# http://localhost:8000/creador-video.html
```

## 🎨 Crear Iconos (IMPORTANTE)

La PWA necesita 2 iconos. Opciones:

### Opción A: Generador Online
1. Ve a https://favicon.io/favicon-generator/
2. Configuración:
   - Texto: "🎬" o "VC"
   - Fondo: #667eea
   - Color texto: #ffffff
3. Genera y descarga
4. Renombra a:
   - `icon-192.png` (192x192 px)
   - `icon-512.png` (512x512 px)
5. Coloca en la raíz del proyecto

### Opción B: Desde Imagen
1. Usa cualquier editor (Photoshop, GIMP, Canva)
2. Crea dos versiones: 192x192 y 512x512
3. Guarda como PNG
4. Coloca en la raíz del proyecto

## 📁 Estructura del Proyecto

```
video-creator-pwa/
├── creador-video.html    # Aplicación principal
├── manifest.json         # Configuración PWA
├── service-worker.js     # Service Worker (offline)
├── icon-192.png         # Icono 192x192 (CREAR)
├── icon-512.png         # Icono 512x512 (CREAR)
├── PWA-README.md        # Guía PWA completa
├── APK-GUIDE.md         # Guía para crear APK
└── README.md            # Este archivo
```

## 🔧 Configuración

### Personalizar URLs

Si tu app NO está en la raíz del dominio, actualiza:

**manifest.json:**
```json
"start_url": "/tu-carpeta/creador-video.html"
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

## 📱 Convertir a APK

Lee la guía completa en **APK-GUIDE.md**

**Resumen rápido:**
1. Despliega la PWA (GitHub Pages, Netlify, etc.)
2. Ve a https://www.pwabuilder.com
3. Pega tu URL
4. Generate → Android
5. Descarga APK
6. Instala en Android

## 💾 Guardar Preferencias

La app incluye un botón "💾 Guardar Preferencias" que guarda:
- Configuraciones de slideshow
- Configuraciones de texto
- Formato de salida
- Todas las personalizaciones

Las preferencias se guardan en localStorage y persisten entre sesiones.

## 🎯 Uso

### Crear Video Imagen + Audios:
1. Pestaña "Imagen + Audios"
2. Selecciona 1 imagen
3. Selecciona 1-5 audios
4. (Opcional) Personaliza configuraciones
5. "Crear Video"

### Crear Slideshow:
1. Pestaña "Slideshow + Música"
2. Selecciona múltiples imágenes
3. Arrastra para reordenar
4. Selecciona música
5. Configura texto (opcional)
6. Ajusta efectos y transiciones
7. (Opcional) "💾 Guardar Preferencias"
8. "Crear Slideshow"

## 🐛 Solución de Problemas

### La PWA no se instala
- ✅ Verifica que esté en HTTPS (no localhost)
- ✅ Verifica que los iconos existan
- ✅ Abre DevTools → Application → Manifest

### Service Worker no funciona
- ✅ Verifica la ruta en el registro
- ✅ Mira la consola para errores
- ✅ DevTools → Application → Service Workers

### No funciona offline
- ✅ Verifica que el SW esté activado
- ✅ Recarga después de instalar
- ✅ Limpia caché y vuelve a cargar

## 🌐 Navegadores Soportados

- ✅ Chrome/Edge (Desktop & Mobile)
- ✅ Firefox (Desktop & Mobile)
- ✅ Safari (iOS & macOS)
- ✅ Samsung Internet
- ✅ Opera

## 📊 Especificaciones Técnicas

- **Resolución Video:** 1280x720 (HD)
- **Tasa de frames:** 25 FPS
- **Audio:** 48kHz, Stereo, 320kbps
- **Video:** 5 Mbps
- **Codec Video:** VP8/VP9/H264 (según navegador)
- **Codec Audio:** Opus/AAC
- **Formatos salida:** WebM, MP4

## 🔐 Privacidad

- ✅ Todo el procesamiento es local
- ✅ No se suben archivos a ningún servidor
- ✅ No se recopilan datos del usuario
- ✅ Las preferencias se guardan localmente
- ✅ Funciona completamente offline

## 📄 Licencia

MIT License - Úsalo libremente para proyectos personales o comerciales.

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/amazing`)
3. Commit cambios (`git commit -m 'Add feature'`)
4. Push a la rama (`git push origin feature/amazing`)
5. Abre un Pull Request

## 📞 Recursos

- [PWA Documentation](https://web.dev/progressive-web-apps/)
- [PWABuilder](https://www.pwabuilder.com)
- [Service Worker Guide](https://developers.google.com/web/fundamentals/primers/service-workers)
- [Web App Manifest](https://web.dev/add-manifest/)

## ⭐ Agradecimientos

Desarrollado con:
- Canvas API
- Web Audio API
- MediaRecorder API
- Service Workers
- LocalStorage
- Drag & Drop API

---

**¿Te gusta el proyecto? ¡Dale una estrella ⭐!**

**¿Problemas o sugerencias? Abre un issue**
