# Función que representa la implicación A => B
def implication(a, b):
    return (not a) or b

# Imprimir encabezados de la tabla
print("A\tB\tA => B")
print("--------------------")

# Generar la tabla de verdad
for a in [0, 1]:
    for b in [0, 1]:
        resultado = implication(a, b)
        print(f"{a}\t{b}\t{int(resultado)}")
