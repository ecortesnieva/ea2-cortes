import os
import sys
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def buscar_artista():
    # 1. Recuperar la API KEY de forma segura
    api_key = os.getenv('API_KEY_PROYECTO', '2') 
    
    # 2. DINÁMICO: Recupera el artista desde la variable de entorno. Si no hay ni uno, usa 'Coldplay' por defecto.
    artista_buscado = os.getenv('ARTISTA_A_BUSCAR', 'Coldplay')
    
    url = f"https://www.theaudiodb.com/api/v1/json/{api_key}/search.php?s={artista_buscado}"
    print(f"Buscando información en la API para: '{artista_buscado}'...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            print("⚠️ Error de Formato: La respuesta del servidor no es un JSON válido.", file=sys.stderr)
            sys.exit(1)

        # Procesamiento de datos
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

    except HTTPError as http_err:
        print(f"⚠️ Error de HTTP (Código {http_err.response.status_code})", file=sys.stderr)
        sys.exit(1)
    except ConnectionError:
        print("⚠️ Error de Conexión: Servidor inaccesible.", file=sys.stderr)
        sys.exit(1)
    except Timeout:
        print("⚠️ Error de Tiempo (Timeout).", file=sys.stderr)
        sys.exit(1)
    except RequestException:
        print("⚠️ Error General de Petición.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    buscar_artista()
