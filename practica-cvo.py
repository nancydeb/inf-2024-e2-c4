
# enteros
entero = 543
print(entero)

# float - decimal
decimal = 0.43
print(decimal)

# string
cadena = "Info 2024-07-11"
cadena1 = 'Info 2024-07-11'
cadena2 = """DOCSTRING"""
cadena3 = '''DOCSTRING'''
print(cadena)

# Booleano
verdadero = True
print(verdadero)
falso = False
print(falso)
# vacío, null, nulo, None, nil
vacio= None
print(vacio)

# funcion type(), qué tipo de dato tiene dentro
print(type(vacio))

## Tipos de datos estructurados/complejos
# list (array).
lista=[1, 2, 3, 4, 5, 6, 7, 8, "algo"]
# La lista tiene 9 elementos.
# A los elementos se accede a través índice lista.
print(lista)
print(lista[3])
lista_lista= [[3, 2, 1], [7, 6, 5], [10, 11, 13]]
# ¿Cómo accedo al N° 7?
# concatenando...
print(lista_lista)
print(lista_lista[1][0])
lista_lista.append(2)
print(lista_lista)
print(lista_lista[3])
lista_lista[3]= 365
print(lista_lista)
 
 ## Tipos de datos estructurados/complejos
 #  # list lista = [1,2,3,4,5,6,7,8,"algo"] # 9 elementos. 
 # El índice empieza en 0. print(lista) print(lista[3]) 
 # lista_lista = [[3,2,1], [7,6,5], [10,11,13]]

# tuplas. Las tuplas son inmutables
tuplas= (3, 2, 1, 2, 2, 2, 2)
print (tuplas)
print (tuplas[2])
tuplass= (3, 2, 1, 2, 2, 2, 2, "ask")
tuplasss= (3, 2)
print(tuplass)
print(tuplasss)

# set -conjunto  1, 2, 3
#los valores que devuelve no se repiten(son únicos).
# devuelve {1, 2, 3, 4, 5, 6, 7, 8, 9} Ej.:
conjuntos= {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
print(conjuntos)
for i  in conjuntos:
    print(i)
    
conjunto= {1, 2, 3, 4, "123", "123"}
print(conjunto)
#devuelve {1, 2, 3, 4, "123"}

# definidos por el programador, librerias, dataframe(df)

# diccionarios, map, clave-valor, key-value
diccionario= {"llave": "valor", 1:"uno"}
print(diccionario)
print(diccionario["llave"])
print(diccionario [1])
capitales= {"Chaco":"Resistencia", "Corrientes":"Corrientes",
            "Misiones":"Posadas"}
print (capitales["Misiones"])
ciudades= {"Chaco":["Resistencia", "Fontana", "Barranqueras"],
           "Corrientes":"Corrientes","Misiones":"Posadas"}
print (ciudades["Chaco"])
# Devuelve Resistencia, Fontana, Barranqueras

