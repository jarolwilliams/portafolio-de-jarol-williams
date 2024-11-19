# 1. Conversión de Pesos Dominicanos a Dólares*

tasa_cambio = float(input("Ingrese la tasa de cambio de 1 dólar en pesos dominicanos: "))
pesos = float(input("Ingrese la cantidad en pesos dominicanos: "))
dolares = pesos / tasa_cambio
print(pesos, "pesos dominicanos son equivalentes a", dolares, "dólares.")


# 2. Promedio de Notas*

cantidad_notas = int(input("¿Cuántas notas deseas ingresar?: "))
suma = 0

for i in range(cantidad_notas):
    nota = float(input("Ingresa la nota: "))
    suma += nota

promedio = suma / cantidad_notas
print("El promedio de las notas es:", promedio)

# 3. Operaciones Matemáticas Básicas*

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)

if num2 != 0:
    print("División:", num1 / num2)
else:
    print("No se puede dividir entre cero.")


# 4. Conversión de Fahrenheit a Celsius*

fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, "°F equivalen a", celsius, "°C.")


# 5. Conversión de Metros a Pulgadas*

metros = float(input("Ingrese la cantidad en metros: "))
pulgadas = metros * 39.3701
print(metros, "metros equivalen a", pulgadas, "pulgadas.")

