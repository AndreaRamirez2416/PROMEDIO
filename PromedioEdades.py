def CalcularPromedioDeEdad():
    Cantidad_Salones=int(input("digite la cantidad de salones "))
    Suma_Edades=0
    for j in range(1,Cantidad_Salones+1):
        Cantidad_Alumnos=int(input("digite la cantidad de alumnos "))
        for i in range(1,Cantidad_Alumnos+1):
            Edad= float(input("digite la edad del alumno "))
            Suma_Edades=Suma_Edades+Edad

    Promedio_Edad=Suma_Edades/Cantidad_Alumnos
    print(Promedio_Edad)

CalcularPromedioDeEdad()


