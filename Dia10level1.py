# Iterar de 0 a 10 con for loop
for i in range(11):
    print(i)

# Iterar de 0 a 10 con while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterar de 10 a 0 con for loop
for i in range(10, -1, -1):
    print(i)

# Iterar de 10 a 0 con while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# Triángulo de #
for i in range(1, 8):
    print("#" * i)

# Cuadro con nested loops
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

# Patrón de multiplicación
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterar sobre lista de tecnologías
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

# Números pares del 0 al 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# Números impares del 0 al 100
for i in range(101):
    if i % 2 != 0:
        print(i)
