#Sindy Marcela Cuatin Cuastumal
#Juan Diego Muñoz Ospina
##punto número 2 y 4 del taller de Ia
#punto2 IA
#clasificar números indicando al final la cantidad de números pares y la cantidad de numeros impares,
#el dato a ingresar es un número. Solo se deja de pedir número cuando el  usuario ingrese el numero cero


contadorpar=0
contadorimpar=0
while True:
    
    numero=int(input("Ingrese un numero:  "))
    if numero!=0:
        if numero%2==0:
            contadorpar+=1
        else:
            contadorimpar+=1 
    else:
        print("Usted a ingresado la siguiente cantidad de numeros pares: ")
        print(contadorpar)
        print("Usted a ingresado la siguiente cantidad de numeros impares: ")
        print(contadorimpar)
        break


# punto 3
# Para un grupo de estudiantes se conoce las notas de las 7 materias cursadas.
# Escriba un algoritmo que permita introducir los datos de cada estudiante, los
# almacene y que luego imprima:

# Los datos del estudiante con la nota más alta de todas las notas.
# El promedio de notas de cada estudiante.
# El promedio de notas de cada materia.
# La nota que más se repite por cada materia
# porcentaje de aprobados y reprobados para cada materia.

estudiantes=[]
notas=[]
cantidad= int(input("Ingrese la cantidad de estudiantes: "))
for x in range (cantidad) :
    est= input("Ingrese el nombre del estudiante: ")
    estudiantes.append(est)
    y=1
    cont=0
    while y<=7:
         nota= float(input("Ingrese la calificación {}: " .format(y)))
         notas.append(nota)
         cont= cont + nota
         y=y+1

print(estudiantes)
print(notas)


MATERIAS = 2
nombre = input("Nombre completo: ")

contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    sumatoria = sumatoria + calificacion
    contador = contador + 1

promedio = sumatoria / MATERIAS
print("Nombre: {} , promedio {}".format(nombre ,promedio))


#punto 4
# Diseña un programa que, dado un carácter cualquiera, lo identifique como vocal
# minúscula, vocal mayúscula, consonante minúscula, consonante mayúscula u
# otro tipo de carácter.

caracter = input("Ingresar un carácter: ")
vocal=['a','e','i','o','u']

aux = None
if caracter in vocal:
    aux="vocal minuscula"
elif caracter in [x.upper() for x in vocal]:
    aux = "VOCAL MAYUSCULA"
elif caracter >= "B" and caracter<="Z":
    aux = "Consonante mayúscula"
elif caracter >= "b" and caracter<="z":
    aux = "Consonante minúscula"

print(aux)