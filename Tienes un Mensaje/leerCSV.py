import csv
import email
import os

# Define la ruta del archivo CSV
ruta_archivo = "/ruta/a/archivo.csv"

# Define una función para leer los correos electrónicos desde el archivo CSV
def leer_correos_desde_csv(ruta_archivo):
    with open(ruta_archivo, "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            # Cada fila representa un correo electrónico
            correo = email.message_from_string(fila[0])
            # Extrae los detalles del correo electrónico
            de = correo["From"]
            para = correo["To"]
            asunto = correo["Subject"]
            cuerpo = correo.get_payload()
            # Haz algo con los detalles del correo electrónico (por ejemplo, envíalos a otra dirección de correo electrónico)
            print("De:", de)
            print("Para:", para)
            print("Asunto:", asunto)
            print("Cuerpo:", cuerpo)
            print("")

# Ejecuta la función para leer los correos electrónicos desde el archivo CSV
leer_correos_desde_csv(ruta_archivo)
