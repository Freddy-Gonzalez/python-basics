nombre = "Freddy"
edad = "37 años"
profecion = "Director"
Saludo = f"Hola, mi nombre es {nombre}, tengo {edad} y trabajo como {profecion}"
print(Saludo)


cafe = "El cafe es una bebida muy aromatica"
print(cafe.upper())
print(cafe.lower())
len(cafe)
print(len(cafe))
print("muy" in cafe)


etiqueta = "  Cafe de especialidad -   TOSTADO MEDIO  "
# print(etiqueta.lstrip().rstrip())
print(etiqueta.lower())
print(' '.join(etiqueta.split()).title())

presentacion = "nombre: Freddy \nedad: 37 \nprofecion: Barista"
print(presentacion)


producto1 = "Doppio"
len(producto1)
print(f"El producto {producto1.upper()} tiene {len(producto1)} caracteres")
