# Crear un diccionario vacío llamado perro
perro = {}

# Agregar nombre, color, raza, patas y edad al diccionario
perro['nombre'] = 'Fido'
perro['color'] = 'Café'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 5

print("1-2. Diccionario 'perro':", perro)

# Crear un diccionario llamado estudiante con varias claves
estudiante = {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'género': 'Masculino',
    'edad': 21,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'HTML'],
    'país': 'México',
    'ciudad': 'CDMX',
    'dirección': 'Av. Universidad 3000'
}

# Obtener la longitud del diccionario estudiante
print("3-4. Longitud del diccionario 'estudiante':", len(estudiante))

# Obtener el valor de 'habilidades' y verificar su tipo de dato
valor_habilidades = estudiante['habilidades']
print("5. Valor de 'habilidades':", valor_habilidades)
print("5. Tipo de dato de 'habilidades':", type(valor_habilidades))

# Agregar una o dos habilidades más
estudiante['habilidades'].append('CSS')
estudiante['habilidades'].append('JavaScript')
print("6. Habilidades actualizadas:", estudiante['habilidades'])

# Obtener las claves del diccionario como lista
claves = list(estudiante.keys())
print("7. Claves del diccionario:", claves)

# Obtener los valores del diccionario como lista
valores = list(estudiante.values())
print("8. Valores del diccionario:", valores)

#  Convertir el diccionario a una lista de tuplas usando items()
tuplas = list(estudiante.items())
print("9. Diccionario convertido a lista de tuplas:", tuplas)

# Eliminar uno de los elementos del diccionario
del estudiante['estado_civil']
print("10. Después de eliminar 'estado_civil':", estudiante)

# Eliminar el diccionario completo
del estudiante

# Verificar si el diccionario fue eliminado
try:
    print(estudiante)
except NameError:
    print("11. El diccionario 'estudiante' ha sido eliminado.")
