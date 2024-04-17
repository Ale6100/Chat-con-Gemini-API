import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

safety_settings = [ # Para quitarle la censura a la IA
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
]

introduccion = """
Este es tu único contexto, lo único que sabes de tí:
1. Tú eres una inteligencia artificial creada por Alejandro Portaluppi

2. Te llamas Bob

3. Tu propósito es responder consultas de la gente

4. Las respuestas que generes no deben ser largas
Comencemos:""" # Acá puedes personalizar el comportamiento de la IA

def train_ai(): # Entrena a la IA para que entienda qué debe responder en base a lo que le piden
    try:
        genai.configure(api_key=os.getenv('API_KEY')) # Coloca en un archivo .env tu API Key. Lee el readme para más información
        genai.GenerationConfig(candidate_count=0) # Cantidad de respuestas que la IA puede dar al mismo tiempo

        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])

        chat.send_message(introduccion, safety_settings=safety_settings) # El primer mensaje lo enviamos para "entrenarlo"

        return chat
    except Exception as e:
        print(e)

chat = train_ai()

# A modo de ejemplo envío dos mensajes
response_ia = chat.send_message("Cómo te llamas?", safety_settings=safety_settings)
print(response_ia.text)

response_ia = chat.send_message("Entiendo. Decime la diferencia entre http y https", safety_settings=safety_settings)
print(response_ia.text)

# Siguiendo el mismo patrón, se puede continuar la conversación como si fuera un chat
