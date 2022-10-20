# CONDICIONALES



from difflib import Match


print("CONDICIONAL IF")

# LA CONDICIONAL IF SOLO SE EJECUTARA SI Y SOLO SI LAS CONDICIONES SE CUMPLEN  O SON VERDADES

# if condiciones:
#       acciones
#       acciones2
#aciones fuera del If

print("EJEMPLO")

a = 1
b = 2
c = 3

if (a <b)  and (b < c ):
    print('Como se cumple la condicion entonces se ejecuta el print')
    print("Puedo poner varias condiciones y todas ellas pueden ejecutarse")
    
print()

print("Otro ejemplo")

# elif se utiliza cuando se quiere verificar varias condiciones  y si en el  if no se cumple la condicion entonces salta al elif, se puede utilizar varias elif y se ejecutara la primera que de verdadero

if (a >b)  and (b < c ):
    print('Como se cumple la condicion entonces se ejecuta el print')
    print("Puedo poner varias condiciones y todas ellas pueden ejecutarse")
elif a < b:
    print("COmo el if es falso , entonces salta al elif, podemos tener cuantos querramos")

print()

print("Otro ejemplo")

#Else se ejecutar si las condiciones son falsas

    
if (a >b)  and (b < c ):
    print('Como se cumple la condicion entonces se ejecuta el print')
    print("Puedo poner varias condiciones y todas ellas pueden ejecutarse")
elif a == 9:
    print("COmo el if es falso , entonces salta al elif, que siempre necesitara una condicion")
else:
    print("Como el if es falso y el elif, que es otra condicion es falsa, se ejecuta el else, que solo puede haber una  y no necesita condicion por que se sobrentiende que se ejecuta por que las otras anteriores dieron falso")
    
    
#CONDICION WHILE
print("BUCLE WHILE")

print()

# WHILE mientras las condiciones sean true , entonces se van a ejecutar una y otra vez, hasta que la condicione sea falsa. Por esa razon necesita alterar el programa para que sea falso y se detenga el bucle.

print('Ejemplo')

contador = 1

while contador <= 10:
    # lo que ocurre dentro de un bucle se llama iteracion
    print( ' contador vale : ' , contador)
    contador += 1
    
# Se puede romper un bucle con el comando

print('Como romper las iteraciones de un bucle con break y continiu')
print()
print('ejemplo')

contador2 = 1

while contador2 <= 10:
    if contador2 % 2 == 0:
        print (contador2, 'es un numero par')
    contador2 += 1

# Se puede romper una ejecucion en proceso con BREAK
print()
print('ejemplo con breake ')


contador3 = 1

while contador3 <= 10:
    print(contador3)
    if contador3 == 9 :
        print(contador3, 'Hasta aqui se cuenta:')
        break
        
    contador3 += 1
    
print()
print('Tambien se puede forzar la siguiente interacion, eso puede hacer que se cree un bucle infinito')
    
    
# Ejemplo, con bucle infinito

#contador4 = 1

#while contador4 <= 10:
    
#    if contador4 % 2 == 0:  
#        print(contador4)
#        continue
    # no sigue si es 2 
#    print(' como esta continuo esta linea de codigo no lo agarra')
#    contador4 += 1

# Esto ya no es un infitino

contador4 = 1

while contador4 <=10:
    
    contador4 += 1

    
    if contador4 % 2 == 0:
        print( contador4, "Es un numero par")
        continue
    
    print(contador4, 'No se ha disparado continue')


print()
print()
print('BUCLE FOR')

print()

# la sintaxis
# for  valor in lista:
#   acciones

lista = [ 2, 3 , 7 , 29 , 32, 1, 43]

for dondeGuardoElValor in lista:
    print ('Esto recorre la lista =>' , dondeGuardoElValor)
    

print()
print()
print('TAMBIEN SE PUEDE DEVOLVER UNA CONJUNTO  DE VALORES , CON RANGE y podemos ver  cuanta es nuestra lonitud de la lista con len')

print() 

longitud = len(lista)
print('la longitud de mi lista es esta >>', longitud)

for conjuntoDeValores in range(1,11):
    
    print(conjuntoDeValores)
 

    
print()
print()
print('podemos buscar en la lista')    

for palabra in lista:
    print( 'Recorre la lista hasta',palabra)
    
    if palabra == 2:
        print('encontre lo que buscaba', palabra)
   
#sin embargo de esta manera se recorre toda la lista o itere sin necesidad, debemos parar la busqueda cuando encontremos lo que buscamos.
print()
print()

for palabra in lista:
    print( 'Recorre la lista hasta',palabra)
    
    if palabra == 2:
        print('encontre lo que buscaba', palabra)
        break
    
#Hay otra forma de hacerlo de manera mas eficiente
print()
print()

if 2 in lista :
    #la parte de la izquierda, que es 2 este contenido en la parte de la derecha que es lista, pero tambien podemos negarlo con NOT IN , asi le decimos si 2 no esta en lista .
    print('encontramos la palabra mas rapido', palabra)

print()
print()
print('como podemos ordenar las listas')

# LAs listas se ordenan con sorted, de manera ascendente y tambien de forma descendente, sorted (lista , reverse = true
# )

numero = range (1,101)
        

for n in reversed(numero):
    print(n)
####
Listaordenada = sorted(lista)

print(Listaordenada)

print()
print('lista desordenada')

listadesordenada = sorted(lista, reverse=True)
print(listadesordenada)

print()
print('Switch')
# Es una conveniencia para comaparar una variable con determinados valores y actuar en consecuencia.

# esta es la forma antigua de hacer switch
valor = 4

if valor == 1:
    print("este es un numero uno")
    
elif valor == 2:
    print("este es un numero dos")

elif valor == 3:
    print("este es un numero tres")

elif valor == 4:
    print("este es un numero cuatro")

# pero hay otra forma de hacer mas eficaz y es con switch
print('palabra reservada para hacer un switch es MATCH')
print()

match valor:
    case 1:
        print("este es un numero uno")
    case 2:
        print("este es un numero dos")
    case 3:
        print("este es un numero tres")
    case 4:
        print("este es un numero cuatro")
        
        
print()
print(' Ambito de una variable')

#Ambito global y ambito bucle.  Cuando pongo una lista fuera de un bucle , funcionan tanto dentro como fuera del bucle , pero si se declara dentro del bucle esa variable solo funcniona alli.
  
print('LA PALABRA MAGICA PASS')

#en el que momento que esta pase de todo, que funcione la fucnion pero sin implementarlo\
    
for palabra in lista:
    pass

if 5> 6:
    pass