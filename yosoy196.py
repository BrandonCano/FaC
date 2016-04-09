numero1= int(input("En que numero comienza la lista: "))
numero2= int(input("En que numero termina la lista: "))
lista=list(range(numero1,numero2+1))

for n in lista:
    inverso_n=int(str(n)[::-1])
    suma=inverso_n+n
    inverso_checa=int(str(suma)[::-1])
    if n==inverso_n:
        print(n,"es palindromo")
    elif(suma==inverso_checa):
        print(n,"No es un numero Lychrel")
    else:
        print(n,"Es un numero Lychrel")
