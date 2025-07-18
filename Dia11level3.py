def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def items_unicos(lista):
    return len(lista) == len(set(lista))

def mismo_tipo(lista):
    tipo = type(lista[0])
    return all(isinstance(i, tipo) for i in lista)

def variable_valida(nombre):
    return nombre.isidentifier()

# Asume que countries_data es una lista de diccionarios
from collections import Counter

def idiomas_mas_hablados(data, top=10):
    contador = Counter()
    for pais in data:
        contador.update(pais['languages'])
    return contador.most_common(top)

def paises_mas_poblados(data, top=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:top]
