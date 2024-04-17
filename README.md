# Creación y entrenamiento de un chat simple usando la API de Gemini

Bienvenido! En este pequeño proyecto dejo un código funcional donde se crea un chat personalizado usando Gemini API

La idea de este proyecto nació gracias al hecho de que en el proyecto [Asistente-Virtual-Python](https://github.com/Ale6100/Asistente-Virtual-Python.git) quería implementarle IA. La parte central de ese nuevo código creado lo dejo acá de manera pública.

## Pre-requisitos 📋

El código está hecho y testeado utilizando la versión 3.12.3 de Python y un Windows 11 de 64bits

## Instalación 🔧 (en windows)

Primero debes crear un entorno virtual con el comando

```bash
py -3 -m venv .venv
```

luego actívalo con el comando

```bash
.venv\Scripts\activate
```

A continuación, instala las dependencias con el comando

```bash
pip install -r requirements.txt
```

Recuerda que debes activar el entorno virtual siempre que desees usarlo

Es necesaria la creación de una variable de entorno mediante la elaboración de un archivo .env. Este archivo debe ser completado con el siguiente campo, el cual deberá incluir el valor de tu API key de Gemini. Si no tienes una, consíguela [aquí](https://aistudio.google.com/app/apikey)

```env
API_KEY = X # Coloca aquí tu API Key
```

## Despliegue 📦

Ejecuta el archivo [script.py](/script.py) y listo. Lee los comentarios para entender su funcionamiento

## Autor ✒️

| ![Alejandro Portaluppi](https://avatars.githubusercontent.com/u/107259761?size=50)
|:-:
| **Alejandro Portaluppi**
|[![GitHub](https://img.shields.io/badge/github-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ale6100) [![LinkedIn](https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alejandro-portaluppi)
