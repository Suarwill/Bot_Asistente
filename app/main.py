import sys
import os

# Añadir el directorio 'app' al PYTHONPATH para que las importaciones relativas funcionen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Bot_Asistente.app.logging_config import setup_logging
from Bot_Asistente.app.config import config
from whatsapp_service import WhatsAppService
from conversation_flow import handle_message

if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Iniciando Bot Asistente...")

    # 2. Cargar configuración
    try:
        logger.info(f"Cargando configuración para el asistente: {config.ASSISTANT_NAME}")
        whatsapp_api_key = config.WHATSAPP_API_KEY
    except Exception as e:
        logger.error(f"Error al cargar la configuración: {e}")
        sys.exit(1)

    # 3. Inicializar el servicio de WhatsApp (simulado)
    whatsapp_service = WhatsAppService(whatsapp_api_key)

    # 4. Simular un mensaje entrante y procesarlo
    simulated_message = input("Escribe un mensaje para el bot (ej. 'hola', '1', 'consulta de ventas'): ")
    response = handle_message(simulated_message)
    whatsapp_service.send_message("user_phone_number", response) # 'user_phone_number' sería el número real del usuario

    logger.info("Bot Asistente finalizado (simulación de un solo mensaje).")