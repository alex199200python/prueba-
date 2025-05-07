# problema  1:  Numeros Primos Y Gemelos 
#un mumro primo es auqel que solo es divisible por 1y por si mmismo. dos numeros primos se considerangemelos si la diferencia entre ellos es exactamente 2.

# requisitos 

# 1 pide al usuario que ingrese un numero entero positivo N mayor que 2.
# 2 encuentra y muestra todos los pares de numeros primos gemels menores o iguales a N.
# 3 si no hay pares de primos guemelos muestra un mensaje indecando que no existen es ese rango
#ejemplo

# ingreso un numero: 20
#pares de primos jemelos:



num=int(input("ingrese un numero: "))

if num >1:
    con=0
    i=2
    while i<num and cont==0:
        resto=num%i
        if resto==0:
            cont+=1
        i+=1
    if cont=00:
       print(num)
