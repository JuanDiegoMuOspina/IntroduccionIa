palabra=input('Ingrese la palabra : ')

def isPalindromo(palabra):
    palabra2=""
    i=len(palabra)
    while i>0:
        palabra2+=palabra[i-1]
        i=i-1
    print (palabra2)
    if palabra2==palabra:
        print("Palindromo")
    else:
        print("no lo es Palindromo")



def is_parangrama (palabra):
    import string
    #obtener el alfabeto
    alfabeto=string.ascii_lowercase
    for letra in alfabeto:  #Recorrer el alfabeto
        if letra not in palabra:  # Si una letra del alfabeto no está, sabemos que no es pangrama
            print( "No es pangrama")
   
    return print("si lo es un pangrama")
isPalindromo(palabra)
is_parangrama(palabra)
