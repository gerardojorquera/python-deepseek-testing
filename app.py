from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Cargar las variables del archivo .env al entorno del sistema
load_dotenv()

# 2. Recuperar el valor usando os.environ.get
api_key = os.environ.get("API_KEY")
pregunta = "Nombrame tres personajes del señor de los anillos"

# 3. Comprobar que se cargó correctamente
if api_key:
    print("=> Iniciando uso de la IA de DeepSeek... para hacer una pregunta: ", pregunta)
    print("¡Clave cargada con éxito!: ", api_key[0:4] + "..." + api_key[-4:])  # Muestra solo los primeros y últimos 4 caracteres
    print("---------------------------------")
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1",  # Reemplaza el modelo antiguo por este
        messages=[
            {
                "role": "user",
                "content": pregunta,
            }
        ],
    )
    # print(chat)
    print(chat.choices[0].message.content)
else:
    print("Error: No se pudo encontrar la API KEY. Revisa tu archivo .env")