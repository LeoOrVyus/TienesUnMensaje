import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="empleados"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE empleados2 (nombre VARCHAR(255), correo VARCHAR(255), fecha_de_nacimiento DATEtime, tipo_de_empleado VARCHAR(255))")
