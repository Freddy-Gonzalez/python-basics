producto = input("Ingrese un producto: ").strip().upper()
producto_sin_espacios = len(producto.replace(" ", ""))
validar = bool(producto)

print(f"""
      Producto: {producto}
      Caracteres (sin espacios): {producto_sin_espacios}
      Texto válido: {validar}
      """)
