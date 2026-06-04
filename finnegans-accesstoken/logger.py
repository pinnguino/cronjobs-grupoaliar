import os
import logging
from logging.handlers import RotatingFileHandler

# Convertir MB a Bytes. Devuelve un entero.
def mb_to_bytes(mb: int | float) -> int:
    return int(mb * 1024**2)

# Configuración del logger
logging.basicConfig(
    level = logging.INFO, # Nivel mínimo de mensajes a registrar. Niveles más bajos se ignoran (DEBUG < INFO < WARNING < ERROR < CRITICAL)
    format = "%(asctime)s - [%(levelname)s] | %(name)s: %(message)s", # Formato de los mensajes. Usa el formato 
    handlers = [ RotatingFileHandler("finnegans.log", maxBytes = mb_to_bytes(5), backupCount = 2) ]
)

# Función para crear loggers con nombre
def get_logger(name: str = None) -> logging.Logger:
    return logging.getLogger(name or __name__)