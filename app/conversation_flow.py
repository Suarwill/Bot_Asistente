import logging
from app.config import config

logger = logging.getLogger("BotAsistente")

# Diccionario simple para mantener el estado por usuario (sender_id)
# En un entorno de producción, esto debería ser una base de datos como Redis para persistencia y escalabilidad.
user_states = {}

def handle_message(sender_id: str, message_text: str) -> str:
    message_text = message_text.strip().lower()
    current_state = user_states.get(sender_id)
    
    logger.info(f"Usuario {sender_id} en estado '{current_state}' envió: '{message_text}'")

    # Lógica basada en el estado actual del usuario
    if current_state == "product_info":
        user_states.pop(sender_id, None)  # Limpiar estado después de usarlo
        return f"Entendido, buscando información sobre productos de '{message_text}'... (Lógica de búsqueda no implementada)"
    
    if current_state == "sales_inquiry":
        user_states.pop(sender_id, None)
        logger.info(f"Dato de contacto para ventas de {sender_id}: {message_text}")
        return "Gracias. Un asesor de ventas se pondrá en contacto contigo pronto."

    if current_state == "support_inquiry":
        user_states.pop(sender_id, None)
        logger.info(f"Problema de soporte de {sender_id}: {message_text}")
        return "Hemos registrado tu problema. Un técnico se pondrá en contacto contigo."

    if message_text in ["hola", "hi", "saludos"]:
        response = config.WELCOME_MESSAGE
    elif message_text in config.CONVERSATION_FLOW:
        flow_step = config.CONVERSATION_FLOW[message_text]
        response = flow_step["response"]
        
        # Guardar el siguiente paso esperado para este usuario si está definido
        if "next_step" in flow_step:
            user_states[sender_id] = flow_step["next_step"]
            logger.info(f"Estableciendo estado para {sender_id}: {user_states[sender_id]}")
    else:
        response = "Lo siento, no entendí tu consulta. Por favor, elige una de las opciones numéricas o escribe 'hola' para empezar de nuevo."
        logger.warning(f"Mensaje no reconocido de {sender_id}: '{message_text}'")

    logger.info(f"Respuesta generada para {sender_id}: {response}")
    return response