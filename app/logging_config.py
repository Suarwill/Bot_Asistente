import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    """
    Configura el sistema de logging para la aplicación.
    Los logs se escribirán en la consola, en un archivo general y en un archivo de errores.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configuración del logger principal
    logger = logging.getLogger("BotAsistente")
    logger.setLevel(logging.INFO)

    # Formato de los logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler para la consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler para el archivo de logs general (rotación de archivos)
    file_handler = RotatingFileHandler(os.path.join(log_dir, 'bot_asistente.log'),
                                       maxBytes=1024 * 1024 * 5,  # 5 MB
                                       backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para el archivo de errores (rotación de archivos)
    error_handler = RotatingFileHandler(os.path.join(log_dir, 'bot_asistente_error.log'),
                                        maxBytes=1024 * 1024 * 5,  # 5 MB
                                        backupCount=5)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    logger.info("Sistema de logging configurado.")
    return logger