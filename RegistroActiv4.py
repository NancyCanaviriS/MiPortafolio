# registro de estudiantes

cantidad = int(input("la cantidad de estudiantes a registrar:"))
estudiantes=[]
mayores = 0
menores = 0

for i in range(cantidad):
    print("\ingresar los datos del estudiantes:",{i+1})
    nombre=input("nombre: ")
    edad = int(input("edad: "))
    estudiante={"nombre": nombre,"edad": edad}
    estudiantes.append(estudiante)

for estudiante in estudiantes:
   if estudiante["edad"]>=18:
    print(estudiante['nombre'] ," es mayor de edad")
   mayores +=1
else:
   print(estudiante['nombre'] ," es menor de edad")
   menores +=1

edades=estudiante["edad"] + 5
print(estudiante['nombre'],"tendra",edades,"anos en 5 anos")
print("estudiantes registrados son:",cantidad)
print("estudiantes mayores son:",mayores)
print("estudiantes menores son:",menores)

numero = int(input("intoduce un nro para ver su tabla de multiplicacion:"))
for i in range (1, 11):
   resultado = numero * i
   print(numero," x ", i," = ", resultado)