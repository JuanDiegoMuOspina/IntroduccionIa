#Sindy Marcela Cuatin Cuastumal
#Juan Diego Muñoz Ospina
##punto número 3 del taller de Ia

class Materia:
    name=""
    notas=[]

    def __init__(self,name,notas):
        self.name=name
        self.notas=notas

    def promedioNotas(self):
        contador=0
        for nota in self.notas:
            contador+=nota
        contador=contador/3
        return contador

    def notaMasRepetida(self):
      return self.notas

        



class Persona:
    """Esta clase define el comportamiento de una persona"""
    name=""
    m1=[]
    promedio=0
    promedio_materia={}

    def __init__(self,name,m1):
        self.name=name
        self.m1=m1

    def promedioNotas (self):
        contador=0
        dividir=0
        for nota in self.m1:
            self.promedio+=nota.promedioNotas()
            dividir+=dividir+1
            if nota.promedioNotas()>contador:
                contador=nota.promedioNotas()
        self.promedio/dividir

        return contador


    def promedio_materia_dir(self):
         indice=0
         for nota in self.m1:
           self.promedio_materia["materia"+str(indice)]=nota.name
           self.promedio_materia["nota"+str(indice)]=nota.promedioNotas()
           indice=indice+1
         return self.promedio_materia


    def obtenerNotasPorMaterias(self,materia):
        for nota in self.m1:
          if(nota.name==materia):
            return nota.notaMasRepetida()         
           
        
    def is_aprobado(self,materia):
        for nota in self.m1:
          if(nota.name==materia):
           if nota.promedioNotas()>=5.5:
               return True
           else:
               return False
#definiendo una persona con la materia para pruebas en consola
a=Materia("Matematicas",[3,0,8])
a1=Materia("ciencias",[3,1,8])
a2=Materia("quimica",[3,2,8])
a3=Materia("sociales",[3,3,8])
a4=Materia("espanol",[3,4,8])
a5=Materia("fisica",[3,5,8])
a6=Materia("ingles",[3,6,8])
p1=Persona("Manuel",[a,a1,a2,a3,a4,a5,a6])
b=Materia("Matematicas",[3,3,8])
b1=Materia("ciencias",[3,3,8])
b2=Materia("quimica",[4,4,8])
b3=Materia("sociales",[3,5,8])
b4=Materia("espanol",[3,4,8])
b5=Materia("fisica",[5,5,8])
b6=Materia("ingles",[8,9,8])
p2=Persona("Carlos",[b,b1,b2,b3,b4,b5,b6])

#el estudiante con la nota mas alta
num1=p1.promedioNotas()
num2=p2.promedioNotas()
if (num1>num2):
   print("\n el estudiante con la nota mas alta",p1.promedioNotas(),p1.name)
else:
   print("\n el estudiante con la nota mas alta",p2.promedioNotas(), p2.name)

#promedio de notas de cada estudiante

print("\n el promedio de notas del estudiante "+p1.name+" es :"+str(num1))
print("\n el promedio de notas del estudiante "+p2.name+" es :"+str(num2))

print("\n el promedio de cada materia del estiante "+p1.name+" son :",p1.promedio_materia_dir())
print("\n el promedio de cada materia del estiante "+p2.name+" son :",p2.promedio_materia_dir())

#la nota que mas se repite por cada materia

def obtenerNotaMasRepetida(p1, p2):
    notas_repetidas = ["Matematicas","ciencias","quimica","sociales","espanol","fisica","ingles"]
    estudiante=[p1,p2]
    notas_revisadas={}


    for i in notas_repetidas:
        notas_almacenadas= []
        for j in estudiante:
           notas_almacenadas+=j.obtenerNotasPorMaterias(i)
        notas_revisadas[i]=definirLaNotaMasRepetida(notas_almacenadas)
    print("\n Las notas que mas se repten en cada materia son : \n",notas_revisadas)
#Porcentaje de las notas
def materiasPerdidas():
    materias = ["Matematicas","ciencias","quimica","sociales","espanol","fisica","ingles"]
    estudiante=[p1,p2]
    contador=0
    prcentajes_Materias_Ganados={}
    for i in materias:
        
        for j in estudiante:
            if j.is_aprobado(i)==True:
                contador+=1
        Procentaje_Ganado=contador*100/2
        porcentaje_Perdido=(Procentaje_Ganado-100)*-1
        prcentajes_Materias_Ganados[i]=str(Procentaje_Ganado)+"porcentaje ganado \n"
        prcentajes_Materias_Ganados[i]+=str(porcentaje_Perdido)+"porcentaje perdido \n"

    print("\n Listado de los porcentajes de estdudiantes que han aprobado o perdido \n",prcentajes_Materias_Ganados)


def definirLaNotaMasRepetida(notas):

    repeticiones=0
    num_repetivo=0
    repeticiones_tem=0
    for i in notas:
            num1 = i
            for j in notas:
                if num1==j:
                    repeticiones+=1
            if repeticiones>repeticiones_tem:
                repeticiones_tem=repeticiones
                repeticiones=0
                num_repetivo=i
            else:
                repeticiones=0
    repeticiones_tem=0
    return num_repetivo


obtenerNotaMasRepetida(p1,p2)
materiasPerdidas()