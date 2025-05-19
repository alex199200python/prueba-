
class Cuentas:
    def _init_(self,numero, saldo, contraseña, titular):
        self.numero = numero 
        self.saldo = saldo 
        self.contraseña = contraseña
        self.titular = titular

    def verSaldo(self):
        print(f"Su saldo es {self.saldo}") 
                            
    def depositar(self,monto):
        self.saldo = self.saldo + monto 
        print("Nuevo Saldo", self.saldo)

    def retirar(self,monto):
        if self.saldo < monto:
           print("saldo insuficiente")
        else:
           self.saldo = self.saldo - monto
           print("Nuevo.saldo", self.saldo)   

cuentas = [
   Cuentas("001", 0, "contra1", "juan"),
   Cuentas("002", 0, "contra2", "ana"),
   Cuentas("003", 0, "contra3", "maria"),
   Cuentas("004", 0, "contra4", "pedro"),
]

def validar_cuenta():
    cuentaNumero = input("ingrese su numero de cuenta")
    contra = input("ingrese su contraseña")
    for cuenta in cuentas:
     if cuenta.numero == cuentaNumero and cuenta.contraseña == contra:
      print("cuenta validada con exito")
    return cuenta
    print("error al validar cuenta")
    return None

def buscar_cuenta(numero):
   for cuenta in cuentas:
      if cuenta.numero == numero:
       print("Si existe la cuenta")
       return None

Validar = "validar_cuenta"()

while Validar != None:
    print("Bienvenido")
    print("ingrese una de las siguientes opciones:")
    print("1. Cunsultar saldo")
    print("2. Depositar")
    print("3. Retitar")
    print("4. Transferi")
    print("5. Salir")
    opcion =input(">") 
    #opcion = input("ingresa 1 si quieres retirar o 2 si quieres Depositar:")

    if opcion == "1":
        Validar.verSaldo()

    if opcion == "3":
        monto = int(input("monto"))
        Validar.retirar(monto)

    if opcion == "2":    
        monto = int(input("monto"))
        Validar.depositar(monto)

    if opcion == "4":
       numCuentaDestino = input("ingresa la cuenta de destino")
       cuentaDestino = buscar_cuenta(numCuentaDestino)
       monto = int(input("monto"))
       cuentaDestino.depositar(monto) 
          
