class Cuentas:
    def __init__(self, numero, saldo, contrasena, titular):
        self.numero = numero
        self.saldo = saldo
        self.contrasena = contrasena
        self.titular = titular

    def verSaldo(self):
        print(f"Su saldo es {self.saldo}")

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        print(f"Nuevo saldo de la cuenta {self.numero} es {self.saldo}")

    def retirar(self, monto):
        if self.saldo < monto:
            print("Saldo insifuciente")
            return False
        else:
            self.saldo = self.saldo - monto
            print("Nuevo saldo ", self.saldo)
            return True

cuentas = [
    Cuentas("001", 1000000, "contra1", "Juan"),
    Cuentas("002", 0, "contra2", "Ana"),
    Cuentas("003", 0, "contra3", "Maria"),
    Cuentas("004", 0, "contra4", "Pedro"),
]


def validar_cuenta():
    cuentaNumero = input("Ingrese su numero de cuenta ")
    contra = input("Ingrese su contraseña ")
    for cuenta in cuentas:
        if cuenta.numero == cuentaNumero and cuenta.contrasena == contra:
            print("Cuenta validada con exito")
            return cuenta
    print("Error al validar cuenta")
    return None

def buscar_cuenta(numero):
    for cuenta in cuentas:
        if cuenta.numero == numero:
            print("Si existe la cuenta")
            return cuenta
    print("No se encontro la cuenta")
    return None

validar = validar_cuenta()

while validar != None:
    print("Bienvenido")
    print("Ingrese una de las siguientes opciones:")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Salir")
    opcion = input("> ")

    if opcion == "1":
        validar.verSaldo()

    if opcion == "2":
        monto = int(input("monto "))
        validar.depositar(monto)

    if opcion == "3":
        monto = int(input("monto "))
        validar.retirar(monto)

    if opcion == "4":
        numCuentaDestino = input("Ingresa la cuenta destino: ")
        cuentaDestino = buscar_cuenta(numCuentaDestino)
        monto = int(input("monto "))
        retirar = validar.retirar(monto)
        if retirar == True:
       # validar.retirar(monto)
         cuentaDestino.depositar(monto)


print("prueva repositorio")

