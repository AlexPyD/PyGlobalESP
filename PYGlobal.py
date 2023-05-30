import time
import importlib
import requests
import json
from colorama import Fore, Style

def instalar_paquete(paquete):
    try:
        importlib.import_module(paquete)
        print(f"{paquete} ya está instalado.")
    except ImportError:
        try:
            import pip
            print(f"Instalando {paquete}...")
            pip.main(['install', paquete])
            print(f"{paquete} ha sido instalado correctamente.")
        except:
            print(f"No se pudo instalar {paquete}. Asegúrate de tener pip instalado.")

def mostrar_progreso_porcentaje(progreso):
    barra = "[" + Fore.GREEN + "|" * (progreso // 2) + " " * (50 - progreso // 2) + "]" + Style.RESET_ALL
    porcentaje = f"{progreso}%"
    print(f"\r{barra} {porcentaje}", end="")

def verificar_instalacion_paquetes(paquetes):
    total_paquetes = len(paquetes)
    paquetes_instalados = 0

    for paquete in paquetes:
        try:
            importlib.import_module(paquete)
            paquetes_instalados += 1
        except ImportError:
            instalar_paquete(paquete)

    if paquetes_instalados == total_paquetes:
        print(Fore.GREEN + "Todos los paquetes están instalados.")
    else:
        print(Fore.YELLOW + "Instalación de paquetes completa.")

def mostrar_carga_programa():
    print("Cargando pyglobal:")
    for i in range(11):
        time.sleep(1)
        mostrar_progreso_porcentaje(i * 10)
    print("\nActualizando Archivos Importantes!")
    time.sleep(5)
    print("Actualización completa.")

def mencionar_usuario(usuario_id):
    return f"<@{usuario_id}>"

def obtener_informacion_usuario(usuario_id):
    response = requests.get(f"https://discord.com/api/v9/users/{usuario_id}")
    if response.status_code == 200:
        data = response.json()
        username = data.get("username")
        discriminator = data.get("discriminator")
        created_at = data.get("created_at")
        avatar_id = data.get("avatar")
        avatar_url = f"https://cdn.discordapp.com/avatars/{usuario_id}/{avatar_id}.png" if avatar_id else None

        return username, discriminator, created_at, avatar_url

    return None

def enviar_embed(webhook, mensaje, nombre, imagen_url=None, mencion=None):
    embed = {
        "title": f"Mensaje por: {nombre}",
        "description": mensaje,
        "footer": {
            "text": "By Alex • PYGlobal"
        }
    }

    if imagen_url is not None and imagen_url.strip():
        embed["footer"]["icon_url"] = imagen_url.strip()

    payload = {
        "content": mensaje,
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print("Embed enviado con éxito.")
    else:
        print("Error al enviar el embed. Verifica el webhook e inténtalo de nuevo.")

# Verificar e instalar los paquetes necesarios
paquetes_necesarios = ["colorama", "requests"]

print("Verificando la instalación de paquetes...")
verificar_instalacion_paquetes(paquetes_necesarios)

# Mostrar la carga del programa
mostrar_carga_programa()

# Mostrar el menú de opciones
print("\n--- PYGlobal Tool ---")
print("[1] Enviar mensaje a un webhook")
print("[2] Obtener información de un ID de Discord")

opcion = input("Selecciona una opción: ")

if opcion == "1":
    print("\n--- Enviar mensaje a un webhook ---")
    webhook = input(Fore.YELLOW + "Webhook: ")
    nombre = input(Fore.YELLOW + "Tu Nombre: ")
    mensaje = input(Fore.YELLOW + "Mensaje: ")
    imagen_url = input(Fore.YELLOW + "URL de la imagen (opcional): ")

    # Verificar si se quiere mencionar a un usuario
    mencionar = input(Fore.YELLOW + "¿Quieres mencionar a algún usuario? (s/n): ")
    mencion = None
    if mencionar.lower() == "s":
        usuario_id = input(Fore.YELLOW + "ID de usuario a mencionar: ")
        mencion = mencionar_usuario(usuario_id)

    # Enviar el embed
    enviar_embed(webhook, mensaje, nombre, imagen_url, mencion)
elif opcion == "2":
    print("\n--- Obtener información de un ID de Discord ---")
    usuario_id = input(Fore.YELLOW + "ID a inspeccionar: ")
    webhook = input(Fore.YELLOW + "Webhook (para el embed): ")

    # Obtener información del usuario
    informacion_usuario = obtener_informacion_usuario(usuario_id)
    if informacion_usuario is not None:
        username, discriminator, created_at, avatar_url = informacion_usuario

        embed = {
            "title": f"Información de usuario",
            "fields": [
                {"name": "Usuario", "value": f"{username}#{discriminator}"},
                {"name": "ID", "value": usuario_id},
                {"name": "Fecha de creación", "value": created_at}
            ],
            "footer": {
                "text": "By Alex • PYGlobal"
            }
        }

        if avatar_url is not None:
            embed["thumbnail"] = {"url": avatar_url}

        payload = {
            "content": "",
            "embeds": [embed]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(webhook, data=json.dumps(payload), headers=headers)

        if response.status_code == 204:
            print("Embed enviado con éxito.")
        else:
            print("Error al enviar el embed. Verifica el webhook e inténtalo de nuevo.")
    else:
        print("No se pudo obtener la información del usuario.")
else:
    print("Opción inválida.")
