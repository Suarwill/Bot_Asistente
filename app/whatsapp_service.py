import logging
from twilio.rest import Client

logger = logging.getLogger("BotAsistente")

class WhatsAppService:
    """
    Clase de servicio para enviar mensajes de WhatsApp a través de la API de Twilio.
    """

    def __init__(self, account_sid: str, auth_token: str, twilio_number: str):
        """
        Inicializa el cliente de Twilio.
        :param account_sid: El SID de la cuenta de Twilio.
        :param auth_token: El token de autenticación de Twilio.
        :param twilio_number: El número de WhatsApp de Twilio (ej. 'whatsapp:+14155238886').
        """
        try:
            self.client = Client(account_sid, auth_token)
            self.twilio_number = twilio_number
            logger.info("WhatsAppService (Twilio) inicializado correctamente.")
        except Exception as e:
            logger.error(f"Error al inicializar el cliente de Twilio: {e}")
            self.client = None

    def send_message(self, recipient: str, message: str):
        if not self.client:
            logger.error("No se puede enviar mensaje, el cliente de Twilio no está inicializado.")
            return

        try:
            logger.info(f"Enviando a {recipient}: {message}")
            self.client.messages.create(body=message, from_=self.twilio_number, to=recipient)
        except Exception as e:
            logger.error(f"Error al enviar mensaje a {recipient} vía Twilio: {e}", exc_info=True)