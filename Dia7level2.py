# Definimos dos conjuntos de ejemplo
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#  Unir A y B (Union)
union_ab = A.union(B)
print("1. Unión de A y B:", union_ab)

# Intersección de A y B
intersection_ab = A.intersection(B)
print("2. Intersección de A y B:", intersection_ab)

# ¿A es subconjunto de B?
is_subset = A.issubset(B)
print("3. ¿A es subconjunto de B?:", is_subset)

# ¿A y B son conjuntos disjuntos?
are_disjoint = A.isdisjoint(B)
print("4. ¿A y B son disjuntos?:", are_disjoint)

# Unir A con B y B con A (esto es lo mismo: unión)
a_union_b = A.union(B)
b_union_a = B.union(A)
print("5. A unido con B:", a_union_b)
print("5. B unido con A:", b_union_a)

# Diferencia simétrica entre A y B
symmetric_diff = A.symmetric_difference(B)
print("6. Diferencia simétrica entre A y B:", symmetric_diff)

# Eliminar completamente los conjuntos
del A
del B

# Confirmamos que han sido eliminados
try:
    print(A)
except NameError:
    print("7. El conjunto A ha sido eliminado")

try:
    print(B)
except NameError:
    print("7. El conjunto B ha sido eliminado")
