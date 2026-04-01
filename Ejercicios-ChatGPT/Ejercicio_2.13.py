producto = input("Ingrese un producto: ").strip().upper()

if not producto:
    producto = input("Debes ingresar un producto válido: ").strip().upper()

print(f"Producto ingresado: {producto}")
