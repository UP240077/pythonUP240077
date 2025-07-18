# Ejercicios Día 13 - Soluciones completas

# Filtrar números negativos y ceros usando list comprehension
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numeros if n <= 0]
print("1. Números negativos y ceros:", negativos_y_ceros)

# Aplanar lista de listas de listas a lista 
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublista1 in lista_de_listas for sublista2 in sublista1 for num in sublista2]
print("2. Lista aplanada:", lista_aplanada)

# Crear lista de tuplas con potencias usando list 
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("3. Lista de tuplas con potencias:")
for t in tuplas:
    print(t)

# Aplanar lista y convertir países y ciudades a formato requerido
paises = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
nuevo_formato = [[
    pais.upper(),
    pais[:3].upper(),
    ciudad.upper()
] for [[pais, ciudad]] in paises]
print("4. Nuevo formato de países y ciudades:", nuevo_formato)

# Convertir lista a lista de diccionarios con llaves 'país' y 'ciudad'
lista_diccionarios = [{'país': pais.upper(), 'ciudad': ciudad.upper()} for [[pais, ciudad]] in paises]
print("5. Lista de diccionarios:")
for dic in lista_diccionarios:
    print(dic)

# Concatenar nombres y apellidos 
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for [[nombre, apellido]] in nombres]
print("6. Nombres completos concatenados:", nombres_completos)

# Pendiente entre dos puntos 
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# Intersección con eje y dado un punto (x, y) y pendiente m
interseccion = lambda x, y, m: y - m * x

# Ejemplo de uso
x1, y1 = 1, 2
x2, y2 = 3, 6
m = pendiente(x1, y1, x2, y2)
b = interseccion(x1, y1, m)

print(f"7. Pendiente calculada: {m}")
print(f"   Intersección con eje y: {b}")
