num1= int(input("Desde que numero empezara a sumar: "))
num2= int(input("Donde terminara de sumar: "))
contador=num1
suma=0

while(contador<=num2):
    suma=contador+suma
    contador=contador+1

print(suma)
