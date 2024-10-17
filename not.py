# Función que representa la compuerta NOT
def not_gate(a):
    return not a

# Imprimir encabezados de la tabla
print("A\tNOT A")
print("--------------------")

# Generar la tabla de verdad
for a in [0, 1]:
    resultado = not_gate(a)
    print(f"{a}\t{int(resultado)}")
