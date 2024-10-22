### Librerias #################################################################################################
import speech_recognition as sr                                 # Biblioteca para reconocimiento de voz.
import pyttsx3                                                  # Biblioteca para síntesis de voz (text-to-speech).
import pywhatkit                                                # Para controlar WhatsApp desde el navegador.
import datetime                                                 # Trabajar con fechas y horas.
import wikipedia                                                # Buscar información en Wikipedia.
import webbrowser                                               # Abre el navegador web por defecto.
import keyboard                                                 # Detecta eventos del teclado.
import time                                                     # Trabajar con retardos o pausas en el código.
import dateparser                                               # Analiza fechas en lenguaje natural.
import base64                                                   # Para codificación y decodificación en base64.
from tkinter import messagebox                                  # Muestra cuadros de diálogo emergentes (GUI).
from email.mime.text import MIMEText                            # Crea correos electrónicos con formato MIME.
import pyautogui                                                # Automatización de la interfaz de usuario (control de mouse y teclado).
from deep_translator import GoogleTranslator                    # Traducción de texto usando Google Translate.
import AVMSpeechMath as sm                                      # Biblioteca personalizada para operaciones matemáticas por voz.
from tkinter import *                                           # Para crear interfaces gráficas de usuario (GUI).
from PIL import Image, ImageTk, ImageDraw, ImageFont            # Manipulación de imágenes.
import threading                                                # Ejecuta hilos en paralelo (multitarea).
import unicodedata                                              # Trabaja con cadenas Unicode y elimina acentos.
import re                                                       # Expresiones regulares para buscar patrones en cadenas de texto.
import spotipy                                                  # Interactuar con el API de Spotify.
from spotipy.oauth2 import SpotifyOAuth                         # Maneja la autenticación de Spotify usando OAuth2.
from google.oauth2.credentials import Credentials               # Maneja credenciales de autenticación de Google.
from google_auth_oauthlib.flow import InstalledAppFlow          # Maneja el flujo OAuth para Google.
from google.auth.transport.requests import Request              # Gestiona solicitudes de autenticación a Google.
from googleapiclient.discovery import build                     # Construye servicios de API de Google (Gmail, Calendar, etc.).
import os                                                       # Trabaja con el sistema operativo (archivos y directorios).
import requests                                                 # Realiza solicitudes HTTP a páginas web o APIs.
from sklearn.feature_extraction.text import CountVectorizer     # Convierte texto a vectores de palabras.
from sklearn.naive_bayes import MultinomialNB                   # Implementa el algoritmo Naive Bayes para clasificación.
from sklearn.pipeline import make_pipeline                      # Crea pipelines para procesamiento y clasificación.
import sqlite3                                                  # Trabaja con bases de datos SQLite.
####################################################################################################################################################################################
### Ventana principal #########################################################################################

main_w = Tk()
main_w.title("Julia Asistente Virtual")
main_w.iconbitmap('logos/logojulia.ico')
main_w.geometry("450x625")
main_w.resizable(0, 0)
main_w.configure(bg='#434343')
####################################################################################################################################################################################

### Ventana para mostrar funciones ############################################################################

def load_font(font_path, size):  # Carga una fuente personalizada desde una ruta y tamaño específicos.
    return ImageFont.truetype(font_path, size)

def create_text_image(text, font, image_size=(380, 50), bg_color=(114, 137, 218), text_color="white"):      # Crea una imagen con texto utilizando la fuente y los parámetros de color y tamaño dados.
    img = Image.new('RGB', image_size, color=bg_color)                                                      # Crea una nueva imagen con color de fondo.
    draw = ImageDraw.Draw(img)                                                                              # Inicializa el objeto para dibujar en la imagen.
    draw.text((10, 10), text, font=font, fill=text_color)                                                   # Dibuja el texto en la imagen.
    return img                                                                                              # Devuelve la imagen con el texto.

def create_function_image(func_name, font, image_size=(300, 50), bg_color=(46, 46, 46), text_color=(255, 255, 255)):        # Crea una imagen de función con el nombre de la función y los parámetros visuales.
    img = Image.new('RGB', image_size, color=bg_color)                                                                      # Crea una nueva imagen con un color de fondo.
    draw = ImageDraw.Draw(img)                                                                                              # Inicializa el objeto para dibujar en la imagen.
    draw.text((10, 10), func_name, font=font, fill=text_color)                                                              # Dibuja el nombre de la función.
    return img                                                                                                              # Devuelve la imagen con el texto de la función.

