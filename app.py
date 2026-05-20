import os
import sys
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def buscar_artista():
    # SEGURIDAD: Recuperar la API KEY desde variables de entorno
    api_key = os.getenv('API_KEY_PROYECTO', '2') 
    
    # CONSULTA PUNTUAL: Sin bucles infinitos para cumplir la pauta
    artista_buscado = os.getenv('ARTISTA_A_BUSCAR', 'Coldplay')
    
    url = f"https://www.theaudiodb.com/api/v1/json/{api_key}/search.php?s={artista_buscado}"
    print(f"Iniciando consulta puntual a TheAudioDB para el artista: '{artista_buscado}'...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            print("⚠️ Error de Formato: La respuesta del servidor no es un JSON válido.", file=sys.stderr)
            sys.exit(1)

        # Procesamiento y visualización de datos (>= 3 campos)
        if data and data.get("artists"):
            artista = data["artists"][0]
            print("\n=============================================")
            print(f"✅ RESULTADOS OBTENIDOS")
            print(f"🎸 Artista: {artista.get('strArtist')}")      
            print(f"📁 Género: {artista.get('strGenre', 'N/A')}")  
            print(f"🌍 País: {artista.get('strCountry', 'N/A')}")  
            
            bio = artista.get('strBiographyES') or artista.get('strBiographyEN')
            if bio:
                print(f"📖 Biografía: {bio[:300]}...")             
            print("=============================================\n")
            sys.exit(0) 
        else:
            print(f"❌ No se encontraron registros para el artista '{artista_buscado}'.")
            sys.exit(0)

    # MANEJO ROBUSTO DE ERRORES (>= 4 tipos de excepciones controladas)
    except HTTPError as http_err:
        status = http_err.response.status_code
        print(f"⚠️ Error de HTTP detectado (Código {status}): {http_err}", file=sys.stderr)
        sys.exit(1)
        
    except ConnectionError:
        print("⚠️ Error de Conexión: No se pudo conectar al servidor de la API.", file=sys.stderr)
        sys.exit(1)
        
    except Timeout:
        print("⚠️ Error de Tiempo (Timeout): El servidor tardó demasiado en responder.", file=sys.stderr)
        sys.exit(1)
        
    except RequestException as req_err:
        print(f"⚠️ Error General de Petición: Problema en la llamada de red: {req_err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    buscar_artista()
