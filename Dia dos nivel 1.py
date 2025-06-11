# Día 2: 30 días de programación en Python

# === Nivel 1 ===

# Declaraciones de variables
primer_nombre = "Angel"
apellido = "Correa"
nombre_completo = primer_nombre + ' ' + apellido
pais = 'México'
ciudad = 'Ciudad de México'
edad = 18
año = 2025
esta_casado = False
es_verdadero = True
luz_encendida = True

# Declaración de múltiples variables en una sola línea
lenguaje, comida_favorita, hobby = 'Python', 'Tacos', 'Leer'
#Nivel2 

# Verificar tipos de datos
print('Tipos de datos:')
print('primer_nombre:', type(primer_nombre))
print('apellido:', type(apellido))
print('nombre_completo:', type(nombre_completo))
print('pais:', type(pais))
print('ciudad:', type(ciudad))
print('edad:', type(edad))
print('año:', type(año))
print('esta_casado:', type(esta_casado))
print('es_verdadero:', type(es_verdadero))
print('luz_encendida:', type(luz_encendida))
print('lenguaje:', type(lenguaje))
print('comida_favorita:', type(comida_favorita))
print('hobby:', type(hobby))

# Longitud del primer nombre
print('\nLongitud del primer nombre:', len(primer_nombre))

# Comparar longitudes
print('¿El primer nombre es más largo que el apellido?', len(primer_nombre) > len(apellido))

# Declarar dos números
num_uno = 5
num_dos = 4

# Operaciones aritméticas
total = num_uno + num_dos
diff = num_uno - num_dos
producto = num_uno * num_dos
division = num_uno / num_dos
residuo = num_uno % num_dos
exp = num_uno ** num_dos
division_entera = num_uno // num_dos

print('\nOperaciones matemáticas:')
print('Suma:', total)
print('Resta:', diff)
print('Producto:', producto)
print('División:', division)
print('Residuo:', residuo)
print('Potencia:', exp)
print('División entera:', division_entera)

# Cálculos con círculo
radio = 30
pi = 3.14159

area_del_circulo = pi * radio ** 2
circunferencia_del_circulo = 2 * pi * radio

print('\nCálculos con radio fijo:')
print('Área del círculo:', area_del_circulo)
print('Circunferencia del círculo:', circunferencia_del_circulo)

# Solicitar radio al usuario
radio_usuario = float(input('\nIngresa un radio para calcular el área del círculo: '))
area_usuario = pi * radio_usuario ** 2
print('Área del círculo con radio ingresado:', area_usuario)

# Solicitar datos al usuario
nombre_usuario = input('\nIngresa tu primer nombre: ')
apellido_usuario = input('Ingresa tu apellido: ')
pais_usuario = input('Ingresa tu país: ')
edad_usuario = input('Ingresa tu edad: ')

print('\nInformación del usuario:')
print('Nombre:', nombre_usuario)
print('Apellido:', apellido_usuario)
print('País:', pais_usuario)
print('Edad:', edad_usuario)

# Palabras reservadas en Python
print('\nPalabras clave de Python:')
help('keywords')
