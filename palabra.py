palabra=(input("¿Que palabra quieres buscar?:  "))
def numpalabra():
    archivo=open('Hola.txt','r')
    cantidad=0
    for i in archivo:
        minisculas=i.lower()
        sub=minisculas.find(palabra)
        while sub !=-1:
            cantidad=cantidad+1
            sub=minisculas.find(palabra,(sub+1))
    return(cantidad)
    close('Hola.txt')
ba=numpalabra()
print("las veces que se encuentra la palabra: ", palabra, " es ",ba)
