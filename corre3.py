def superpower (base,elevado):
    aco=1
    num=base
    while(aco<elevado):
        num=num*base
        aco=aco+1
    return num
base= int(input("Dame el numero base: "))
elevado= int(input("Dame la pontencia a la que se elevara:"))

print("La potencia del numero: ",base, "elevado a la: ",elevado," veces es: ",superpower(base,elevado))
