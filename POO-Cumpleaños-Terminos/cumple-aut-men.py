import datetime
import subprocess
import os
import pymysql.cursors

conexion = pymysql.connect(host='localhost',
                           user='root',
                           password='Grettel33',
                           db='empleados',
                           cursorclass=pymysql.cursors.DictCursor)

with conexion.cursor() as cursor:
    sql = "SELECT 'fecha de nacimiento', fecha_de_nacimiento FROM empleados"
    cursor.execute(sql)
    resultados = cursor.fetchall()

fecha_actual = datetime.datetime.now().strftime("%m-%d")

for resultado in resultados:
    fecha_nacimiento = resultado['fecha_de_nacimiento']
    fecha_nacimiento_str = fecha_nacimiento.strftime('%Y-%m-%d')
    fecha_cumple = fecha_nacimiento.strftime("%m-%d")
    if fecha_actual == fecha_cumple:
        os.chdir("C:/Users/clase/OneDrive/Escritorio/NAO Evidencias/RETO3/POO-Cumpleaños-Terminos/")
        subprocess.call(["python", "cumpleaños.py"])
        break