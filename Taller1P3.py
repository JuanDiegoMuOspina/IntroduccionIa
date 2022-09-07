from re import M


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
        



class Persona:
    """Esta clase define el comportamiento de una persona"""
    name=""
    m1=[]
    promedio=0

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



#definiendo una persona con la materia para pruebas en consola
a=Materia("Matematicas",[3,0,8])
a1=Materia("Matematicas",[3,1,8])
a2=Materia("Matematicas",[3,2,8])
a3=Materia("Matematicas",[3,3,8])
a4=Materia("Matematicas",[3,4,8])
a5=Materia("Matematicas",[3,5,8])
a6=Materia("Matematicas",[3,6,8])
p1=Persona("Manuel",[a,a1,a2,a3,a4,a5,a6])
b=Materia("Matematicas",[3,3,8])
b1=Materia("Matematicas",[3,3,8])
b2=Materia("Matematicas",[3,4,8])
b3=Materia("Matematicas",[3,5,8])
b4=Materia("Matematicas",[3,4,8])
b5=Materia("Matematicas",[3,5,8])
b6=Materia("Matematicas",[3,9,8])
p2=Persona("Carlos",[b,b1,b2,b3,b4,b5,b6])

#el estudiante con la nota mas alta
num1=p1.promedioNotas()
num2=p2.promedioNotas()
if (num1>num2):
   print("el estudiante con la nota mas alta",p1.promedioNotas(),p1.name)
else:
   print("el estudiante con la nota mas alta",p2.promedioNotas(), p2.name)

