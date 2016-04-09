lista=[]
print("Dame 10 numero")
n=0
while  n<11:
    n=int(input("Dame el numero:"))
    lista.append(n)
    n=n+1
def rara():
    contador=0
    for x in lista:
        ave=x-promedio
        chido=ave*ave
        contador=contador+chido
    return contador
suma=0
for i in lista:
    suma += i
    promedio=suma/len(lista)
print ("Esta es tu lista ",lista,"El promedio de esta es ",promedio," y el standard deviation es","%.1f" % rara())
