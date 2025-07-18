def pares_e_impares(numero):
    pares = sum(1 for i in range(numero + 1) if i % 2 == 0)
    impares = numero + 1 - pares
    return f"Números pares: {pares}, Números impares: {impares}"

def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def esta_vacio(valor):
    return valor == '' or valor == [] or valor == {} or valor is None

def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    medio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    return lista_ordenada[medio]

def calcular_moda(lista):
    from collections import Counter
    conteo = Counter(lista)
    return conteo.most_common(1)[0][0]

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    media = calcular_media(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def calcular_desviacion_estandar(lista):
    import math
    return math.sqrt(calcular_varianza(lista))