def show_functions_window():                            # Crea y muestra una ventana con las funciones disponibles.
    functions_w = Toplevel(main_w)                      # Crea una nueva ventana secundaria.
    functions_w.title("Funciones disponibles")          # Define el título de la ventana.
    functions_w.geometry("450x600")                     # Define el tamaño de la ventana.
    functions_w.configure(bg="#2E2E2E")                 # Establece el color de fondo.
    functions_w.iconbitmap("logos/logojulia.ico")       # Establece un ícono para la ventana.
    functions_w.resizable(0, 0)                         # Evita que la ventana cambie de tamaño.

    custom_header_font = load_font("font/Righteous-Regular.ttf", 21)        # Carga una fuente personalizada para el encabezado.

    if custom_header_font:                                                                          # Si se carga la fuente correctamente:
        header_text_image = create_text_image("Funciones disponibles", custom_header_font)          # Crea la imagen con el texto.
        header_photo = ImageTk.PhotoImage(header_text_image)                                        # Convierte la imagen en un objeto PhotoImage.

        header_label = Label(functions_w, image=header_photo, bg="#7289DA")         # Crea una etiqueta con la imagen del encabezado.
        header_label.image = header_photo                                           # Almacena la referencia a la imagen (para que no se elimine).
        header_label.pack(fill=X, pady=5)                                           # Coloca la etiqueta en la ventana.

    canvas = Canvas(functions_w, bg="#2E2E2E")                                          # Crea un lienzo (canvas) para contener el contenido desplazable.
    scrollbar = Scrollbar(functions_w, orient="vertical", command=canvas.yview)         # Crea una barra de desplazamiento vertical.
    scrollable_frame = Frame(canvas, bg="#2E2E2E")                                      # Crea un marco desplazable para los elementos.

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))         # Configura el área de desplazamiento.
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")          # Coloca el marco desplazable dentro del canvas.
    canvas.configure(yscrollcommand=scrollbar.set)          # Sincroniza la barra de desplazamiento con el canvas.
    canvas.pack(side=LEFT, fill=BOTH, expand=True)          # Coloca el canvas en la ventana.
    scrollbar.pack(side=RIGHT, fill=Y)          # Coloca la barra de desplazamiento a la derecha.

    font_path = "font/Righteous-Regular.ttf"        # Ruta de la fuente personalizada.
    font_size = 14          # Tamaño de la fuente.
    custom_font = load_font(font_path, font_size)       # Carga la fuente personalizada.

    functions_list = [          # Lista de funciones disponibles con sus respectivos iconos.
        ("Reproducir canción", 'icons/1.png'),
        ("Captura de pantalla", 'icons/2.png'),
        ("Consultar información en Wikipedia", 'icons/3.png'),
        ("Abrir programas", 'icons/4.png'),
        ("Buscar en Google", 'icons/5.png'),
        ("Buscar en Google Maps", 'icons/6.png'),
        ("Operaciones matemáticas", 'icons/7.png'),
        ("Consultar clima", 'icons/8.png'),
        ("Reproducir en Spotify", 'icons/9.png'),
        ("Agendar evento", 'icons/10.png'),
        ("Enviar correo", 'icons/11.png'),
        ("Traducir texto", 'icons/12.png')
    ]

    for func_name, icon_path in functions_list:             # Itera sobre la lista de funciones para crear los elementos visuales.
        frame_func = Frame(scrollable_frame, bg="#2E2E2E")  # Crea un marco para cada función.
        frame_func.pack(fill=X, pady=5)                     # Coloca el marco en el frame desplazable.

        try:
            func_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((30, 30)))                              # Carga y redimensiona el icono.
            label_icon = Label(frame_func, image=func_icon, bg="#2E2E2E")                                       # Crea una etiqueta con el icono.
            label_icon.image = func_icon                                                                        # Almacena la referencia al icono.
            label_icon.pack(side=LEFT, padx=5)                                                                  # Coloca la etiqueta con el icono en el marco de la función.
        except Exception as e:                                                                                  # Si hay un error al cargar el icono:
            messagebox.showwarning("Advertencia", f"No se encontró la imagen: {icon_path}. Error: {str(e)}")    # Muestra un aviso.

        func_image = create_function_image(func_name, custom_font)      # Crea una imagen con el nombre de la función.
        func_photo = ImageTk.PhotoImage(func_image)                     # Convierte la imagen de la función en un objeto PhotoImage.
        label_func = Label(frame_func, image=func_photo, bg="#2E2E2E")  # Crea una etiqueta con la imagen de la función.
        label_func.image = func_photo                                   # Almacena la referencia a la imagen de la función.
        label_func.pack(side=LEFT, padx=5)                              # Coloca la etiqueta con la imagen de la función en el marco.
####################################################################################################################################################################################

### Solicitar nombre de Usuario ###############################################################################

user_name = ""          # Variable global para almacenar el nombre del usuario.
name_file = 'user_name.txt'         # Nombre del archivo donde se guarda el nombre del usuario.

def load_user_name():       # Función para cargar el nombre del usuario desde un archivo.
    global user_name        # Declara que se va a usar la variable global user_name.
    if os.path.exists(name_file):       # Verifica si el archivo existe.
        with open(name_file, 'r') as file:          # Abre el archivo en modo lectura.
            user_name = file.read().strip()         # Lee el contenido del archivo y elimina espacios en blanco.
            talk(f"Bienvenido de nuevo, {user_name}. Soy Yulia, tu asistente virtual.")         # Saluda al usuario.
    else:               # Si el archivo no existe:
        ask_name()                  # Llama a la función para preguntar el nombre del usuario.

def ask_name():         # Función para pedir el nombre del usuario.
    global user_name        # Declara que se va a usar la variable global user_name.
    talk("Hola, ¿cuál es tu nombre?")       # Pide al usuario que diga su nombre.
    with sr.Microphone() as source:         # Usa el micrófono como fuente de audio.
        talk("Escuchando tu nombre...")         # Indica que está listo para escuchar.
        voice = listener.listen(source)         # Escucha el audio del micrófono.
        try:
            user_name = listener.recognize_google(voice, language='es-ES')          # Intenta reconocer el nombre usando Google Speech Recognition en español.
            talk(f"Bienvenido {user_name}, soy Yulia, tu asistente virtual.")       # Saluda al usuario con su nombre.
            with open(name_file, 'w') as file:          # Abre el archivo en modo escritura.
                file.write(user_name)       # Guarda el nombre del usuario en el archivo.
        except Exception as e:          # Si ocurre un error durante el reconocimiento:
            print(f"Error: {e}")        # Imprime el error en la consola.
            talk("Lo siento, no pude entender tu nombre. Intenta de nuevo.")        # Informa al usuario sobre el error.
            ask_name()          # Llama a la función para preguntar el nombre nuevamente.
####################################################################################################################################################################################

#### Conversacion y Carga de datos/Entrenamiento ##############################################################

def load_data():        # Función para cargar preguntas y respuestas desde la base de datos.
    conn = sqlite3.connect('brain.db')          # Conecta a la base de datos brain.db.
    cursor = conn.cursor()          # Crea un cursor para ejecutar comandos SQL.
    cursor.execute("SELECT question, answer FROM question_answers")         # Ejecuta una consulta para obtener preguntas y respuestas.
    data = cursor.fetchall()        # Obtiene todos los resultados de la consulta.
    conn.close()        # Cierra la conexión a la base de datos.
    questions = [row[0] for row in data]        # Extrae las preguntas de los resultados.
    answers = [row[1] for row in data]          # Extrae las respuestas de los resultados.
    return questions, answers       # Devuelve las listas de preguntas y respuestas.

def train_model(questions, answers):        # Función para entrenar el modelo con preguntas y respuestas.
    model = make_pipeline(CountVectorizer(), MultinomialNB())       # Crea un pipeline con un vectorizador y un clasificador Naive Bayes.
    model.fit(questions, answers)       # Entrena el modelo con las preguntas y respuestas.
    return model        # Devuelve el modelo entrenado.

def start_conversation():       # Función para iniciar la conversación con el usuario.
    questions, answers = load_data()        # Carga las preguntas y respuestas de la base de datos.
    model = train_model(questions, answers)         # Entrena el modelo con las preguntas y respuestas.
    talk("¡Perfecto! Vamos a conversar. Di, 'adiós' para salir de la conversación.")         # Informa al usuario que puede comenzar a hablar.
    
    while True:         # Bucle para mantener la conversación.
        user_input = listen_conversation()          # Escucha la entrada del usuario.
        if user_input is None:          # Verificar si user_input es None (indica un error en la escucha).
            continue        # Si hubo un error, continúa escuchando.
        
        if user_input.lower() == 'adiós':       # Si el usuario dice 'adiós':
            talk("¡Hasta luego!")       # Responde con un mensaje de despedida.
            write_func("Has salido del modo de conversación.")          # Muestra un mensaje en el canvas.
            break       # Sal del bucle de conversación.
        
        prediction = model.predict([user_input])[0]         # Predice la respuesta usando el modelo entrenado.
        talk(prediction)        # Habla la respuesta predicha.
        write_func('Respuesta: ' + prediction)          # Muestra la respuesta en el canvas.

