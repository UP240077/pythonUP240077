# Suma total del 0 al 100
total = 0
for i in range(101):
    total += i
print("La suma total es:", total)

# Suma de pares e impares
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("La suma de los pares es:", even_sum)
print("La suma de los impares es:", odd_sum)
