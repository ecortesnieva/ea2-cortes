# Buscador Automatizado de Artistas - TheAudioDB API

## A. Definición del Contexto y Narrativa

* [cite_start]**Stakeholder:** **Music Curator & Content Creator (Editor de Contenido Musical)**[cite: 6]. [cite_start]Este perfil técnico necesita automatizar la recolección de metadatos básicos de artistas musicales (nombre oficial, género y país de origen) para poblar catálogos y plataformas de streaming de manera masiva, eliminando por completo la búsqueda manual en navegadores web[cite: 7].
* [cite_start]**Propuesta de Valor (Problema/Solución):** El proceso manual de documentar biografías y géneros de artistas genera pérdidas de tiempo y errores de digitación[cite: 8]. [cite_start]Esta aplicación resuelve la necesidad ejecutando una consulta puntual y ligera a la API de TheAudioDB por consola[cite: 4, 8]. [cite_start]Procesa los campos estructurados en segundos, garantizando consistencia de datos y permitiendo su portabilidad total mediante contenedores Docker e integración continua con Jenkins[cite: 1, 14, 22].

---

## B. Guía de Configuración y Variables de Entorno

[cite_start]Para resguardar la seguridad técnica y evitar el hardcoding de credenciales, la aplicación requiere las siguientes variables de entorno[cite: 12, 15]:

* [cite_start]`API_KEY_PROYECTO`: Llave de acceso para la API de TheAudioDB (para pruebas públicas se utiliza el valor `2`)[cite: 16].
* `ARTISTA_A_BUSCAR`: Nombre del artista musical que se desea consultar (Ejemplo: `Coldplay`, `Linkin Park`).

### Inicialización de Variables de Entorno

**En Windows (PowerShell):**
```powershell
$env:API_KEY_PROYECTO="2"
$env:ARTISTA_A_BUSCAR="Coldplay"
