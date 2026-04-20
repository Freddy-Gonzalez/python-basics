numero = input("Ingrese número del 1 al 10: ").strip()
while not numero.isdigit() or int(numero) < 1 or int(numero) > 10:
    numero = input("Número inválido. Ingrese un número del 1 al 10: ").strip()

print(f"Número aceptado: {numero}")