def listen_conversation():          # Función para escuchar la entrada del usuario.
    try:
        with sr.Microphone() as source:         # Usa el micrófono como fuente de audio.
            voice = listener.listen(source)         # Escucha la entrada de voz.
            rec = listener.recognize_google(voice, language='es-ES')        # Reconoce el audio usando Google Speech Recognition en español.
            rec = rec.lower()       # Convierte la transcripción a minúsculas.
            return rec          # Devuelve la transcripción reconocida.
    except Exception as e:          # Si ocurre un error al escuchar o reconocer:
        print(f"Error: {e}")        # Imprime el error en la consola.
        talk('Lo siento, no puedo responder esa pregunta.')         # Informa al usuario sobre el error.
        return None         # Retorna None en caso de error.
####################################################################################################################################################################################

### Cerrar Ventana ############################################################################################

def close_app():
    main_w.destroy()
    os._exit(0)

main_w.protocol("WM_DELETE_WINDOW", close_app)
####################################################################################################################################################################################

#### Motor Voz ################################################################################################

name = 'julia'          # Asigna el valor de 'julia' a la variable name
listener = sr.Recognizer()          # Crea un objeto Recognizer de la biblioteca SpeechRecognition para procesar audio.
engine = pyttsx3.init()         # Inicializa el motor de texto a voz (TTS) usando la biblioteca pyttsx3.
voices = engine.getProperty('voices')       # Obtiene una lista de las voces disponibles en el motor TTS.
engine.setProperty('voice', voices[0].id)       # Establece la primera voz de la lista como la voz activa del motor.
engine.setProperty('rate', 150)         # Ajusta la velocidad de la voz a 150 palabras por minuto.
engine.setProperty('volume', 0.9)       # Establece el volumen del motor TTS al 90% (0.9).
####################################################################################################################################################################################

### Escuchador ################################################################################################

def listen():       # Función para escuchar y procesar la entrada de voz del usuario.
    try:
        with sr.Microphone() as source:         # Usa el micrófono como fuente de audio.
            talk('Escuchando... ')          # Indica al usuario que está escuchando.
            voice = listener.listen(source)         # Escucha la entrada de voz.
            rec = listener.recognize_google(voice, language='es-ES')        # Reconoce la voz usando Google Speech Recognition en español.
            rec = rec.lower()       # Convierte la transcripción a minúsculas.
            
            if name in rec:         # Verifica si el nombre ('julia', 'yulia', 'iulia') está en la transcripción.
                rec = rec.replace(name, '')         # Elimina el nombre de la transcripción para procesar solo el comando.
                run_assistant(rec)          # Llama a la función run_assistant con el comando procesado.
            else:       # Si el nombre no se reconoce en la transcripción:
                talk('Vuelve a intentarlo, no reconozco: ' + rec)       # Informa al usuario que no reconoció el comando.
    except Exception as e:          # Si ocurre un error al escuchar o reconocer:
        print(f"Error: {e}")        # Imprime el error en la consola.
        talk('Hubo un error, por favor intenta de nuevo.')          # Informa al usuario sobre el error.
####################################################################################################################################################################################

### Hilo ######################################################################################################

def listen_in_thread():         # Función para iniciar la escucha en un hilo separado.
    thread = threading.Thread(target=listen)        # Crea un nuevo hilo que ejecutará la función listen.
    thread.start()          # Inicia el hilo, permitiendo que la función listen se ejecute en paralelo.
####################################################################################################################################################################################

### Hablador ##################################################################################################

def talk(text):         # Función para convertir texto a voz.
    engine.say(text)        # Añade el texto a la cola de habla del motor TTS.
    engine.runAndWait()         # Espera a que se complete la reproducción del habla.

def speaker():          # Función para hablar el contenido de un área de texto.
    info_qs = info_answr.get("0.5", "end")          # Obtiene el texto del widget info_answr desde la posición 0.5 hasta el final.
    talk(info_qs)       # Llama a la función talk para reproducir el texto obtenido.

def write_func(text_functions):         # Función para insertar texto en un área de texto.
    info_answr.insert(INSERT, text_functions + "\n")        # Inserta el texto en el widget info_answr y añade un salto de línea.
####################################################################################################################################################################################

### Traductor #################################################################################################

def translate_text(text, dest_language="en"):       # Función para traducir texto a un idioma destino.
    try:
        translated = GoogleTranslator(source='auto', target=dest_language).translate(text)          # Utiliza GoogleTranslator para traducir el texto
        return translated       # Devuelve el texto traducido.
    except Exception as e:          # Maneja cualquier excepción que pueda ocurrir durante la traducción.
        return f"Error en la traducción: {e}"       # Devuelve un mensaje de error si algo falla.
####################################################################################################################################################################################

### Abrir programas ###########################################################################################

def open_program_by_shortcut(nombre_programa):          # Función para abrir un programa mediante un atajo de teclado.
    try:
        keyboard.press_and_release('win')       # Presiona y suelta la tecla de Windows para abrir el menú de inicio.
        time.sleep(0.1)         # Espera 0.1 segundos para asegurarse de que el menú se haya abierto.
        pyautogui.write(nombre_programa, interval=0.1)          # Escribe el nombre del programa en el menú de inicio.
        time.sleep(0.1)         # Espera 0.1 segundos para que el texto se ingrese correctamente.
        pyautogui.press('enter')        # Presiona la tecla Enter para abrir el programa.
        print(f"Abriendo {nombre_programa}...")         # Imprime un mensaje en la consola indicando que se está abriendo el programa.
    except Exception as e:          # Captura cualquier excepción que pueda ocurrir durante el proceso.
        print(f"Error al intentar abrir {nombre_programa}: {e}")        # Imprime un mensaje de error si algo falla.
####################################################################################################################################################################################

### Clima #####################################################################################################

API_KEY = "9ad6f112d1bc4349bbd21303240910"          # Clave de API para autenticar las solicitudes a la API del clima.
BASE_URL = "http://api.weatherapi.com/v1/current.json?"         # URL base de la API para obtener el clima actual.

