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
