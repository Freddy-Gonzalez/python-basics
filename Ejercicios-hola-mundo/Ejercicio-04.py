nombre1 = input("Ingrese primer nombre: ")
nombre2 = input("Ingrese segundo nombre: ")
apellido1 = input("Ingrese primer apellido: ")
apellido2 = input("Ingrese segundo apellido: ")

nom1_format = nombre1.strip().capitalize()
nom2_format = nombre2.strip().capitalize()
ap1_format = apellido1.strip().capitalize()
ap2_format = apellido2.strip().capitalize()

print(f"{nom1_format} {nom2_format} {ap1_format} {ap2_format}")
