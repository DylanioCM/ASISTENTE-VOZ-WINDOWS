# ==========================================
# VOICE ASSISTANT - Dylan AI Assistant
# Asistente por voz para Windows
# ==========================================

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

# Inicializar voz
engine = pyttsx3.init()

def hablar(texto):
    print("Asistente:", texto)
    engine.say(texto)
    engine.runAndWait()

# Escuchar voz
def escuchar():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nEscuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language="es-ES")
        print("Tú dijiste:", comando)
        return comando.lower()

    except:
        hablar("No entendí lo que dijiste")
        return ""

# Saludo inicial
hablar("Hola Dylan, asistente iniciado")

# Bucle principal
while True:

    comando = escuchar()

    # ABRIR WEBS
    if "youtube" in comando:
        hablar("Abriendo YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in comando:
        hablar("Abriendo Google")
        webbrowser.open("https://www.google.com")

    elif "spotify" in comando:
        hablar("Abriendo Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "chat gpt" in comando:
        hablar("Abriendo Chat GPT")
        webbrowser.open("https://chat.openai.com")

    # ABRIR APPS
    elif "calculadora" in comando:
        hablar("Abriendo calculadora")
        os.system("start calc")

    elif "bloc de notas" in comando:
        hablar("Abriendo bloc de notas")
        os.system("start notepad")

    elif "cmd" in comando:
        hablar("Abriendo consola")
        os.system("start cmd")

    # HORA
    elif "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora}")

    # APAGAR PC
    elif "apagar computadora" in comando:
        hablar("Apagando computadora")
        os.system("shutdown /s /t 5")

    # BUSQUEDA EN GOOGLE
    elif "buscar" in comando:
        buscar = comando.replace("buscar", "")
        hablar(f"Buscando {buscar} en Google")
        webbrowser.open(f"https://www.google.com/search?q={buscar}")

    # SALIR
    elif "salir" in comando:
        hablar("Cerrando asistente")
        break

    # COMANDO DESCONOCIDO
    elif comando != "":
        hablar("Ese comando no está programado")