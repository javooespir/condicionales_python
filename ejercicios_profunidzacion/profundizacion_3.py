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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''



print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


# Punto 1

'3 METODOS para el punto 1 XQ SI'

print("Por favor, ingrese a continuacion 3 valores de temperatura:")

temp_1 = float(input('Ingrese el primer valor de temperatura:\n')) # Utilizo float, ya que normalmente la temperatura se utiliza con decimales
temp_2 = float(input('Ingrese el segundo valor de temperatura:\n'))
temp_3 = float(input('Ingrese el tercer valor de temperatura:\n'))

'''if temp_1 >= temp_2 and temp_1 >= temp_3:
    if temp_1 > temp_2 and temp_1 == temp_3:
        print(f"El valor {temp_1} es el valor máximo de temperatura ingresado junto con el tercer valor ingresado.")
    elif temp_1 == temp_2 and temp_1 > temp_3:
        print(f"El valor {temp_1} es el valor máximo de temperatura ingresado junto con el segundo valor ingresado.")
    elif temp_1 == temp_2 and temp_1 == temp_3:
        print("Los valores ingresados son iguales.")
    else:
        print(f"El valor {temp_1} es el valor máximo de temperatura ingresado.")

elif temp_1 <= temp_2 and temp_2 >= temp_3:
    if temp_1 < temp_2 and temp_2 == temp_3:
        print(f"El valor {temp_2} es el valor máximo de temperatura ingresado junto con el tercer valor ingresado.")
    elif temp_1 == temp_2 and temp_2 > temp_3:
        print(f"El valor {temp_2} es el valor máximo de temperatura ingresado junto con el primer valor ingresado.")
    elif temp_1 == temp_2 and temp_2 == temp_3:
        print("Los valores ingresados son iguales.")
    else:
        print(f"El valor {temp_2} es el valor máximo de temperatura ingresado.")

elif temp_1 <= temp_3 and temp_2 <= temp_3:
    if temp_1 < temp_3 and temp_2 == temp_3:
        print(f"El valor {temp_3} es el valor máximo de temperatura ingresado junto con el segundo valor ingresado.")
    elif temp_1 == temp_3 and temp_2 < temp_3:
        print(f"El valor {temp_3} es el valor máximo de temperatura ingresado junto con el primer valor ingresado.")
    elif temp_1 == temp_2 and temp_2 == temp_3:
        print("Los valores ingresados son iguales.")
    else:
        print(f"El valor {temp_3} es el valor máximo de temperatura ingresado.")'''  
# Este metodo es el mas largo pero toma en cuenta todas las variables ingresadas con sus posibilidades por separado.

# 2do metodo mas eficiente
if temp_1 > temp_2 and temp_1 > temp_3:
    print(f"El valor {temp_1}º es la temperatura máxima ingresada.")
elif temp_1 < temp_2 and temp_2 > temp_3:
    print(f"El valor {temp_2}º es la temperatura máxima ingresada.")
elif temp_1 < temp_3 and temp_2 < temp_3:
    print(f"El valor {temp_3}º es la temperatura máxima ingresada.")
elif temp_1 == temp_2 and temp_1 > temp_3: 
    print(f"El valor {temp_1} es el valor máximo de temperatura ingresado junto con el segundo valor ingresado.")
elif temp_1 > temp_2 and temp_1 == temp_3:
    print(f"El valor {temp_1} es el valor máximo de temperatura ingresado junto con el tercer valor ingresado.")
elif temp_1 < temp_2 and temp_2 == temp_3:
    print(f"El valor {temp_2} es el valor máximo de temperatura ingresado junto con el tercer valor ingresado.")
else:
    print("Los tres valores son iguales")

# Metodo corto sin if
'''temperaturas = [temp_1, temp_2, temp_3]

valor_maximo = max(temperaturas)
print("El maximo valor de temperatura es:", valor_maximo)'''

# Punto 2
if temp_1 < temp_2 and temp_1 < temp_3:
    print(f"El valor {temp_1}º es la temperatura mínima ingresada.")
elif temp_1 > temp_2 and temp_2 < temp_3:
    print(f"El valor {temp_2}º es la temperatura mínima ingresada.")
elif temp_1 > temp_3 and temp_2 > temp_3:
    print(f"El valor {temp_3}º es la temperatura mínima ingresada.")
elif temp_1 == temp_2 and temp_1 < temp_3:
    print(f"El valor {temp_1} es el valor mínimo de temperatura ingresado junto con el segundo valor ingresado.")
elif temp_1 < temp_2 and temp_1 == temp_3:
    print(f"El valor {temp_1} es el valor mínimo de temperatura ingresado junto con el tercer valor ingresado.")
elif temp_1 > temp_2 and temp_2 == temp_3:
    print(f"El valor {temp_2} es el valor mínimo de temperatura ingresado junto con el tercer valor ingresado.")
else:
    print("Los tres valores son iguales")

# Metodo con funcion min()

'''temperaturas = [temp_1, temp_2, temp_3]
valor_min = min(temperaturas)
print = ("El valor mínimo de temperatura es:", valor_min)'''


# Punto 3 - promedio 

temperaturas = [temp_1, temp_2, temp_3]

promedio = sum(temperaturas) / len(temperaturas)

print(f"El promedio de las temperaturas es: {promedio}º")

