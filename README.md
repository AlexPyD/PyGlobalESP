# Herramienta PYGlobal

La Herramienta PYGlobal es un programa en Python que te permite enviar mensajes a un webhook de Discord y obtener información a partir de un ID de usuario de Discord. Proporciona una interfaz de línea de comandos para interactuar con la herramienta.

## Características

- Envía mensajes a un webhook de Discord con una mención y una imagen opcional.
- Obtiene información sobre un usuario de Discord basada en su ID.

## Requisitos previos

- Python 3.x instalado en tu sistema.
- Paquetes requeridos: `colorama` y `requests`. El programa intentará instalarlos si no se encuentran.

## Instalación

1. Clona o descarga este repositorio en tu máquina local.

2. Instala los paquetes requeridos ejecutando el siguiente comando en tu terminal: `pip install -r requirements.txt`

## Uso

1. Abre una terminal y navega hasta el directorio del proyecto.

2. Ejecuta el programa utilizando el siguiente comando:


3. Elige una opción del menú:

- Opción 1: Enviar un mensaje a un webhook de Discord.
  - Ingresa la URL del webhook cuando se te solicite.
  - Proporciona tu nombre, mensaje y una URL de imagen opcional.
  - El programa enviará el mensaje como una incrustación al webhook.

- Opción 2: Obtener información a partir de un ID de usuario de Discord.
  - Ingresa el ID de usuario y la URL del webhook cuando se te solicite.
  - El programa recuperará información sobre el usuario, como su nombre de usuario, discriminador, fecha de creación y avatar.
  - La información se enviará como una incrustación al webhook.

4. Sigue las indicaciones en pantalla y proporciona la información requerida.

5. Verifica la salida en la terminal para conocer el resultado de la operación.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Reconocimientos

La Herramienta PYGlobal es desarrollada por Alex_ como parte del proyecto PYGlobal.
