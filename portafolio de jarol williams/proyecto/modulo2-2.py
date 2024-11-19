# *. Clasificación de Personas por Sueldo*

sueldo = float(input("Ingrese el sueldo de la persona: "))

if sueldo < 20000:
    print("El sueldo es bajo.")
elif 20000 <= sueldo <= 50000:
    print("El sueldo es medio.")
else:
    print("El sueldo es alto.")


# 2. Verificar si una Contraseña es Segura*

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and any(c.isdigit() for c in contraseña) and any(c.isupper() for c in contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")


# 3. Validar si una Persona Puede Obtener Visa*

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: "))
antecedentes = input("¿Tiene antecedentes penales? (si/no): ").lower()

if edad >= 18 and ingresos >= 2000 and antecedentes == "no":
    print("Usted puede obtener visa.")
else:
    print("Usted no cumple con los requisitos para obtener visa.")




# 4. Validar si un Número es Par o Impar*

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# 5. Validar Usuario y Contraseña*

usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario = input("Ingrese el usuario: ")
contraseña = input("Ingrese la contraseña: ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso permitido.")
else:
    print("Usuario o contraseña incorrectos.")

