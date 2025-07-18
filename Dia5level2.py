# Lista de edades
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista
edades.sort()
print("Edades ordenadas:", edades)

# Encontrar la edad mínima y máxima
edad_min = min(edades)
edad_max = max(edades)
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)

# Agregar de nuevo la edad mínima y máxima a la lista
edades.extend([edad_min, edad_max])
print("Lista con edades mín. y máx. agregadas:", edades)

# Ordenar de nuevo (porque agregamos nuevos elementos)
edades.sort()

# Encontrar la mediana (valor del medio)
longitud = len(edades)
if longitud % 2 == 0:
    mediana = (edades[longitud//2 - 1] + edades[longitud//2]) / 2
else:
    mediana = edades[longitud//2]
print("Mediana:", mediana)

# Promedio (media)
promedio = sum(edades) / len(edades)
print("Promedio:", promedio)

# Rango (máximo - mínimo)
rango = edad_max - edad_min
print("Rango:", rango)

# Comparar el valor absoluto de (mínimo - promedio) y (máximo - promedio)
diff_min = abs(edad_min - promedio)
