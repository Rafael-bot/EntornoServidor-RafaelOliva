despedida = "Sois una clase cojonuda. Os echaré de menos"
dict_repeticiones = {}

for caracter  in despedida:
    if(caracter in dict_repeticiones):
        dict_repeticiones[caracter] = dict_repeticiones[caracter]+1
    else:
        dict_repeticiones.update({caracter:1})

print(dict_repeticiones)
