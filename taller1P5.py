#Sindy Marcela Cuatin Cuastumal
#Juan Diego Muñoz Ospina
##punto número 5 del taller de Ia
#5. Usted ha sido contratado para realizar un programa en Python para resolver los  procesos de facturación de un supermercado, analice el programa y defina los  procesos a implementar debe tener:  
#a. Diferenciar sobre los diferentes productos con iva  
#b. Elementos de la canasta familiar  
#c. Productos de aseo  
#d. Elementos Top.  

#Para lo propuesto se recomienda definir objetos de tipo producto

class Producto:
    name = ""
    iva=False
    Canasta_Familiar=False
    producto_aseo=False
    Elemento_top=False

    def __init__(self,name,iva,canasta_familiar,producto_aseo,Elemento_top):
        self.name = name
        self.iva =iva
        self.Canasta_Familiar = canasta_familiar
        self.producto_aseo= producto_aseo
        self.Elemento_top= Elemento_top

    #Métodos correspondientes al producto
    #def is_produc_iva
    #def is_canasta_familiar
    #def is_produc_Aseo
    #def is_Elemtos_top




