# Evaluacion 2 - Administración de Contenedores y Pipelines (DRY7122)

**Estudiante:** Emilio Cortes  
**Especialidad:** Ingeniería en Infraestructura Tecnológica y Redes  
**Institución:** DuocUC  

---

## 🚀 Resumen del Proyecto
Este repositorio contiene el despliegue contenerizado de una aplicación en Python que consume la API de **TheAudioDB** de forma dinámica y segura, integrada con la lógica de automatización para un Pipeline de CI/CD.

## 📁 Estructura del Repositorio
* **`app.py`**: Código fuente en Python optimizado con manejo de excepciones y consumo dinámico mediante variables de entorno (`ARTISTA_A_BUSCAR`).
* **`Dockerfile`**: Archivo de configuración permanente para la construcción de la imagen basada en `python:3.9-slim`.
* **`requirements.txt`**: Definición de librerías requeridas (`requests`).
* **`output.txt`**: Reporte real de ejecución en entorno Linux (Killercoda) que demuestra el estado `Exited (0)` y la captura de logs con resultados exitosos.
* **`evidencias/jenkins/pipeline_script.txt`**: Script en Groovy con la estructura formal del Pipeline exigido por la pauta (`Preparation` y `Build`).

---

## 🐋 Comandos de Ejecución (Motor Docker)

Para recrear el entorno en cualquier máquina con Docker:

```bash
# 1. Construir la imagen
docker build -t music-app-img .

# 2. Ejecutar de forma dinámica pasándole el artista deseado
docker run --name samplerunning_new -e API_KEY_PROYECTO="2" -e ARTISTA_A_BUSCAR="Linkin Park" music-app-img
