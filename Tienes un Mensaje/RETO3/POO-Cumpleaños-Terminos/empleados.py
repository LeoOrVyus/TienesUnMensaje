class Empleado:
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        self.nombre = nombre
        self.correo = correo
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Fecha de nacimiento: {self.fecha_de_nacimiento}")

class Programador(Empleado):
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        super().__init__(nombre, correo, fecha_de_nacimiento)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lenguaje: {self.lenguaje}")

class Gerente(Empleado):
    def __init__(self, nombre, correo, fecha_de_nacimiento):
        super().__init__(nombre, correo, fecha_de_nacimiento)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")
