"""
Escribe un programa que permita al usuario ingresar una frase
y determine si es un palindromo o no.
"""

frase_user = input("Introduce la frase:")
frase_user_invert_1 = frase_user[::-1]

if(frase_user_invert_1 == frase_user):
    print("Es un palindromo.")
else:
    print("No es un palindromo.")
