# Obtener la edad del usuario y evaluar si puede aprender a conducir
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Tienes edad suficiente para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Necesitas esperar {años_faltantes} año" + ("s" if años_faltantes > 1 else "") + " para aprender a conducir.")

# Comparar mi edad con la del usuario
mi_edad = 25  # Puedes cambiar esto según tu edad
tu_edad = int(input("¿Cuál es tu edad?: "))

if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    print(f"Eres {diferencia} año" + ("s" if diferencia > 1 else "") + " mayor que yo.")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    print(f"Soy {diferencia} año" + ("s" if diferencia > 1 else "") + " mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Comparar dos números introducidos por el usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
