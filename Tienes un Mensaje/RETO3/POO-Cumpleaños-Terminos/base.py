import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Grettel33",
  database="empleados"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE empleados (nombre VARCHAR(255), correo VARCHAR(255), fecha_de_nacimiento DATE, tipo_de_empleado VARCHAR(255))")
