
rep=0
r=1
while rep==0:
    n= int(input("De que numero quieres saber el factorial: "))
    if n<0:
        print("por favor, eliga un numero positivo")
        rep=0
    else:
        rep=1
        contador=0
        while contador<n:
            contador=contador+1
            r=contador*r
print("El factorial de ",n," es ",r)
