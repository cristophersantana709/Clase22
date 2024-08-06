nota1=int(input("Ingresar nota1: "))
nota2=int(input("Ingresar nota2: "))
nota3=int(input("Ingresar nota3: "))
examen=int(input("Ingresar nota del Examen:"))

suma=nota1+nota2+nota3+examen

Promedio=suma/4
if Promedio>=90:
    print("a")
elif Promedio>=80: 
    print("b")
elif Promedio>=70:
    print("c")
elif Promedio>=60:
    print("D")
else:
    print("E")