# Asignar calificaciones según puntajes
puntaje = int(input("Ingresa tu puntaje (0-100): "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje < 80:
    print("Calificación: B")
elif 60 <= puntaje < 70:
    print("Calificación: C")
elif 50 <= puntaje < 60:
    print("Calificación: D")
elif 0 <= puntaje < 50:
    print("Calificación: F")
else:
    print("Puntaje inválido")

# Verificar estación según el mes
mes = input("Ingresa el nombre de un mes: ").strip().capitalize()

if mes in ['Septiembre', 'Octubre', 'Noviembre']:
    print("Estación: Otoño ")
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    print("Estación: Invierno ")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("Estación: Primavera ")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("Estación: Verano ")
else:
    print("Mes no válido")

# Verificar si una fruta ya está en la lista
frutas = ['banana', 'naranja', 'mango', 'limón']
nueva_fruta = input("Ingresa el nombre de una fruta: ").strip().lower()

if nueva_fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(nueva_fruta)
    print("Lista actualizada de frutas:", frutas)
