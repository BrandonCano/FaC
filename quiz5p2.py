def find_threes():
    con=0
    suma=0
    nada=""
    n=int(input("Cuantos numeros desa ingresar:"))
    lista=list()
    lista3=list()
    while n>con:
        r=int(input("Ingresa los numeros por favor: "))
        lista.append(r)
        con=con+1
    for z in lista:
        if (z%3==0):
            suma=z+suma
            lista3.append(z)
    print("Estos son los numero que ingresaste",lista,"de los cuales estos son divisibles entre 3 ",lista3," y la suma de estos numeros es: ",suma)
    return nada
print(find_threes())
