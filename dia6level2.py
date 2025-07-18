#Dia 6, crea un tuple
#==//Paso 1 
#Crea un tuple vacio 
tuple_vacia= ()
#crea una con nombres de hermanos y hermanas (imaginarios esta bien)
tuple_vacia= ("Juanita" , "Frida ")
tuple_vacia1= ("Juan" , "Pepe")
tuplellena= (tuple_vacia+tuple_vacia1)
cantidad= len(tuplellena)
print ("Tengo:", cantidad, "De hermanos")
papas= ("Laura" , "Honorio")
miembros_de_la_familia= papas+tuplellena
print (miembros_de_la_familia)

mama, papa, hermana1, hermana2, hermano1, hermano2 = miembros_de_la_familia
print ("Mama:", mama)
print ("Papa: ", papa)
print ("Hermano: ", hermano1)
print ("Hermano:", hermano2)
print ("Hermana:", hermana1)
print ("Hermana:", hermana2)

# Crear tuplas de frutas, vegetales y productos animales
frutas = ("manzana", "plátano", "naranja")
vegetales = ("zanahoria", "lechuga", "espinaca")
productos_animales = ("leche", "queso", "huevo")

# Unir las tres tuplas y asignarlas a una variable llamada food_stuff_tp
food_stuff_tp = frutas + vegetales + productos_animales
print("Tupla de alimentos (food_stuff_tp):", food_stuff_tp)

# Cambiar la tupla food_stuff_tp a una lista llamada food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print("Lista de alimentos (food_stuff_lt):", food_stuff_lt)

# Extraer el elemento o elementos del medio de la lista
indice_medio = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    elementos_medios = food_stuff_lt[indice_medio - 1:indice_medio + 1]
else:
    elementos_medios = [food_stuff_lt[indice_medio]]
print("Elemento(s) del medio:", elementos_medios)

# Extraer los primeros tres y los últimos tres elementos de la lista
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print("Primeros tres:", primeros_tres)
print("Últimos tres:", ultimos_tres)

# Eliminar completamente la tupla food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Esto daría error porque la tupla fue eliminada

# Verificar si un elemento existe en una tupla
paises_nordicos = ("Dinamarca", "Finlandia", "Islandia", "Noruega", "Suecia")
print("¿Estonia es un país nórdico?", "Estonia" in paises_nordicos)
