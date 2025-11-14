import sys
import os

# Añadir el directorio 'app' al PYTHONPATH para que las importaciones relativas funcionen
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify

from logging_config import setup_logging
from config import config
from whatsapp_service import WhatsAppService
from conversation_flow import handle_message

# --- Inicialización de la Aplicación ---

# 1. Inicializar Flask
app = Flask(__name__)

# 2. Configurar el logging
logger = setup_logging()

# 3. Cargar configuración e inicializar servicios
try:
    logger.info(f"Cargando configuración para el asistente: {config.ASSISTANT_NAME}")
    whatsapp_service = WhatsAppService(
        account_sid=config.TWILIO_ACCOUNT_SID,
        auth_token=config.TWILIO_AUTH_TOKEN,
        twilio_number=config.TWILIO_WHATSAPP_NUMBER
    )
except Exception as e:
    logger.error(f"Error fatal al inicializar la aplicación: {e}", exc_info=True)
    sys.exit(1)

# --- Endpoints de la API ---

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    try:
        # La estructura del body depende del proveedor. Esto es para Twilio.
        incoming_msg = request.values.get('Body', '').strip()
        sender_id = request.values.get('From', '')  # ej: 'whatsapp:+5491155554444'
        
        logger.info(f"Mensaje recibido de {sender_id}: '{incoming_msg}'")

        if not incoming_msg or not sender_id:
            logger.warning("Webhook recibido sin cuerpo de mensaje o sin remitente.")
            return jsonify({"status": "error", "message": "Missing Body or From field"}), 400

        response_text = handle_message(sender_id, incoming_msg)
        whatsapp_service.send_message(sender_id, response_text)

        return jsonify({"status": "ok"}), 200
    except Exception as e:
        logger.error(f"Error procesando el webhook: {e}", exc_info=True)
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500

if __name__ == "__main__":
    logger.info("Iniciando Bot Asistente con servidor Flask...")
    # El host '0.0.0.0' es crucial para que Flask sea accesible desde fuera del contenedor Docker.
    app.run(host='0.0.0.0', port=5000, debug=False)