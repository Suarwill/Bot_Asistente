import json
import os
from dotenv import load_dotenv

def create_env_if_not_exists():
    env_path = '.env'
    if not os.path.exists(env_path):
        print(f"Archivo '{env_path}' no encontrado. Creando uno con valores por defecto.")
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write("# Clave de API para el servicio de WhatsApp (puede ser un valor de prueba)\n")
            f.write("WHATSAPP_API_KEY=YOUR_MOCK_WHATSAPP_API_KEY\n")

create_env_if_not_exists()

load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.getenv("ASSISTANT_CONFIG_PATH", "/app/config/assistant_config.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.ASSISTANT_NAME = self.data.get("ASSISTANT_NAME", "Asistente Genérico")
        self.WELCOME_MESSAGE = self.data.get("WELCOME_MESSAGE", "Bienvenido.")
        self.CONVERSATION_FLOW = self.data.get("CONVERSATION_FLOW", {})

        self.WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")
        

# Instancia global de configuración
config = Config()