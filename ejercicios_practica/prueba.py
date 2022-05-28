# Recibir dos palabras por consola y compararlas por orden alfabetico
# y tambien por longitud

palabra_1 = str(input("ingrese la primer palabra"))
palabra_2 = str(input("ingrese la seguna palabra"))

if palabra_1 < palabra_2:
    print(f"{palabra_1} es menor alfabeticamente que {palabra_2}")

elif not(palabra_2 < palabra_1):
    print(f"{palabra_2} es menor alfabeticamente que {palabra_1}")

elif palabra_1 == palabra_2:
    print("Ambas palabras son iguales")

palabra_1_inicio = palabra_1 [0:3]

palabra_2_inicio = palabra_2[2:]

if palabra_1_inicio < palabra_2_inicio:
    print(f"{palabra_1_inicio} es menor alfabeticamente que {palabra_2_inicio}")

elif not(palabra_2_inicio < palabra_1_inicio):
    print(f"{palabra_2_inicio} es menor alfabeticamente que {palabra_1_inicio}")

elif palabra_1_inicio == palabra_2_inicio:
    print("Ambas palabras son iguales")
