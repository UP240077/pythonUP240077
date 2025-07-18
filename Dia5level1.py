# Declarar una lista vacía de super
lista_vacia = []

# Declarar una lista con más de 5 elementos
mi_lista = ["manzana', 'banana', 'naranja', 'pera', 'uva', 'kiwi"]

# Longitud de la lista
print(len(mi_lista))  # 6

# Obtener el primer, el medio y el último elemento
print("Primero:", mi_lista[0])              # manzana
print("Medio:", mi_lista[len(mi_lista)//2]) # naranja
print("Último:", mi_lista[-1])              # kiwi

# Lista con datos mixtos
datos_mixtos = ['Angel', 18, 1.70, 'Soltero', 'Santa Anita']

# Declarar lista de empresas tecnológicas
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Imprimir la lista
print(it_companies)

# Número de empresas en la lista
print("Cantidad de empresas:", len(it_companies))

#Primera, del medio y última empresa
print("Primera:", it_companies[0])
print("Medio:", it_companies[len(it_companies)//2])
print("Última:", it_companies[-1])

# Modificar una de las empresas
it_companies[1] = 'Meta'
print("Lista modificada:", it_companies)

# Agregar una nueva empresa
it_companies.append('Tesla')
print("Después de agregar:", it_companies)

# Insertar una empresa en el medio
it_companies.insert(len(it_companies)//2, 'Spotify')
print("Después de insertar en medio:", it_companies)

# Cambiar una empresa a mayúsculas (excepto IBM)
for i in range(len(it_companies)):
    if it_companies[i].lower() != 'ibm':
        it_companies[i] = it_companies[i].upper()
print("Nombres en mayúsculas:", it_companies)

# Unir con '#; '
print("#; ".join(it_companies))

# Verificar si una empresa está en la lista
print("¿GOOGLE está en la lista?:", 'GOOGLE' in it_companies)

# Ordenar la lista
it_companies.sort()
print("Ordenada:", it_companies)

# Revertir (orden descendente)
it_companies.reverse()
print("Reversa:", it_companies)

# Cortar las primeras 3 empresas
print("Primeras 3:", it_companies[:3])

# Cortar las últimas 3 empresas
print("Últimas 3:", it_companies[-3:])

# Cortar las del medio
medio = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Empresas del medio:", it_companies[medio-1:medio+1])
else:
    print("Empresa del medio:", it_companies[medio])

# Eliminar la primera empresa
it_companies.pop(0)
print("Sin la primera empresa:", it_companies)

# Eliminar del medio
medio = len(it_companies) // 2
it_companies.pop(medio)
print("Sin empresa del medio:", it_companies)

# Eliminar la última empresa
it_companies.pop()
print("Sin última empresa:", it_companies)

# Eliminar todas las empresas
it_companies.clear()
print("Lista vacía:", it_companies)

# Eliminar la lista completamente
del it_companies

# Unir dos listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# Insertar Python y SQL después de Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

print("Full Stack Final:", full_stack)