def obtener_clima(ciudad):          # Función para obtener el clima de una ciudad específica.
    try:
        url_completa = f"{BASE_URL}key={API_KEY}&q={ciudad}&lang=es"        # Construye la URL completa para la solicitud, incluyendo la clave API y el nombre de la ciudad.
        response = requests.get(url_completa)       # Realiza una solicitud GET a la API del clima.
        data = response.json()          # Convierte la respuesta en formato JSON a un diccionario de Python.
        
        if "error" not in data:         # Verifica si hay algún error en la respuesta de la API.
            temp_celsius = data['current']['temp_c']        # Obtiene la temperatura en grados Celsius.
            condition = data['current']['condition']['text']        # Obtiene la condición climática (por ejemplo, "soleado").
            clima_texto = f"El clima en {ciudad} es de {temp_celsius} grados Celsius con {condition}."      # Crea un mensaje de texto sobre el clima actual en la ciudad especificada.
            talk(clima_texto)       # Llama a la función talk para reproducir el mensaje en voz alta.
            write_func(clima_texto)         # Llama a write_func para mostrar el mensaje en la interfaz.
        else:
            talk(f"No se encontró información sobre el clima para {ciudad}.")       # Mensaje en voz si no hay datos del clima.
            write_func(f"No se encontró información para {ciudad}.")        # Mensaje en la interfaz si no hay datos.
    except Exception as e:          # Captura cualquier excepción que pueda ocurrir durante el proceso.
        talk(f"Lo siento, hubo un problema al obtener el clima. {e}")       # Mensaje de error en voz.
        write_func(f"Error: {e}")       # Mensaje de error en la interfaz.
####################################################################################################################################################################################

### Calendario ################################################################################################
SCOPES = ['https://www.googleapis.com/auth/calendar']       # Alcance de permisos para acceder al calendario de Google.

def google_calendar_auth():         # Función para autenticar el acceso a Google Calendar.
    creds = None            # Inicializa las credenciales como None.
    if os.path.exists('tokens/token_c.json'):
        try:
            creds = Credentials.from_authorized_user_file('tokens/token_c.json', SCOPES)
        except Exception as e:
            print(f"Error cargando el token: {e}. Se eliminará el token para generar uno nuevo.")
            os.remove('tokens/token_c.json')
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())                                             # Intenta refrescar el token
            except Exception as e:
                print(f"Error refrescando el token: {e}. El token será eliminado.")
                talk(f"Error refrescando el token: {e}. El token será eliminado.")
                os.remove('tokens/token_c.json')                                     # Elimina el token si no se puede refrescar
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file('credentials/credentials_calendar.json', SCOPES)  # Si no se puede refrescar, inicia el flujo de autenticación desde cero
                creds = flow.run_local_server(port=0)
                with open('tokens/token_c.json', 'w') as token:                 # Guarda las nuevas credenciales
                    token.write(creds.to_json())
            except Exception as e:
                print(f"Error en la autenticación: {e}")
                talk(f"Error en la autenticación: {e}")
                return None

    return build('calendar', 'v3', credentials=creds)       # Devuelve el servicio de Google Calendar autenticado.
       # Devuelve el servicio de Google Calendar autenticado.

def create_event(summary, location, description, start_time, end_time):  # Función para crear un evento en Google Calendar.
    service = google_calendar_auth()  # Autenticación para acceder al calendario.
    
    event = {       # Define los detalles del evento a crear.
        'summary': summary,         # Título del evento.
        'location': location,       # Ubicación del evento.
        'description': description,         # Descripción del evento.
        'start': {          # Detalles de inicio del evento.
            'dateTime': start_time,         # Fecha y hora de inicio.
            'timeZone': 'America/Los_Angeles',          # Zona horaria.
        },
        'end': {                # Detalles de fin del evento.
            'dateTime': end_time,       # Fecha y hora de fin.
            'timeZone': 'America/Los_Angeles',          # Zona horaria.
        },
        'reminders': {          # Recordatorios para el evento.
            'useDefault': False,        # Desactiva los recordatorios predeterminados.
            'overrides': [          # Personaliza los recordatorios.
                {'method': 'email', 'minutes': 24 * 60},        # Recordatorio por correo electrónico un día antes.
                {'method': 'popup', 'minutes': 10},         # Recordatorio emergente 10 minutos antes.
            ],
        },
    }
    
    event = service.events().insert(calendarId='primary', body=event).execute()         # Inserta el evento en el calendario y ejecuta la solicitud.
    print(f"Evento creado: {event.get('htmlLink')}")        # Imprime el enlace del evento creado.
    talk('Evento agendado con éxito')       # Comunica al usuario que el evento ha sido creado.

def get_event_detail(detail):       # Función para obtener detalles de un evento (como título o descripción).
    talk(f"Dime {detail} del evento.")          # Pide al usuario que proporcione el detalle del evento.
    time.sleep(0)       # Pausa para permitir que el asistente escuche.
    
    with sr.Microphone() as source:         # Utiliza el micrófono para escuchar al usuario.
        listener.adjust_for_ambient_noise(source)       # Ajusta el micrófono para el ruido ambiental.
        print(f"Escuchando {detail}...")        # Imprime en consola lo que se está escuchando.
        talk(f"Escuchando {detail}...")         # Informa al usuario que está escuchando.
        
        voice = listener.listen(source, timeout=10, phrase_time_limit=10)       # Escucha la entrada del usuario con un tiempo de espera y límite de frase.
        try:
            rec = listener.recognize_google(voice, language='es-ES')        # Reconoce el habla del usuario.
            print(f"{detail.capitalize()} capturado: {rec}")        # Imprime el detalle capturado.
            return rec          # Devuelve el detalle capturado.
        except sr.UnknownValueError:        # Captura errores si no se entiende la entrada.
            print(f"No se pudo entender {detail}.")         # Mensaje en consola.
            talk(f"No pude entender {detail}. Intenta de nuevo.")       # Comunica al usuario que hubo un error.
            return get_event_detail(detail)         # Reintenta obtener el detalle.
        except sr.RequestError as e:        # Captura errores de comunicación con el servicio.
            print(f"Error al comunicarse con el servicio de reconocimiento de voz: {e}")        # Mensaje en consola.
            talk(f"Hubo un problema al conectar con el servicio. Intenta más tarde.")       # Informa al usuario.
            return ""       # Devuelve una cadena vacía en caso de error.

