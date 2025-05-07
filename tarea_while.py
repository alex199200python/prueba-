

contador = 0

while contador < 4:
    contador += 1
    print(contador)
    carro = int(input("ingrese un numero:"))
    if carro == 20:
     print("ganaste la loteria")
     break
     
    elif carro == 30:
         print("ganaste un carro")
         break
    elif contador == 4:
       print("numero de intrnto exedido, GAME OVER")
    else:
     print("numero incorrecto")



