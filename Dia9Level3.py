# Diccionario persona
persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'esta_casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Space street',
        'codigo_postal': '02210'
    }
}

# Verificar si existe la clave 'habilidades' y mostrar la habilidad del medio
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    longitud = len(habilidades)
    habilidad_media = habilidades[longitud // 2]  # índice central
    print("1. La habilidad del medio es:", habilidad_media)
else:
    print("1. No tiene la clave 'habilidades'")

# Verificar si tiene la habilidad 'Python'
if 'habilidades' in persona:
    if 'Python' in persona['habilidades']:
        print("2. La persona tiene la habilidad Python.")
    else:
        print("2. La persona no tiene la habilidad Python.")
else:
    print("2. No tiene la clave 'habilidades'")

# Evaluar el tipo de desarrollador según sus habilidades
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    front_end = {'JavaScript', 'React'}
    back_end = {'Node', 'Python', 'MongoDB'}
    full_stack = {'React', 'Node', 'MongoDB'}

    habilidades_set = set(habilidades)

    if habilidades_set == front_end:
        print("3. Es un desarrollador frontend.")
    elif back_end.issubset(habilidades_set):
        print("3. Es un desarrollador backend.")
    elif full_stack.issubset(habilidades_set):
        print("3. Es un desarrollador fullstack.")
    else:
        print("3. Título desconocido.")
else:
    print("3. No tiene la clave 'habilidades'")

# 4. Verificar si está casado y vive en Finlandia para imprimir la frase
if persona.get('esta_casado') and persona.get('pais') == 'Finlandia':
    print(f"4. {persona['nombre']} {persona['apellido']} vive en Finlandia. Está casado.")
else:
    print("4. No cumple las condiciones de estado civil y país.")
