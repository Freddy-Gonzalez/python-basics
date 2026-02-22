marca = input("Ingrese marca: ").strip().upper()
modelo = input("Ingrese modelo: ").strip().upper()
partes = [marca, modelo]
producto = " ".join(partes)

print(f"Producto: {producto}")
