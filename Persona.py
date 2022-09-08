#Sindy Marcela Cuatin Cuastumal
#Juan Diego Muñoz Ospina

##punto número 1 del taller de Ia

from turtle import st


class Persona:
    """Esta clase define el comportamiento de una persona"""
    edad=0
    sexo=0

    def __init__(self,edad,sexo):
        self.edad=edad
        self.sexo=sexo



p1=Persona(15,'m')
p2=Persona(16,'m')
p3=Persona(17,'m')
p4=Persona(18,'m')
p5=Persona(19,'m')
p6=Persona(20,'m')
p7=Persona(15,'f')
p8=Persona(16,'f')
p9=Persona(17,'f')
p10=Persona(18,'f')
p11=Persona(19,'f')
p12=Persona(19,'f')
p13=Persona(19,'f')
p14=Persona(19,'m')
p15=Persona(19,'m')
personitas= [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 ]
masculinas_mayores_de_edad=0
femeninas_menores_de_edad=0
personas_mayores=0
personas_menores=0
porcentajeMayores=0
porcentajemenores=0

for i in personitas:
   if  i.edad>18:
       personas_mayores=personas_mayores+1
       if i.sexo=="m":
           masculinas_mayores_de_edad=masculinas_mayores_de_edad+1
   else:
       personas_menores=personas_menores+1
       if i.sexo=="f":
           femeninas_menores_de_edad=femeninas_menores_de_edad+1

porcentajeMayores=personas_mayores*100/15
porcentajemenores=personas_menores*100/15

print("Las personas masculinas_mayores_de_edad son :"+str(masculinas_mayores_de_edad) +"\n","Las personas_menores femeninas son :"
+str(femeninas_menores_de_edad)+"\n","Las personas mayores son "+str(personas_mayores)+"\n","Las personas menores son :"+str(personas_menores)+
"\n","El porcenta de menores es ;"+str(porcentajemenores)+"\n","El porcenta de mayores son "+str(porcentajeMayores)+"\n")


