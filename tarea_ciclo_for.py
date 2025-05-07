
for i in range(0,4):
 loteria = int(input("ingrese un numero:"))

 if loteria == 10:
     
     print("ganaste la loteria")
     break
 elif loteria == 30:
  print("ganaste un carro")
  break
 elif i == 3:
    print("numero de intentos exedido, GAME OVER")        
 else:
     print("numero incorrecto")