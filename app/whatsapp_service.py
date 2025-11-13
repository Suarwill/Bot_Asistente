import logging

logger = logging.getLogger("BotAsistente")

class WhatsAppService:

    # Clase de servicio para simular el envío y recepción de mensajes de WhatsApp.
    # En un entorno real, esto se conectaría a una API de WhatsApp (ej. Twilio, Meta Business API).

    def __init__(self, api_key):
        self.api_key = api_key
        logger.info(f"WhatsAppService inicializado con API Key: {'*' * (len(api_key) - 4) + api_key[-4:] if api_key else 'N/A'}")

    def send_message(self, recipient: str, message: str):
        logger.info(f"Simulando envío a {recipient}: {message}")
        # Aquí iría la lógica real para enviar el mensaje a través de la API

    def receive_message(self) -> dict:
        """Simula la recepción de un mensaje de WhatsApp. (Para pruebas manuales)"""
        # En un sistema real, esto sería un webhook o un polling.
        # Para esta demostración, main.py simulará la entrada.
        pass