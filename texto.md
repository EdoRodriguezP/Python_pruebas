

1. El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas tipografías además de usarse para rellenar espacios que requieran largos textos. ¿Cuántas palabras componen este texto?

Genere un archivo llamado word_count.py que importe un texto a Python y realice las siguientes tareas:
● Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres distintos que componen un texto
● Cuente el número de palabras distintas que componen el texto ingresado. Para separar un texto por espacios puede utilizar el método .split("").

TIP: Para importar texto en python puede adaptar el siguiente código:
with open(“texto.txt”, "r") as file:
texto=file.read() donde “texto.txt” corresponderá a la ruta del archivo a importar. Para comprobar el correcto funcionamiento del código se provee el archivo lorem_ipsum.txt. Al ejecutar el programa se espera el siguiente output.
python word_count.py lorem_ipsum.txt
Respuesta esperada:
El número de caracteres distintos es: 40
El número de palabras distintas es: 243