def get_event_date_time(detail):        # Función para obtener la fecha y hora de un evento.
    talk(f"Dime la fecha y hora de {detail} (por ejemplo, 15 de octubre de 2024 a las 10 am).")         # Pide al usuario la fecha y hora.
    time.sleep(0)       # Pausa para escuchar al usuario.
    
    with sr.Microphone() as source:         # Utiliza el micrófono para escuchar al usuario.
        listener.adjust_for_ambient_noise(source)       # Ajusta el micrófono para el ruido ambiental.
        print(f"Escuchando la fecha y hora de {detail}...")         # Imprime en consola lo que se está escuchando.
        talk(f"Escuchando la fecha y hora de {detail}...")          # Informa al usuario que está escuchando.
        
        voice = listener.listen(source, timeout=10, phrase_time_limit=10)       # Escucha la entrada del usuario.
        try:
            datetime_str = listener.recognize_google(voice, language='es-ES')               # Reconoce la entrada como fecha y hora.
            print(f"Fecha y hora de {detail} capturada: {datetime_str}")                # Imprime la fecha y hora capturada.
        except sr.UnknownValueError:                # Captura errores si no se entiende la entrada.
            print(f"No se pudo entender la fecha y hora de {detail}.")                  # Mensaje en consola.
            talk(f"No pude entender la fecha y hora de {detail}. Intenta de nuevo.")        # Informa al usuario.
            return get_event_date_time(detail)                  # Reintenta obtener la fecha y hora.
        except sr.RequestError as e:                # Captura errores de comunicación con el servicio.
            print(f"Error al comunicarse con el servicio de reconocimiento de voz: {e}")                # Mensaje en consola.
            talk(f"Hubo un problema al conectar con el servicio. Intenta más tarde.")               # Informa al usuario.
            return ""               # Devuelve una cadena vacía en caso de error.

    date_time = dateparser.parse(datetime_str, languages=['es'])        # Utiliza dateparser para interpretar la cadena de fecha y hora proporcionada por el usuario.
    if date_time is None:       # Verifica si la fecha y hora no pudieron ser interpretadas.
        print(f"No se pudo interpretar la fecha y hora: {datetime_str}")        # Mensaje en consola.
        talk(f"No pude interpretar la fecha y hora. Intenta de nuevo.")         # Informa al usuario.
        return get_event_date_time(detail)          # Reintenta obtener la fecha y hora.
    else:
        date_time_formatted = date_time.isoformat()         # Formatea la fecha y hora en formato ISO.
        print(f"Fecha y hora de {detail} interpretada: {date_time_formatted}")          # Imprime la fecha y hora interpretadas.
        return date_time_formatted          # Devuelve la fecha y hora formateadas.
####################################################################################################################################################################################

### Spotify ###################################################################################################

SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'      # Credenciales de autenticación para la API de Spotify.
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,         # Inicializa el cliente de Spotify con las credenciales y los permisos necesarios.
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state user-modify-playback-state playlist-modify-private playlist-modify-public user-library-read"))

def reproducir_cancion(cancion):        # Función para reproducir una canción específica o las canciones guardadas.
    try:
        if not cancion.strip():         # Si no se proporciona una canción específica.
            liked_songs = sp.current_user_saved_tracks(limit=10)        # Obtiene las 10 canciones guardadas del usuario.
            if liked_songs['items']:        # Verifica si hay canciones guardadas.
                uris = [item['track']['uri'] for item in liked_songs['items']]          # Extrae las URIs de las canciones.
                sp.start_playback(uris=uris)        # Comienza la reproducción de las canciones guardadas.
                talk("Reproduciendo tus canciones que te gustan en Spotify.")       # Mensaje al usuario.
            else:
                talk("No tienes canciones guardadas en 'Tus me gusta'.")        # Mensaje si no hay canciones.
        else:
            resultados = sp.search(q=cancion, type='track', limit=1)        # Busca la canción proporcionada.
            if resultados['tracks']['items']:       # Verifica si se encontró la canción.
                track_uri = resultados['tracks']['items'][0]['uri']         # Obtiene la URI de la canción encontrada.
                sp.start_playback(uris=[track_uri])         # Comienza la reproducción de la canción.
                talk(f"Reproduciendo {cancion} en Spotify.")        # Mensaje al usuario.
            else:
                talk(f"No encontré {cancion} en Spotify.")          # Mensaje si no se encuentra la canción.
    except Exception as e:          # Maneja errores.
        print(f"Error al reproducir canción: {e}")          # Imprime el error en consola.
        talk("Hubo un problema al reproducir la música en Spotify.")        # Mensaje al usuario sobre el error.

def pausar_cancion():       # Función para pausar la música actual.
    try:
        sp.pause_playback()         # Pausa la reproducción.
        talk("Música pausada.")         # Mensaje al usuario.
    except Exception as e:          # Maneja errores.
        print(f"Error al pausar la música: {e}")        # Imprime el error en consola.

def saltar_cancion():       # Función para saltar a la siguiente canción.
    try:
        sp.next_track()         # Salta a la siguiente canción.
        talk("Saltando a la siguiente canción.")        # Mensaje al usuario.
    except Exception as e:          # Maneja errores.
        print(f"Error al saltar la canción: {e}")       # Imprime el error en consola.

def reproducir_cancion_anterior():          # Función para reproducir la canción anterior.
    try:
        sp.previous_track()         # Reproduce la canción anterior.
        talk("Reproduciendo la canción anterior.")          # Mensaje al usuario.
    except Exception as e:          # Maneja errores.
        print(f"Error al reproducir la canción anterior: {e}")          # Imprime el error en consola.

def ver_cancion_actual():       # Función para ver la canción que se está reproduciendo actualmente.
    try:
        current_track = sp.current_playback()       # Obtiene la canción actual que se está reproduciendo.
        if current_track is not None and current_track['is_playing']:       # Verifica si hay una canción reproduciéndose.
            track_name = current_track['item']['name']          # Obtiene el nombre de la canción.
            artist_name = current_track['item']['artists'][0]['name']       # Obtiene el nombre del artista.
            talk(f"Actualmente reproduciendo: {track_name} de {artist_name}.")          # Mensaje al usuario.
        else:
            talk("No hay música reproduciéndose en este momento.")          # Mensaje si no hay música.
    except Exception as e:          # Maneja errores.
        print(f"Error al obtener la canción actual: {e}")       # Imprime el error en consola.

def crear_lista_reproduccion(nombre_lista):         # Función para crear una nueva lista de reproducción.
    try:
        user_id = sp.current_user()['id']       # Obtiene el ID del usuario.
        sp.user_playlist_create(user_id, nombre_lista, public=True)         # Crea la lista de reproducción.
        talk(f"Lista de reproducción '{nombre_lista}' creada.")         # Mensaje al usuario.
    except Exception as e:  # Maneja errores.
        print(f"Error al crear la lista de reproducción: {e}")          # Imprime el error en consola.

