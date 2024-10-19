import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

introduccion = """
Este es tu único contexto, lo único que sabes de tí:
1. Tú eres una inteligencia artificial creada por Alejandro Portaluppi

2. Te llamas Bob

3. Tu propósito es responder consultas de la gente

4. Las respuestas que generes no deben ser largas
Comencemos:""" # Acá puedes personalizar el comportamiento de la IA

def train_ai(): # Entrena a la IA para que entienda qué debe responder en base a lo que le piden
    try:
        client = Groq(api_key = os.getenv('API_KEY')) # Coloca en un archivo .env tu API Key. Lee el readme para más información

        intro = introduccion # El primer mensaje lo enviamos para "entrenarlo"

        historial = [{
            "role": "system",
            "content": intro
        }]

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages = historial,
            temperature=0,
        ).choices[0].message.content

        historial.append({
            "role": "assistant",
            "content": response
        })

        return historial

    except Exception as e:
        print(e)

def enviar_mensaje(mensaje: str, historial: list[str]):
    try:
        client = Groq(api_key = os.getenv('API_KEY'))

        historial.append({
            "role": "user",
            "content": mensaje
        })

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages = historial,
            temperature=0,
        ).choices[0].message.content

        historial.append({
            "role": "assistant",
            "content": response
        })

        return historial
    except Exception as e:
        print(e)

chat = train_ai()

# A modo de ejemplo envío dos mensajes
chat = enviar_mensaje("Cómo te llamas?", chat)
print(chat[-1]["content"])

chat = enviar_mensaje("Entiendo. Decime la diferencia entre http y https", chat)
print(chat[-1]["content"])

# Siguiendo el mismo patrón, se puede continuar la conversación como si fuera un chat
