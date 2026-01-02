# ejercicios dia 1
# ejercicio 1
nombre = "Freddy"
edad = "37 años"
profecion = "Director"
Saludo = f"Hola, mi nombre es {nombre}, tengo {edad} y trabajo como {profecion}"
print(Saludo)

# ejercicio 2
cafe = "El cafe es una bebida muy aromatica"
print(cafe.upper())
print(cafe.lower())
len(cafe)
print(len(cafe))
print("muy" in cafe)

# ejercicio 3
etiqueta = "  Cafe de especialidad -   TOSTADO MEDIO  "
# print(etiqueta.lstrip().rstrip())
print(etiqueta.lower())
print(' '.join(etiqueta.split()).title())

presentacion = "nombre: Freddy \nedad: 37 \nprofecion: Barista"
print(presentacion)

# ejercicio 4
producto1 = "Doppio"
len(producto1)
print(f"El producto {producto1.upper()} tiene {len(producto1)} caracteres")

# ejercicios dia 2
# ejercicio 1
nombre = "Freddy"
apellido = "Gonzalez"
edad = 37
ciudad = "Buenos Aires"
print(
    f"Hola, mi nombre es {nombre} {apellido}. \nTengo {edad} anos de edad y vivo en {ciudad}.")


# ejercicio 2
mensaje = "Aprender Python lleva tiempo y practica"
print(len(mensaje))
print(mensaje.count('a'))


# ejercicio 3

texto = "   Cafe de Especialidad   "
print(texto.strip().lower())


# Ejercicio 4
frase = "Me gusta el cafe con leche"
print(frase.replace('cafe', 'Café'))


# Ejercicio 5
descripcion = "curso incicial de python para principiantes"
print("python" in descripcion)


# ejercicio 6
linea = "=" * 30 + "\n    EJERCICIOS COMPLETADOS\n" + "=" * 30
print(linea)


# ejercicio 7
nombre_completo = "freddy gonzalez"
print(nombre_completo.title())

# ejercicio 8
texto2 = """El curso de python es excelete 
para quienes quieren quieren aprender conceptos 
basicos de programacion con un 
lenguaje de alto nivel"""
print(texto2)
