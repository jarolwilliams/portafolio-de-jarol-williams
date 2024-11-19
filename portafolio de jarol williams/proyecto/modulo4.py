# 1. Programa para guardar una lista de compras y calcular el precio total:

lista_compras = {}

while True:
    producto = input("Ingrese el nombre del producto (o 'salir' para finalizar): ").strip()
    if producto.lower() == "salir":
        break
    if producto in lista_compras:
        print("El producto ya está en la lista.")
        continue
    try:
        precio = float(input(f"Ingrese el precio de {producto}: "))
        lista_compras[producto] = precio
    except ValueError:
        print("Por favor, ingrese un número válido para el precio.")

total = sum(lista_compras.values())
print("\nLista de compras:")
for producto, precio in lista_compras.items():
    print(f"- {producto}: ${precio:.2f}")
print(f"Precio total: ${total:.2f}")

# 2. Programa que analiza una palabra y cuenta letras y consonantes:

palabra = input("Ingrese una palabra: ").strip().lower()
vocales = "aeiouáéíóú"
letras = len(palabra)
consonantes = sum(1 for letra in palabra if letra.isalpha() and letra not in vocales)

print(f"La palabra '{palabra}' tiene {letras} letras en total.")
print(f"De esas, {consonantes} son consonantes.")

# 3. Programa que guarda nombres y los organiza por tamaño:

nombres = []

while True:
    nombre = input("Ingrese un nombre (o 'salir' para finalizar): ").strip()
    if nombre.lower() == "salir":
        break
    nombres.append(nombre)

nombres_ordenados = sorted(nombres, key=len)

print("\nNombres ordenados por tamaño:")
for nombre in nombres_ordenados:
    print(nombre)

# 4. Programa que guarda nombres evitando duplicados:

nombres = set()

while True:
    nombre = input("Ingrese un nombre (o 'salir' para finalizar): ").strip()
    if nombre.lower() == "salir":
        break
    if nombre in nombres:
        print("El nombre ya existe en la lista. Intente con otro.")
    else:
        nombres.add(nombre)

print("\nLista de nombres únicos:")
for nombre in nombres:
    print(nombre)
