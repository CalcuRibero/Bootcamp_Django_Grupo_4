# Buscar en una lista de nombres y en una lista de 
# numeros el elemento que mas cantidad de veces aparece
# , obtener el elemento y la cantidad de veces que aparece


from collections import Counter

lista_nombres = ['Ana', 'Jhon', 'Daniel', 'Melissa', 'Juan', 'Melissa', 'Daniel', 'Ana', 'Melissa']
numeros = [4, 5, 2, 9, 0, 34, 5, 7, 9, 54, 0, 5, 9, 7, 4, 2, 0, 0]

contador = Counter(numeros)
elemento_mas_repetido = contador.most_common(1)

for elemento in elemento_mas_repetido:
    print (f"el elemento mas repetido es: {elemento[0]}, se repitio {elemento[1]} veces")