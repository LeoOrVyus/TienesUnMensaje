import datetime
import subprocess

# Obtener la fecha actual en formato "mes-día"
fecha_actual = datetime.datetime.now().strftime("%m-%d")


if fecha_actual == "01-01" or fecha_actual == "07-01" or fecha_actual == "23-04":

    subprocess.call(["python", "mensual.exe"])
