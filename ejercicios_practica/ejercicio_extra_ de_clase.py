edad = int(input("Ingrese su edad:"))

print(f"Tengo {edad} años")

if edad <= 11:
    print(f"soy un niño de {edad} años")

elif edad > 11 and edad >= 18: 
    print(f"soy un adolescente de {edad} años")

elif edad > 18 and edad >= 60:
    print(f"soy un adulto de {edad} años")

else:
    print(f"soy un adulto mayor")