def agregar_canciones_a_lista(nombre_lista, canciones=None):        # Función para agregar canciones a una lista de reproducción.
    try:
        user_id = sp.current_user()['id']       # Obtiene el ID del usuario.
        playlists = sp.user_playlists(user_id)          # Obtiene las listas de reproducción del usuario.
        playlist_id = None          # Inicializa el ID de la lista de reproducción.
        
        for playlist in playlists['items']:         # Busca la lista de reproducción por su nombre.
            if playlist['name'].lower() == nombre_lista.lower():
                playlist_id = playlist['id']        # Guarda el ID de la lista encontrada.
                break
        
        if playlist_id is not None:         # Verifica si se encontró la lista de reproducción.
            track_uris = []         # Inicializa una lista para las URIs de las canciones.
            if canciones is None:       # Si no se proporcionan canciones.
                current_track = sp.current_playback()       # Obtiene la canción actual.
                if current_track and current_track['is_playing']:       # Verifica si hay una canción reproduciéndose.
                    track_uris.append(current_track['item']['uri'])         # Agrega la URI de la canción actual.
                    talk(f"Agregando la canción en reproducción: {current_track['item']['name']} de {current_track['item']['artists'][0]['name']} a la lista {nombre_lista}.")          # Mensaje al usuario.
                else:
                    talk("No se está reproduciendo ninguna canción. Por favor, proporciona el nombre de una canción.")          # Mensaje si no hay música.
                    return
            else:
                for cancion in canciones:       # Busca cada canción proporcionada y agrega sus URIs a la lista.
                    resultados = sp.search(q=cancion, type='track', limit=1)        # Busca la canción.
                    if resultados['tracks']['items']:       # Verifica si se encontró la canción.
                        track_uris.append(resultados['tracks']['items'][0]['uri'])          # Agrega la URI de la canción encontrada.
                    else:
                        talk(f"No encontré la canción {cancion}.")          # Mensaje si no se encuentra la canción.
        
            if track_uris:          # Agrega las canciones a la lista de reproducción.
                sp.user_playlist_add_tracks(user_id, playlist_id, track_uris)       # Agrega las URIs de las canciones a la lista.
                talk(f"Canciones agregadas a la lista de reproducción '{nombre_lista}'.")       # Mensaje al usuario.
            else:
                talk("No se encontraron canciones para agregar.")       # Mensaje si no hay canciones para agregar.
        else:
            talk(f"No se encontró la lista de reproducción '{nombre_lista}'.")          # Mensaje si no se encuentra la lista.
    except Exception as e:          # Maneja errores.
        print(f"Error al agregar canciones a la lista de reproducción: {e}")        # Imprime el error en consola.
        talk("Hubo un problema al agregar las canciones.")          # Mensaje al usuario sobre el error.

def reproducir_lista_reproduccion(nombre_lista):        # Función para reproducir una lista de reproducción.
    try:
        user_id = sp.current_user()['id']       # Obtiene el ID del usuario.
        playlists = sp.user_playlists(user_id)          # Obtiene las listas de reproducción del usuario.
        playlist_id = None          # Inicializa el ID de la lista de reproducción.
        
        for playlist in playlists['items']:         # Busca la lista de reproducción por su nombre.
            if playlist['name'].lower() == nombre_lista.lower():
                playlist_id = playlist['id']        # Guarda el ID de la lista encontrada.
                break
            
        if playlist_id is not None:         # Verifica si se encontró la lista de reproducción.
            sp.start_playback(context_uri=playlist_id)          # Comienza la reproducción de la lista.
            talk(f"Reproduciendo la lista de reproducción '{nombre_lista}'.")       # Mensaje al usuario.
        else:
            talk(f"No se encontró la lista de reproducción '{nombre_lista}'.")          # Mensaje si no se encuentra la lista.
    except Exception as e:          # Maneja errores.
        print(f"Error al reproducir la lista de reproducción: {e}")         # Imprime el error en consola.

def detener_reproduccion():         # Función para detener la música.
    try:
        sp.pause_playback()         # Pausa la reproducción.
        talk("Deteniendo la música.")       # Mensaje al usuario.
    except Exception as e:          # Maneja errores.
        print(f"Error al detener la música: {e}")       # Imprime el error en consola.

def reanudar_cancion():         # Función para reanudar la música pausada.
    try:
        sp.start_playback()         # Reinicia la reproducción.
        talk("Reanudando la música.")       # Mensaje al usuario.
    except Exception as e:          # Maneja errores.
        print(f"Error al reanudar la música: {e}")          # Imprime el error en consola.
        talk("Hubo un problema al reanudar la música.")         # Mensaje al usuario sobre el error.

def mostrar_listas_reproduccion():          # Función para mostrar las listas de reproducción del usuario.
    try:
        user_id = sp.current_user()['id']       # Obtiene el ID del usuario.
        playlists = sp.user_playlists(user_id, limit=50)        # Obtiene las listas de reproducción del usuario (máx. 50).
        info_answr.delete("1.0", END)       # Borra el área de respuesta anterior.
        all_playlists = playlists['items']          # Inicializa la lista de todas las listas de reproducción.
        
        while playlists['next']:        # Obtiene más listas si hay más de 50.
            playlists = sp.next(playlists)
            all_playlists.extend(playlists['items'])        # Agrega las nuevas listas a la lista total.
        
        if all_playlists:       # Verifica si hay listas de reproducción.
            for playlist in all_playlists:          # Itera sobre las listas.
                info_answr.insert(INSERT, f"Lista: {playlist['name']} - ID: {playlist['id']}\n")        # Muestra cada lista.
            talk("He mostrado tus listas de reproducción.")         # Mensaje al usuario.
        else:
            info_answr.insert(INSERT, "No se encontraron listas de reproducción.")          # Mensaje si no hay listas.
            talk("No encontré ninguna lista de reproducción.")          # Mensaje al usuario.
            
    except Exception as e:                                                      # Maneja errores.
        print(f"Error al obtener las listas de reproducción: {e}")              # Imprime el error en consola.
        talk("Hubo un problema al obtener las listas de reproducción.")         # Mensaje al usuario sobre el error.

####################################################################################################################################################################################

### Gmail #####################################################################################################

def procesar_texto(texto):
    texto = texto.lower()                                                                                       # Convierte el texto a minúsculas.
    texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))        # Normaliza el texto para eliminar acentos.
    return texto

def es_correo_valido(correo):                                                   # Función para validar el formato de un correo electrónico.
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'                # Expresión regular para validar el correo.
    return re.match(patron, correo)                                             # Devuelve True si coincide con el patrón.

