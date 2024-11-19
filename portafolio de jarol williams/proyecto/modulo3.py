# 1. Números Primos del 1 al 100

print("Números primos del 1 al 100:")

for num in range(2, 101):  # Comienza en 2, porque 1 no es primo
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")


# 2. Tabla de Multiplicar de un Número

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# 3. Descomponer una Oración por Letras

oracion = input("Ingrese una oración: ")

print("Letras de la oración:")
for letra in oracion:
    print(letra)


# 4. Programa que Solo Se Cierra al Tercer Intento

intentos = 0

while intentos < 3:
    clave = input("Ingrese la contraseña para cerrar el programa: ")
    if clave == "salir":
        print("¡Programa cerrado!")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos}/3.")

if intentos == 3:
    print("Ha superado el número máximo de intentos. Programa cerrado.")


# 5. Serie Fibonacci

n = int(input("¿Cuántos términos de la serie Fibonacci deseas mostrar?: "))

a, b = 0, 1
print("Serie Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

