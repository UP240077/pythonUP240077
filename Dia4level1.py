# Concatenaciones
cadena1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(cadena1)  # Thirty Days Of Python

cadena2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(cadena2)  # Coding For All

# Declarar una variable
empresa = "Coding For All"
print(empresa)  # Imprimir el valor

# Longitud de la cadena
print(len(empresa))  # Muestra la cantidad de caracteres

# Convertir a mayúsculas y minúsculas
print(empresa.upper())      # Todo en mayúsculas
print(empresa.lower())      # Todo en minúsculas
print(empresa.capitalize()) # Primera letra en mayúscula
print(empresa.title())      # Primera letra de cada palabra en mayúscula
print(empresa.swapcase())   # Invertir mayúsculas/minúsculas

# Cortar la primera palabra
print(empresa[7:])  # Cortar "Coding", muestra "For All"

# Verificar si contiene una palabra
print(empresa.find('Coding'))   # Devuelve 0 (posición)
print(empresa.index('Coding'))  # Devuelve 0 también
print('Coding' in empresa)      # True (está presente)

# Reemplazar texto
print(empresa.replace('Coding', 'Python'))  # Python For All
print('Python for Everyone'.replace('Everyone', 'All'))  # Python for All

# Separar (split)
print(empresa.split())  # ['Coding', 'For', 'All']
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(','))  # Separa en lista por comas

# Índices de caracteres
print(empresa[0])    # Primer carácter: 'C'
print(empresa[-1])   # Último carácter: 'l'
print(empresa[10])   # Carácter en índice 10: 'r'

# Crear acrónimos
frase1 = "Python para todos"
frase2 = 'Coding For All'
acronimo1 = ''.join([palabra[0] for palabra in frase1.split()]).upper()
acronimo2 = ''.join([palabra[0] for palabra in frase2.split()]).upper()
print(acronimo1)  # PFE
print(acronimo2)  # CFA

# Posición de letras
print(empresa.index('C'))  # 0
print(empresa.index('F'))  # 7
print('Codigo para toda la gente'.rfind('l'))  # 17

## Frase con 'because'
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))  # 31 (primera ocurrencia)
print(frase.rindex('because'))  # 47 (última ocurrencia)

# Cortar 'because because because'
inicio = frase.find('because')
fin = frase.rindex('because') + len('because')
print(frase[inicio:fin])  # because because because

# Verificar comienzos y finales
print(empresa.startswith('Coding'))  # True
print(empresa.endswith('coding'))    # False

# Eliminar espacios
cadena_con_espacios = '   Coding For All      '
print(cadena_con_espacios.strip())  # Elimina espacios al inicio y final

# Verificar identificadores válidos
print('30DaysOfPython'.isidentifier())       # False
print('thirty_days_of_python'.isidentifier())  # True

# Unir lista con símbolo #
librerías = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerías))  # Django # Flask # Bottle # Pyramid # Falcon

# Saltos de línea
print("Estoy disfrutando este reto.\nMe pregunto qué sigue.")

# Tabulaciones
print("Nombre\tEdad\tPaís\tCiudad\nAsabeneh\t250\tFinlandia\tHelsinki")

# Formato de cadena
radio = 10
área = 3.14 * radio ** 2
print(f"El área de un círculo con radio {radio} es {int(área)} metros cuadrados.")

# Operaciones matemáticas con formato
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # 2 decimales
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