def convertir_correo_hablado(correo_hablado):                                   # Función para convertir el texto hablado en un correo electrónico.
    correo_hablado = correo_hablado.replace(" arroba ", "@")                    # Reemplaza palabras habladas por sus símbolos correspondientes.
    correo_hablado = correo_hablado.replace(" punto ", ".")
    correo_hablado = correo_hablado.replace(" guión ", "-")
    correo_hablado = correo_hablado.replace(" guión bajo ", "_")
    correo_hablado = correo_hablado.lower()                                     # Convierte a minúsculas.
    correo_hablado = ''.join((c for c in unicodedata.normalize('NFD', correo_hablado) if unicodedata.category(c) != 'Mn'))          # Normaliza el texto para eliminar acentos.
    correo_hablado = correo_hablado.strip()                                             # Elimina espacios en blanco al inicio y al final.
    correo_hablado = re.sub(r'\s+', '', correo_hablado)                                 # Elimina espacios múltiples.
    return correo_hablado

SCOPES_GMAIL = ['https://www.googleapis.com/auth/gmail.send']                               # Alcance para enviar correos.

def gmail_authenticate():                                                                   # Función para autenticar y obtener credenciales para acceder a la API de Gmail.
    creds = None
    if os.path.exists('tokens/token_g.json'):
        try:
            creds = Credentials.from_authorized_user_file('tokens/token_g.json', SCOPES_GMAIL)
        except Exception as e:
            print(f"Error cargando el token: {e}. Se eliminará el token para generar uno nuevo.")
            os.remove('tokens/token_g.json')
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())                                             # Intenta refrescar el token
            except Exception as e:
                print(f"Error refrescando el token: {e}. El token será eliminado.")
                talk(f"Error refrescando el token: {e}. El token será eliminado.")
                os.remove('tokens/token_g.json')                                     # Elimina el token si no se puede refrescar
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file('credentials/credentials_gmail.json', SCOPES_GMAIL)  # Si no se puede refrescar, inicia el flujo de autenticación desde cero
                creds = flow.run_local_server(port=0)
                with open('tokens/token_g.json', 'w') as token:                 # Guarda las nuevas credenciales
                    token.write(creds.to_json())
            except Exception as e:
                print(f"Error en la autenticación: {e}")
                talk(f"Error en la autenticación: {e}")
                return None

    return creds                                                       # Devuelve las credenciales.

def create_message(sender, to, subject, message_text):                      # Función para crear un mensaje de correo.
    message = MIMEText(message_text)                                        # Crea el mensaje como texto plano.
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()         # Codifica el mensaje en base64.
    return {'raw': raw_message}                                                 # Devuelve el mensaje codificado.

def send_email(to, subject, body):                                                      # Función para enviar un correo electrónico.
    creds = gmail_authenticate()                                                        # Obtiene las credenciales.
    try:
        service = build('gmail', 'v1', credentials=creds)                                   # Construye el servicio de la API de Gmail.
        message = create_message('me', to, subject, body)                                   # Crea el mensaje.
        sent_message = service.users().messages().send(userId="me", body=message).execute()         # Envía el correo.
        talk("Correo enviado correctamente.")                                   # Mensaje al usuario.
        return sent_message                                                     # Devuelve el mensaje enviado.
    except Exception as e:
        print(f"Error: {e}")                                                    # Imprime el error en consola.
        talk("Hubo un error al enviar el correo. Intenta nuevamente.")          # Mensaje al usuario.

def enviar_correo(rec):                                                      # Función para iniciar el proceso de envío de un correo.
    talk('¿A quién le gustaría enviar el correo?')                              # Solicita el destinatario.
    with sr.Microphone() as source:
        voice = listener.listen(source)                                             # Escucha la respuesta.
        to_hablado = listener.recognize_google(voice, language='es-ES').strip()         # Reconoce el texto.
    to = convertir_correo_hablado(to_hablado)                                           # Convierte el texto hablado en correo.
    if not es_correo_valido(to):                                                        # Verifica si el correo es válido.
        talk("El correo electrónico proporcionado no es válido. Intenta nuevamente.")           # Mensaje de error.
        return
    talk('¿Cuál será el asunto del correo?')                                # Solicita el asunto del correo.
    with sr.Microphone() as source:
        voice = listener.listen(source)                                     # Escucha la respuesta.
        subject = listener.recognize_google(voice, language='es-ES').strip()        # Reconoce el texto.
    talk('¿Qué mensaje deseas enviar?')                                     # Solicita el mensaje del correo.
    with sr.Microphone() as source:
        voice = listener.listen(source)                                     # Escucha la respuesta.
        body = listener.recognize_google(voice, language='es-ES').strip()                       # Reconoce el texto.
    send_email(to, subject, body)                                               # Envía el correo.
####################################################################################################################################################################################

### Funciones #################################################################################################

def run_assistant(rec):
    if 'reproducir' in rec or 'pon' in rec:
        yt_reprod = rec.replace('reproducir', '').replace('pon', '')
        talk('Reproduciendo ' + yt_reprod)
        pywhatkit.playonyt(yt_reprod)  
        
    elif 'captura de pantalla' in rec or 'screenshot' in rec:
        scrn_sht = rec.replace('captura de pantalla', '').replace('screenshot', '')
        talk('Realizando captura' + scrn_sht)
        pywhatkit.take_screenshot(scrn_sht)
        
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
        
    elif 'consulta' in rec or 'sobre' in rec:
        orderwiki = rec.replace('consulta', '').replace('sobre', '')
        wikipedia.set_lang("es")
        infowiki = wikipedia.summary(orderwiki, 1, 2)
        talk(infowiki)
        write_func(orderwiki + ': ' + infowiki)
        
    elif 'abre' in rec:
        program = rec.replace('abre', '').strip()
        open_program_by_shortcut(program)

    elif 'busca' in rec:
        glg_search = rec.replace('busca', '')
        talk('Realizando búsqueda' + glg_search)
        pywhatkit.search(glg_search)
        
    elif 'mapa' in rec:
        location = rec.replace('mapa', '')
        talk('Buscando ' + location + ' en Google Maps')
        url = f"https://www.google.com/maps/search/{location}"
        webbrowser.open(url)
        
    elif 'cuánto' in rec:
        rec = rec.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        res = sm.getResult(rec)
        talk(res)
        write_func(rec + ': ' + res)
    
    elif 'clima en' in rec:
        ciudad = rec.replace('clima en', '').strip()
        if ciudad:
            obtener_clima(ciudad)
        else:
            talk("No entendí la ciudad, por favor intenta de nuevo.")
    
    elif 'reproduce en spotify' in rec:
        cancion = rec.replace('reproduce en spotify', '').strip()
        reproducir_cancion(cancion)

    elif 'reproduce la lista de reproducción' in rec:
        nombre_lista = rec.replace('reproduce la lista de reproducción', '').strip()
        reproducir_lista_reproduccion(nombre_lista)

    elif 'pausa la música' in rec:
        pausar_cancion()
        
    elif 'reanudar música' in rec:
        reanudar_cancion()

    elif 'saltar canción' in rec:
        saltar_cancion()

    elif 'reproducir canción anterior' in rec:
        reproducir_cancion_anterior()

    elif 'ver canción actual' in rec:
        ver_cancion_actual()

    elif 'crear lista de reproducción' in rec:
        nombre_lista = rec.replace('crear lista de reproducción', '').strip()
        crear_lista_reproduccion(nombre_lista)

    elif 'agregar canciones a la lista' in rec:
        partes = rec.replace('agregar canciones a la lista', '').strip().split('y')
        nombre_lista = partes[0].strip()
        canciones = [cancion.strip() for cancion in partes[1:]]
        agregar_canciones_a_lista(nombre_lista, canciones)

    elif 'detener la música' in rec:
        detener_reproduccion()
        
    elif 'agendar evento' in rec:
        summary = get_event_detail('título')
        if summary == "":
            return
        location = get_event_detail('ubicación')
        if location == "":
            return
        description = get_event_detail('descripción')
        if description == "":
            return
        start_time = get_event_date_time('inicio')
        if start_time == "":
            return
        end_time = get_event_date_time('fin')
        if end_time == "":
            return
        create_event(summary, location, description, start_time, end_time)
        
    elif 'enviar correo' in rec:
        enviar_correo(rec)
    
    elif 'traduce' in rec or 'traducir' in rec:
        if 'a inglés' in rec:
            dest_language = 'en'
        elif 'a francés' in rec:
            dest_language = 'fr'
        elif 'a alemán' in rec:
            dest_language = 'de'
        elif 'a japones' in rec:
            dest_language = 'jp'
        else:
            dest_language = 'en'
        text_to_translate = rec.replace('traduce', '').replace('traducir', '').replace('a inglés', '').replace('a francés', '').replace('a alemán', '').replace('a japones').strip()
        translated_text = translate_text(text_to_translate, dest_language=dest_language)
        talk(f"Traducción: {translated_text}")
        write_func('Traducción: ' + translated_text)
        
    elif 'conversar' in rec:
        start_conversation()
    
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return rec

