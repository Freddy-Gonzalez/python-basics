nombre = input("Ingrese su nombre: ").strip().upper()
apellido = input("Ingrese su apellido: ").strip().upper()
nombre_completo = " ".join([nombre, apellido])
print(nombre_completo)

sin_espacios = len(nombre_completo.replace(" ", ""))
print(f"Cantidad de caracteres (sin espacios) es: {sin_espacios}")
