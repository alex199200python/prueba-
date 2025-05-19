class Personas():
    def __init__(self, nombre, cedula, edad, correo, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.correo = correo
        self.telefono = telefono

    def enviarCorreo(self):
        print(f"Enviando correo a {self.correo}")

    def enviarMensaje(self):
        print(f"Enviando mensaje a {self.telefono}")

class Estudiantes(Personas):
    def __init__(self, nombre, cedula, edad, correo, telefono, curso):
        super().__init__(nombre, cedula, edad, correo, telefono)
        self.curso = curso

    def saludar(self):
        print(f"Hola {self.nombre}")

    def matricular(self):
        print(f"El estudiante se matriculo a {self.curso}")
        super().enviarCorreo()

class Docentes(Personas):
    def __init__(self, nombre, cedula, edad, correo, telefono, curso):
        super().__init__(nombre, cedula, edad, correo, telefono)
        self.curso = curso

    def dicta(self):
        print(f"El docente esta cursando {self.curso}")

estudiante1 = Estudiantes("Juan", 123456, 30, "xyz@gmail.com", 30034433, "Física")
estudiante1.saludar()
estudiante1.matricular()
docente1 = Docentes("Pedro", 18495, 40, "abc@gmail.com", 3222333, "Física")
#docente1.enviarCorreo()
#docente1.enviarMensaje()

