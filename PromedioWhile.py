def CalcularPromedioDeEdad():
    Cantidad_Alumnos=int(input("digite la cantidad de alumnos "))
    i=1
    Suma_Edades=0
    while i < (Cantidad_Alumnos+1):
        Edad= int(input("digite la edad del alumno "))
        Suma_Edades=Suma_Edades+Edad
        i=i+1

    Promedio_Edad=Suma_Edades/Cantidad_Alumnos
    print(Promedio_Edad)

CalcularPromedioDeEdad()
