import random
import string

# Nivel 1

def generar_id_usuario():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(generar_id_usuario())  # Ejemplo: '1ee33d'


def generar_ids_por_usuario():
    num_caracteres = int(input("¿Cuántos caracteres por ID?: "))
    num_ids = int(input("¿Cuántos IDs generar?: "))
    for _ in range(num_ids):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=num_caracteres)))

# generar_ids_por_usuario()


def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(generar_color_rgb())  # Ejemplo: rgb(125,244,255)

# Nivel 2

def lista_colores_hexadecimal(cantidad):
    colores = []
    for _ in range(cantidad):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

print(lista_colores_hexadecimal(3))


def lista_colores_rgb(cantidad):
    return [generar_color_rgb() for _ in range(cantidad)]

print(lista_colores_rgb(3))


def generar_colores(tipo, cantidad):
    if tipo == 'hexa':
        return lista_colores_hexadecimal(cantidad)
    elif tipo == 'rgb':
        return lista_colores_rgb(cantidad)
    else:
        return "Tipo no válido. Usa 'hexa' o 'rgb'."

print(generar_colores('hexa', 3))
print(generar_colores('rgb', 3))

# Nivel 3

def mezclar_lista(lista):
    copia = lista[:]
    random.shuffle(copia)
    return copia

print(mezclar_lista([1, 2, 3, 4, 5]))


def numeros_aleatorios_unicos():
    return random.sample(range(10), 7)

print(numeros_aleatorios_unicos())
