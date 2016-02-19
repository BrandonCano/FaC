TemperaturaF= int(input("Cual es la temperatura en Fahrenheit: "))
Celcius= 5*(TemperaturaF-32)//9
if Celcius>100:
    print(TemperaturaF ,"grados Fahrenheit son", Celcius, " grados celcius, el agua si hierve a esta temperatura")
else:
    print(TemperaturaF ,"grados Fahrenheit son", Celcius, " grados celcius, el agua no hierve a esta temperatura")
