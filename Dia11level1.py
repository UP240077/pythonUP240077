def sumar_dos_numeros(a, b):
    return a + b

def area_del_circulo(radio):
    pi = 3.1416
    return pi * radio * radio

def sumar_todos(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números"

def convertir_celsius_a_fahrenheit(c):
    return (c * 9 / 5) + 32

def verificar_estacion(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    return 'Mes no válido'

def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def resolver_ecuacion_cuadratica(a, b, c):
    import cmath
    d = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(d)) / (2*a)
    raiz2 = (-b - cmath.sqrt(d)) / (2*a)
    return (raiz1, raiz2)

def imprimir_lista(lista):
    for item in lista:
        print(item)

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

def capitalizar_items_lista(lista):
    return [item.capitalize() for item in lista]

def agregar_item(lista, item):
    lista.append(item)
    return lista

def eliminar_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

def suma_de_numeros(numero):
    return sum(range(numero + 1))

def suma_de_impares(numero):
    return sum(i for i in range(numero + 1) if i % 2 != 0)

def suma_de_pares(numero):
    return sum(i for i in range(numero + 1) if i % 2 == 0)
