
import random
contador=0
respuesta=0


n=random.randint(0,101)

while respuesta!=n:
    respuesta=0
    respuesta = int(input("Intente adivinar el numero: "))

    if respuesta>n:
        contador=contador+1
        print(respuesta," es mayor, intenta con otro numero mas pequeño")


    elif respuesta<n:
        contador=contador+1
        print(respuesta," es menor, intenta con otro numero mas grande")

    else:
        print("has acertado el numero, lo has intentado: ",contador," veces")
