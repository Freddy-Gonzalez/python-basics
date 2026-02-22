nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
profesion = input("Ingrese su profesión: ")

partes1 = [nombre, apellido]
nombre_completo = " ".join(partes1)

partes2 = [nombre_completo, profesion]
datos = " - ".join(partes2)

print(datos)
