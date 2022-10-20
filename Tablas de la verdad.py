# Tabla de la verdad con and

print(True and False) 
print(False and True)
print(False and False)
print(True and True)

print( "Esto es un ejemplo")
# Ejemplo :

a = 10
b = 5

resultado = a > b and b < a 
print(resultado)


# El and solo sera verdadero si y solo si las dos comparaciones son verdaderos

print("Tabla con el or")

# Tabla de la verdad con or 
print(True or False)
print(False or True)
print(False or False)
print(True or True)
print()

# En or , solo saldra en verdadero cuando una de las condiciones se cumplan o las dos, pero si ninguna se cumple sera falso

print("ejemplo de Or")

c = 10
d = 21
e = 35

Resultado2 = c > d or e < d

print(Resultado2)


print()

# Tabla de la verdad con xor ( ^ ) o exclusivo


print(True ^ False)
print(False ^ True)
print(False ^ False)
print(True ^ True)
print()

# ejemplo de xor, solo funciona cuando hay una disyuncion en la logica, cuando ambas partes son diferentes, entonces dara verdadero

p =  4
v = 9
s = 2

resultado3 = v > p ^ s > v

print(resultado3)
