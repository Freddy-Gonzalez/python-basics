numero = ""
while not numero.isdigit():
    numero = input("Ingrese un número: ").strip()

print(f"El número ingresado es: {numero}")
