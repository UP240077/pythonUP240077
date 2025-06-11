#Define tus variables, el dia de hoy vamos a ver variables. Conocidas como sumas
#Ejercicios, multiplicaciones, etc.

import math

edad= 18
mi_peso= 85
base_triangulo= 23
Altura_triangulo= 45

print ("Area: ", base_triangulo*Altura_triangulo)
Lado_A= 18
Lado_B= 24
Lado_C= 25
print ("El perimetro es de:", Lado_A+Lado_B+Lado_C)
#Ahora vamos a calcular el area y perimetro de un rectangulo
largo_rectangulo= 254
ancho_rectangulo= 345
print("Area del rectangulo", largo_rectangulo*ancho_rectangulo)
#Ahora calculamos su perimetro
print("Perimetro del triangulo:", 2*largo_rectangulo+ancho_rectangulo)
#Ahora vamos a calcular el radio de un circulo
radio_circulo= 25
print("El radio de un circulo es de:", 3.14*radio_circulo**2)
#ahora la circunferencia de el circulo
print("Circunferencia:", 2*3.14*radio_circulo)
prendiente_x= 2
pendiente_y= 2
pendiente_x2= 6
pendiente_y2= 10
print("La pendiente es: ", pendiente_y2-pendiente_y/ pendiente_x2-prendiente_x )
#Calcula la distancia euclidiana
distancia_eudiciana= math.sqrt (pendiente_x2-prendiente_x**2 +pendiente_y2-pendiente_y**2)

print("Distancia euclidiana es: ", distancia_eudiciana)
#lista de  python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [1, 2, 4]

# Comparar lista1 y lista2 usando and
comparacion_lista1_y_lista2 = (lista1[0] == lista2[0] and
                               lista1[1] == lista2[1] and
                               lista1[2] == lista2[2])

# Comparar lista1 y lista3 usando and
comparacion_lista1_y_lista3 = (lista1[0] == lista3[0] and
                               lista1[1] == lista3[1] and
                               lista1[2] == lista3[2])

print(f"Lista 1 y Lista 2 son iguales: {comparacion_lista1_y_lista2}")
print(f"Lista 1 y Lista 3 son iguales: {comparacion_lista1_y_lista3}")

#Usar el operador and para verificar si 'on'esta en python como en 'dragon'
print('on' in 'python' and 'on' in 'dragon')  # True

#Usar el operador in para verificar si 'jargon' está en la oración
oracion = 'yo creo que la operacion no esta jargon.'
print('jargon' in oracion)  # True

#No hay 'on' en ambas palabras 'dragon' y 'python' (negación de la afirmación anterior)
print(not ('on' in 'python' and 'on' in 'dragon'))  # False

#Obtener la longitud del texto 'python', convertir ese valor a flotante y luego a cadena
longitud = len('python')         
longitud_flotante = float(longitud)  # 6.0
longitud_cadena = str(longitud_flotante)
print(longitud_cadena)  # '6.0'

#Verificar si un número es par (los números pares son divisibles por 2 sin residuo)
numero = 4
es_par = numero % 2 == 0
print(es_par)  # True si es par

#Verificar si la división entera de 7 entre 3 es igual al valor entero de 2.7
print(7 // 3 == int(2.7))  # True (7 // 3 = 2, int(2.7) = 2)

#Verificar si el tipo de '10' es igual al tipo de 10
print(type('10') == type(10))  # False

#Verificar si int('9.8') es igual a 10
# Esto genera un error porque '9.8' no es un número entero válido.
try:
    print(int('9.8') == 10)  # ValueError
except ValueError as e:
    print("Error:", e)

#Script que pide al usuario ingresar horas y tarifa por hora, y calcula el pago
horas = 8
tarifa = 35
pago = horas * tarifa
print("Pago:", pago)

