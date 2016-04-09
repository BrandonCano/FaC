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
def promedio (a):
    suma=0
    for i in a:
        suma += i
        res=suma/len(a)
    return res
print ("Esta es tu lista ",lista,"El promedio de esta es ",promedio(lista)," y el standard deviation es","%.1f" % rara())
