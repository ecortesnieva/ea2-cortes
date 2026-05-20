# Buscador Automatizado de Artistas - TheAudioDB API

## A. Definición del Contexto y Narrativa

* **Stakeholder:** **Music Curator & Content Creator (Editor de Contenido Musical)**. Este perfil técnico necesita automatizar la recolección de metadatos básicos de artistas musicales (nombre oficial, género y país de origen) para poblar catálogos y plataformas de streaming de manera masiva, eliminando por completo la búsqueda manual en navegadores web.
* **Propuesta de Valor (Problema/Solución):** El proceso manual de documentar biografías y géneros de artistas genera pérdidas de tiempo y errores de digitación. Esta aplicación resuelve la necesidad ejecutando una consulta puntual y ligera a la API de TheAudioDB por consola. Procesa los campos estructurados en segundos, garantizando consistencia de datos y permitiendo su portabilidad total mediante contenedores Docker e integración continua con Jenkins.

---

## B. Guía de Configuración y Variables de Entorno

Para resguardar la seguridad técnica y evitar el hardcoding de credenciales, la aplicación requiere las siguientes variables de entorno:

* `API_KEY_PROYECTO`: Llave de acceso para la API de TheAudioDB (para pruebas públicas se utiliza el valor `2`).
* `ARTISTA_A_BUSCAR`: Nombre del artista musical que se desea consultar (Ejemplo: `Coldplay`, `Linkin Park`).

### Inicialización de Variables de Entorno

**En Windows (PowerShell):**
```powershell
$env:API_KEY_PROYECTO="2"
$env:ARTISTA_A_BUSCAR="Coldplay"
