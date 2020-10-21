"""
Escribir una funcion cuadrados(L) que reciba una secuencia de numeros,
devuelve la lista de los cuadrados de esos números, en el mismo orden.
"""
def cuadrados(l):
    result = []
    for x in l:
        result.append(x)
    return result
l = 5,4,7,8,3,3.4,9
print(cuadrados(l))