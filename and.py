# Función que representa la compuerta AND
def and_gate(a, b):
    return a and b

# Imprimir encabezados de la tabla
print("A\tB\tA AND B")
print("--------------------")

# Generar la tabla de verdad
for a in [0, 1]:
    for b in [0, 1]:
        resultado = and_gate(a, b)
        print(f"{a}\t{b}\t{resultado}")
