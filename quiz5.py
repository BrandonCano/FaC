palabras=str(input("Escribe una palabra u oracion: "))
def is_palindrome (a):
    minisculas=a.lower().replace(' ', '')
    s=""
    palindromo=str(minisculas)[::-1]
    if minisculas==palindromo:
        res=print("La palabra u oracion: ",a,"es un palindromo")
    else:
        res=print("La palabra u oracion:  ",a,"no es un palindromo")
    return s
print(is_palindrome(palabras))
