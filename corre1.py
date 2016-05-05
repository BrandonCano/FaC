import math

puntox1= int(input("Posicion de la cordenada X1: "))
puntoy1= int(input("Posicion de la cordenada Y1: "))
puntox2= int(input("Posicion de la cordenada X2: "))
puntoy2= int(input("Posicion de la cordenada Y2: "))

def distancia (x1,y1,x2,y2):
    lejitos=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return lejitos

print("La distancia entre el punto (",puntox1,",",puntoy1,") y el punto (",puntox2,",",puntoy2,") es:","%.2f"%distancia(puntoy1,puntoy1,puntox2,puntoy2))
