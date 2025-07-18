# Definimos dos conjuntos de ejemplo
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unir A y B (Unión)
union_ab = A.union(B)
print("1. Unión de A y B:", union_ab)

# Intersección de A y B
interseccion_ab = A.intersection(B)
print("2. Intersección de A y B:", interseccion_ab)

# ¿Es A un subconjunto de B?
es_subconjunto = A.issubset(B)
print("3. ¿A es subconjunto de B?:", es_subconjunto)

# ¿Son A y B conjuntos disjuntos?
son_disjuntos = A.isdisjoint(B)
print("4. ¿A y B son disjuntos (no comparten elementos)?:", son_disjuntos)

# Unir A con B y B con A (la unión es conmutativa)
a_union_b = A.union(B)
b_union_a = B.union(A)
print("5. A unido con B:", a_union_b)
print("5. B unido con A:", b_union_a)

# Diferencia simétrica entre A y B (elementos que están en uno u otro, pero no en ambos)
diferencia_simetrica = A.symmetric_difference(B)
print("6. Diferencia simétrica entre A y B:", diferencia_simetrica)

# Eliminar completamente los conjuntos
del A
del B

# Verificar que han sido eliminados
try:
    print(A)
except NameError:
    print("7. El conjunto A ha sido eliminado.")

try:
    print(B)
except NameError:
    print("7. El conjunto B ha sido eliminado.")
