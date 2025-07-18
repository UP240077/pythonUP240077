# Definimos el conjunto de empresas de tecnología
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Mostrar la longitud del conjunto
print("1. Longitud del conjunto:", len(it_companies))

# Agregar 'Twitter' al conjunto
it_companies.add('Twitter')
print("2. Después de agregar 'Twitter':", it_companies)

# Insertar múltiples empresas 
more_companies = {'Spotify', 'Tesla', 'Intel'}
it_companies.update(more_companies)
print("3. Después de agregar varias empresas:", it_companies)

# Eliminar una empresa del conjunto
it_companies.remove('IBM') 
print("4. Después de eliminar 'IBM':", it_companies)

# Diferencia entre remove y discard
# remove lanza error si el elemento no existe
try:
    it_companies.remove('Netflix')  # 'Netflix' no está, dará error
except KeyError:
    print("5. Error: 'Netflix' no se puede eliminar con remove porque no está en el conjunto")

# discard NO lanza error si el elemento no existe
it_companies.discard('Netflix')  # No hace nada si no existe
print("5. Después de usar discard con 'Netflix':", it_companies)

print("""
Diferencia entre remove y discard:
- remove(): elimina un elemento, pero lanza un error si no existe.
- discard(): elimina un elemento, pero NO lanza error si no existe.
""")
