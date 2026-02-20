producto = input("Ingrese un producto: ").strip()
producto_sin_espacios = producto.replace(" ", "")
caracteres = len(producto_sin_espacios)
es_valido = bool(producto)

print(f"""
      Producto: {producto.upper()}
      Caracteres: {caracteres}
      Es un texto válido?: {es_valido}
      """)