load_user_name()
main_w.update()
####################################################################################################################################################################################

### Botones ###################################################################################################

def clear_canvas():                                     # Función para limpiar el área de texto de respuestas (asumiendo que 'info_answr' es un Text widget).
    info_answr.delete(1.0, END)                         # Elimina todo el texto desde la posición 1.0 hasta el final.

def create_button_image(text, font, image_size=(190, 40), bg_color=(114, 137, 218), text_color=(255, 255, 255)):            # Función para crear una imagen de botón con texto
    img = Image.new('RGB', image_size, color=bg_color)                                                                      # Crea una nueva imagen con el color de fondo especificado.
    draw = ImageDraw.Draw(img)                                                                                              # Crea un objeto de dibujo para la imagen.
    draw.text((10, 10), text, font=font, fill=text_color)                                                                   # Dibuja el texto en la imagen en la posición (10, 10).
    return img                                                                                                              # Devuelve la imagen creada.

button_font = load_font("font/Righteous-Regular.ttf", 16)                                # Carga la fuente personalizada para los botones.

img_functions = create_button_image("Funciones disponibles", button_font)               # Crea la imagen del botón "Funciones disponibles" usando la función anterior.
photo_functions = ImageTk.PhotoImage(img_functions)                                     # Convierte la imagen a un formato compatible con Tkinter.

button_functions = Button(main_w, image=photo_functions, command=show_functions_window, highlightthickness=0, bd=0, relief="flat", activebackground="#1C1C9C") #mostrar la ventana
button_functions.place(x=125, y=570)  # Coloca el botón en la posición (125, 570).

img_button_speak = PhotoImage(file='icons/speakerw.png')                # Crea un botón para hablar, cargando la imagen del ícono del altavoz.
button_speak = Button(main_w, image=img_button_speak, command=speaker, highlightthickness=0, bd=0, relief="flat", bg="#434343", activebackground="#434343")
button_speak.place(x=15, y=570)                                         # Coloca el botón en la posición (15, 570).

img_button_listen = PhotoImage(file='icons/microphonew.png')                # Crea un botón para escuchar, cargando la imagen del ícono del micrófono.
button_listen = Button(main_w, image=img_button_listen, command=listen_in_thread, highlightthickness=0, bd=0, relief="flat", bg="#434343", activebackground="#434343")
button_listen.place(x=415, y=570)                                           # Coloca el botón en la posición (415, 570).

img_button_clean = PhotoImage(file='icons/return.png')                      # Crea un botón para limpiar el área de texto, cargando la imagen del ícono de retorno.
button_clean = Button(main_w, image=img_button_clean, command=clear_canvas, highlightthickness=0, bd=0, relief="flat", bg="#434343", activebackground="#434343", activeforeground="#434343")
button_clean.place(x=370, y=570)                                            # Coloca el botón en la posición (370, 570).

####################################################################################################################################################################################

### Canvas ####################################################################################################

info_answr = Text(main_w, bg="#403A3E", fg="white",font=("Righteous", 12, "bold"))
info_answr.place(x=50,y=360, height=200, width=350)
####################################################################################################################################################################################

### Label #####################################################################################################

custom_font = load_font("font/Righteous-Regular.ttf", 21)               # Carga la fuente personalizada desde el directorio especificado con un tamaño de 21.
if custom_font:                                                         # Verifica si la fuente se cargó correctamente.
    text_image = create_text_image("Bienvenido, soy tu asistente virtual", custom_font)                 # Crea una imagen con el texto utilizando la fuente personalizada.
    photo = ImageTk.PhotoImage(text_image)                                                              # Convierte la imagen de texto en un formato compatible con Tkinter.
    header_label = Label(main_w, image=photo, bg="#7289DA")                                             # Crea una etiqueta en la ventana principal que contiene la imagen de texto.
    header_label.image = photo                                                      # Guarda una referencia a la imagen para evitar que sea recolectada por el recolector de basura.
    header_label.pack(fill=X, pady=20)                                              # Añade la etiqueta a la ventana, ocupando todo el ancho y añadiendo un espaciado vertical.
julia_logo = ImageTk.PhotoImage(Image.open('logos/logojulia_full.png'))             # Carga la imagen del logo de Julia desde el directorio especificado.
window_logo = Label(main_w, image=julia_logo, bg="#434343")                     # Crea una etiqueta en la ventana principal que contiene el logo.
window_logo.pack(pady=5)                                                    # Añade la etiqueta del logo a la ventana con un espaciado vertical.
####################################################################################################################################################################################

main_w.mainloop()
