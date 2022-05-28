# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print(f"{texto_1.capitalize()} es mayor alfabeticamente que {texto_2.capitalize()}")

elif texto_2 > texto_1:
    print(f"{texto_2.capitalize()} es mayor alfabeticamente que {texto_1.capitalize()}")

elif texto_1 == texto_2:
    print("Ambas palabras son iguales".capitalize())


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print(f"{texto_1.capitalize()} tiene mas letras que {texto_2.capitalize()}")

elif len(texto_2) > len(texto_1):
    print(f"{(texto_2).capitalize()} tiene mas letras que {(texto_1).capitalize()}")

elif len(texto_1) == len(texto_2):
    print("Ambas palabras tienen la misma cantidad de letras")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

texto_1_inicio = texto_1[0]

texto_2_inicio = texto_2[0]

if texto_1_inicio < texto_2_inicio:
    print(f"{texto_1_inicio.upper()} es menor alfabeticamente que {texto_2_inicio.upper()}")

elif not(texto_2_inicio < texto_1_inicio):
    print(f"{texto_2_inicio.upper()} es menor alfabeticamente que {texto_1_inicio.upper()}")

else:
    print("Ambas iniciales son iguales")


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print(f"{copia_texto_1.capitalize()} es igual a {texto_1.capitalize()}")

else:
    print("No son iguales")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(f"{copia_texto_1.capitalize()} es distinto a {texto_2.capitalize()}")

else:
    print(f"{copia_texto_1.capitalize()} es igual a {texto_2.capitalize()}")
