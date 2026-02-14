const CACHE_NAME = 'video-creator-v1';
const urlsToCache = [
  '/creador-video.html',
  '/'
];

// Instalar Service Worker
self.addEventListener('install', event => {
  console.log('Service Worker: Instalando...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Service Worker: Archivos en caché');
        return cache.addAll(urlsToCache);
      })
      .catch(err => {
        console.log('Service Worker: Error al cachear', err);
      })
  );
  self.skipWaiting();
});

// Activar Service Worker
self.addEventListener('activate', event => {
  console.log('Service Worker: Activando...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('Service Worker: Eliminando caché antigua', cache);
            return caches.delete(cache);
          }
        })
      );
    })
  );
  return self.clients.claim();
});

// Interceptar peticiones
self.addEventListener('fetch', event => {
  // Solo cachear peticiones GET
  if (event.request.method !== 'GET') return;
  
  // No cachear blobs o datos
  if (event.request.url.startsWith('blob:')) return;
  
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Si está en caché, devolver desde caché
        if (response) {
          return response;
        }
        
        // Si no está en caché, hacer petición de red
        return fetch(event.request).then(response => {
          // No cachear respuestas no válidas
          if (!response || response.status !== 200 || response.type === 'opaque') {
            return response;
          }
          
          // Clonar la respuesta
          const responseToCache = response.clone();
          
          // Añadir al caché para futuras peticiones
          caches.open(CACHE_NAME)
            .then(cache => {
              cache.put(event.request, responseToCache);
            });
          
          return response;
        });
      })
      .catch(() => {
        // Si falla la red, mostrar página offline (opcional)
        return new Response('Offline - La aplicación funciona sin conexión', {
          headers: { 'Content-Type': 'text/plain' }
        });
      })
  );
});

// Manejo de mensajes del cliente
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
