# Función que representa la compuerta OR
def or_gate(a, b):
    return a or b

# Imprimir encabezados de la tabla
print("A\tB\tA OR B")
print("--------------------")

# Generar la tabla de verdad
for a in [0, 1]:
    for b in [0, 1]:
        resultado = or_gate(a, b)
        print(f"{a}\t{b}\t{resultado}")
