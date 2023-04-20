import tkinter as tk
from tkcalendar import DateEntry
from datetime import date
import mysql.connector

class Empleado:
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        self.nombre = nombre
        self.correo = correo
        self.fecha_de_nacimiento = fecha_de_nacimiento

class Programador(Empleado):
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        super().__init__(nombre, correo, fecha_de_nacimiento)

class Gerente(Empleado):
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        super().__init__(nombre, correo, fecha_de_nacimiento)

def crear_empleado():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    fecha_de_nacimiento = fecha_nacimiento_cal.get_date()
    tipo_de_empleado = variable_tipo.get()
    
    if tipo_de_empleado == "Programador":
        empleado = Programador(nombre, correo, fecha_de_nacimiento)
    elif tipo_de_empleado == "Gerente":
        empleado = Gerente(nombre, correo, fecha_de_nacimiento)
    else:
        empleado = Empleado(nombre, correo, fecha_de_nacimiento)
    
    print("Empleado creado:")
    print(f"Nombre: {empleado.nombre}")
    print(f"Correo: {empleado.correo}")
    print(f"Fecha de nacimiento: {empleado.fecha_de_nacimiento}")
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Grettel33",
        database="empleados"
    )

    cursor = mydb.cursor()

    sql = "INSERT INTO empleados (nombre, correo, fecha_de_nacimiento, tipo_de_empleado) VALUES (%s, %s, %s, %s)"
    if isinstance(empleado, Programador):
        val = (empleado.nombre, empleado.correo, empleado.fecha_de_nacimiento, "Programador")
    elif isinstance(empleado, Gerente):
        val = (empleado.nombre, empleado.correo, empleado.fecha_de_nacimiento, "Gerente")
    else:
        val = (empleado.nombre, empleado.correo, empleado.fecha_de_nacimiento, "Empleado")

    cursor.execute(sql, val)

    mydb.commit()

    mydb.close()

    print("Empleado creado y guardado en la base de datos.")

# interfaz
ventana = tk.Tk()
ventana.title("Registro de empleados")

#widgets de la interfaz
label_nombre = tk.Label(ventana, text="Nombre:")
entry_nombre = tk.Entry(ventana)
label_correo = tk.Label(ventana, text="Correo:")
entry_correo = tk.Entry(ventana)
label_fecha_de_nacimiento = tk.Label(ventana, text="Fecha de nacimiento:")
label_fecha_de_nacimiento.grid(column=0, row=2)
fecha_nacimiento_cal = DateEntry(ventana, width=12, background='darkblue',
                                 foreground='white', date_pattern='yyyy-mm-dd', 
                                 maxdate=date.today())
fecha_nacimiento_cal.grid(column=1, row=2)
label_tipo = tk.Label(ventana, text="Tipo de empleado:")
variable_tipo = tk.StringVar(value="Empleado")
optionmenu_tipo = tk.OptionMenu(ventana, variable_tipo, "Empleado", "Programador", "Gerente")
button_crear_empleado = tk.Button(ventana, text="Crear empleado", command=crear_empleado)

# widgets en la ventana
label_nombre.grid(row=0, column=0, sticky=tk.E)
entry_nombre.grid(row=0, column=1)
label_correo.grid(row=1, column=0, sticky=tk.E)
entry_correo.grid(row=1, column=1)
label_fecha_de_nacimiento.grid(row=2, column=0, sticky=tk.E)
label_tipo.grid(row=3, column=0, sticky=tk.E)
optionmenu_tipo.grid(row=3)

button_crear_empleado.grid(row=4, column=1, pady=10)

ventana.mainloop()