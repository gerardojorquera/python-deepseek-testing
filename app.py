from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Cargar las variables del archivo .env al entorno del sistema
load_dotenv()

# 2. Recuperar el valor usando os.environ.get
api_key = os.environ.get("API_KEY")

# 3. Comprobar que se cargó correctamente
if api_key:
    print("¡Clave cargada con éxito!")

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1",  # Reemplaza el modelo antiguo por este
        messages=[
            {
                "role": "user",
                "content": "Nombrame tres personajes del señor de los anillos",
            }
        ],
    )
    # print(chat)
    print(chat.choices[0].message.content)
else:
    print("Error: No se pudo encontrar la API KEY. Revisa tu archivo .env")