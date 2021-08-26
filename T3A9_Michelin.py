SueldoBase=float(input("Ingrese el sueldo base: "))
AñosAntiguedad=int(input("Ingrese los años de antiguedad: "))

EstadoCivil=input("Ingrese el estado civil: (1 para 'Soltero', 2 para 'Casado'")
if EstadoCivil=="1":
    EstadoCivil=True
elif EstadoCivil=="2":
    EstadoCivil=False
else:
    print("Estado civil no valido")

if EstadoCivil==True or EstadoCivil==False:
    if EstadoCivil==True:
        print("Sueldo Neto: ", ((SueldoBase)+((SueldoBase*0.05)*AñosAntiguedad))-((SueldoBase*0.11)+(SueldoBase*0.03)+(SueldoBase*0.03)))
    else:
        print("Sueldo Neto: ", ((SueldoBase)+((SueldoBase*0.07)*AñosAntiguedad))-((SueldoBase*0.11)+(SueldoBase*0.03)+(SueldoBase*0.03)))