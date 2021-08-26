a=int(input("Ingrese la nota del primer parcial"))
b=int(input("Ingrese la nota del segundo parcial"))

if a<=0 or a>=11 or b<=0 or b>=11:
    print("Error, Nota no valida")
elif a>=7 and b>=7:
    print("El alumno promociona")
elif a>=4 and b>=4:
    print("El alumno aprueba")
else:
    print("El alumno debe recuperar")