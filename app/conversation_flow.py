import logging
from app.config import config

logger = logging.getLogger("BotAsistente")

def handle_message(message_text: str) -> str:
    """
    Procesa un mensaje entrante y genera una respuesta basada en el flujo conversacional.
    """
    message_text = message_text.strip().lower()
    response = ""

    if message_text in ["hola", "hi", "saludos"]:
        response = config.WELCOME_MESSAGE
    elif message_text in config.CONVERSATION_FLOW:
        flow_step = config.CONVERSATION_FLOW[message_text]
        response = flow_step["response"]
        logger.info(f"Usuario eligió opción '{message_text}'. Siguiente paso: {flow_step.get('next_step', 'N/A')}")
    elif "producto" in message_text or "info" in message_text:
        response = config.CONVERSATION_FLOW.get("1", {}).get("response", "No entendí sobre qué producto quieres información.")
    elif "venta" in message_text or "asesor" in message_text:
        response = config.CONVERSATION_FLOW.get("2", {}).get("response", "No entendí tu consulta de ventas.")
    elif "soporte" in message_text or "problema" in message_text:
        response = config.CONVERSATION_FLOW.get("3", {}).get("response", "No entendí tu solicitud de soporte.")
    else:
        response = "Lo siento, no entendí tu consulta. Por favor, elige una de las opciones o reformula tu pregunta."
        logger.warning(f"Mensaje no reconocido: '{message_text}'")

    logger.info(f"Respuesta generada: {response}")
    return response