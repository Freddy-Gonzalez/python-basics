animal = "  perRo gordo     "
print(animal.upper())  # .upper convierte a mayusculas
print(animal.lower())  # .lower convierte a minusculas
# .capitalize convierte primer caracter en mayusculas y el resto a minusculas
print(animal.capitalize())
# .title convierte primer caracter de cada palabra a mayusculas
print(animal.title())
print(animal.strip())  # .strip elimina espacios innecesarios
print(animal.strip().capitalize())  # como unir metodos
print(animal.rstrip())  # elimina espacios a la derecha
print(animal.lstrip())  # elimina espacios a la izquierda
# busca cadena de caracteres y nos devuelve el indice. Si la cadena no existe ns devuelve "-1"
print(animal.find("pe"))
print(animal.replace("pe", "lol"))  # .replace remplaza caracteres
print("pe" in animal)  # in  devuelve boolean si es que lo encuentra
# not in  devuelve boolean si es que no se encuentra la cadena de caracteres mencionada dentro de "" en la variable
print("pe" not in animal)
