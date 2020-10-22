"""
Escribe un programa que permita al usuario ingresar una frase y luego
un caracter (string de longitud 1) y luego muestre la frase ingresada, pero
con todas las ocurrencias del caracter indicado por el usuario reemplazadas por "*".
"""
frase_user = input("Introduce una frase:")
caracter_user = input("Introduce un caracter:")

if(len(caracter_user)==1):
    frase_cambiada = frase_user.replace(caracter_user, "*");
    print(frase_cambiada)
else:
    print("Has introducido mas de un caracter")



