# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

print("Por favor, ingrese a continuacion 3 palabras diferentes:") 


palabra_1 = str(input('Ingrese la primer palabra:\n'))
palabra_2 = str(input('Ingrese la segunda palabra:\n'))
palabra_3 = str(input('Ingrese la tercer palabra:\n'))

print("Por favor, seleccione a continuacion la opcion deseada:"
"\nSi desea ordenar las palabras ingresadas alfabeticamente, ingrese '1'"
"\nSi desea ordenar las palabras ingresadas por cantidad de letras, ingrese '2'")

ingreso = int(input('Ingrese 1 o 2:\n')) # Deberia poner una funcion que me haga repetir la funcion de ingreso en el caso de no poner 1 o 2. supongo que una especie de bucle.

if ingreso == 1:
    if palabra_1 > palabra_2 and palabra_1 > palabra_3 and palabra_2 > palabra_3:
        print(f"La palabra: {palabra_1} es la mayor en orden alfabetico. La palabra: {palabra_2} es la segunda, mientras que la palabra: {palabra_3} es la menor")
    elif palabra_1 > palabra_2 and palabra_1 > palabra_3 and palabra_2 < palabra_3:
            print(f"La palabra: {palabra_1} es la mayor en orden alfabetico. La palabra: {palabra_3} es la segunda, mientras que la palabra: {palabra_2} es la menor")

    elif palabra_1 < palabra_2 and palabra_2 > palabra_3 and palabra_1 > palabra_3:
        print(f"La palabra: {palabra_2} es la mayor en orden alfabetico. La palabra: {palabra_1} es la segunda, mientras que la palabra: {palabra_3} es la menor")
    elif palabra_1 < palabra_2 and palabra_2 > palabra_3 and palabra_1 < palabra_3:
        print(f"La palabra: {palabra_2} es la mayor en orden alfabetico. La palabra: {palabra_3} es la segunda, mientras que la palabra: {palabra_1} es la menor")

    elif palabra_1 < palabra_3 and palabra_2 < palabra_3 and palabra_1 > palabra_2:
        print(f"La palabra: {palabra_3} es la mayor en orden alfabetico. La palabra: {palabra_1} es la segunda, mientras que la palabra: {palabra_2} es la menor")
    elif palabra_1 < palabra_3 and palabra_2 < palabra_3 and palabra_1 < palabra_2:
        print(f"La palabra: {palabra_3} es la mayor en orden alfabetico. La palabra: {palabra_2} es la segunda, mientras que la palabra: {palabra_1} es la menor")

elif ingreso == 2:
    if len(palabra_1) == len(palabra_2) and len(palabra_1) == len(palabra_3):
        print(f"Las 3 palabras ingresadas tienen la misma cantidad de letras")

    elif len(palabra_1) == len(palabra_2) and len(palabra_1) > len(palabra_3):
        print(f"La palabra: {palabra_1} es la mayor en cantidad de letras junto con la palabra: {palabra_2}, mientras que la palabra:{palabra_3} es la menor")
    
    elif len(palabra_1) == len(palabra_3) and len(palabra_1) > len(palabra_2):
        print(f"La palabra: {palabra_1} es la mayor en cantidad de letras junto con la palabra: {palabra_3}, mientras que la palabra:{palabra_2} es la menor")

    elif len(palabra_2) == len(palabra_3) and len(palabra_2) > len(palabra_1):
        print(f"La palabra: {palabra_2} es la mayor en cantidad de letras junto con la palabra: {palabra_3}, mientras que la palabra:{palabra_1} es la menor")

    elif len(palabra_1) == len(palabra_2) and len(palabra_1) < len(palabra_3):
        print(f"La palabra: {palabra_3} es la mayor en cantidad de letras. Mientras que la palabra:{palabra_1} y {palabra_2} son las menores")

    elif len(palabra_1) == len(palabra_3) and len(palabra_1) < len(palabra_2):
        print(f"La palabra: {palabra_2} es la mayor en cantidad de letras. Mientras que la palabra:{palabra_1} y {palabra_3} son las menores")

    elif len(palabra_2) == len(palabra_3) and len(palabra_1) > len(palabra_2):
        print(f"La palabra: {palabra_1} es la mayor en cantidad de letras. Mientras que la palabra:{palabra_2} y {palabra_3} son las menores")


    if len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_2) > len(palabra_3):
        print(f"La palabra: {palabra_1} es la mayor en cantidad de letras. La palabra: {palabra_2} es la segunda, mientras que la palabra:{palabra_3} es la menor")
    elif len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_2) < len(palabra_3):
        print(f"La palabra: {palabra_1} es la mayor en cantidad de letras. La palabra: {palabra_3} es la segunda, mientras que la palabra:{palabra_2} es la menor")

    if len(palabra_1) < len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_2) > len(palabra_3):
        print(f"La palabra: {palabra_2} es la mayor en cantidad de letras. La palabra: {palabra_1} es la segunda, mientras que la palabra:{palabra_3} es la menor")
    elif len(palabra_1) < len(palabra_2) and len(palabra_1) < len(palabra_3) and len(palabra_2) > len(palabra_3):
        print(f"La palabra: {palabra_2} es la mayor en cantidad de letras. La palabra: {palabra_3} es la segunda, mientras que la palabra:{palabra_1} es la menor")

    if len(palabra_1) > len(palabra_2) and len(palabra_1) < len(palabra_3) and len(palabra_2) < len(palabra_3):
        print(f"La palabra: {palabra_3} es la mayor en cantidad de letras. La palabra: {palabra_1} es la segunda, mientras que la palabra:{palabra_2} es la menor")
    elif len(palabra_1) < len(palabra_2) and len(palabra_1) < len(palabra_3) and len(palabra_2) < len(palabra_3):
        print(f"La palabra: {palabra_3} es la mayor en cantidad de letras. La palabra: {palabra_2} es la segunda, mientras que la palabra:{palabra_1} es la menor")

else:
    print("Por favor, reinice el programa y solo ingrese la opcion 1 o 2. Todavia este programa no sabe hacer un bucle")
