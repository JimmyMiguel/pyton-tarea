
from calendar import c
from cgi import print_arguments


print('UNA FUNCNION ES UNA FORMA DE REUTILIZAR CODIGO O REDUCIR LA COMPLEJIDAD DE MI CODIGO, debemos nombrar una funcnion dependiendo a lo que hace')
print('La funcnion se escribe  con la palabra reservada DEF NOMBRE (LOS PARAMETROS)  luego el codigo  de la funcnion ') 
print()
print('# las funcniones de python debem ser cargadas por el interprete, siempre deben ser invocadas depues de su fucnnion ') 
print()
print('ejemplo')
print()

def mifuncion():
    print('aqui va mi fucnion primero, antes de ser declarada')
    print('mas lineas')
    
print('Esto se ejecuta primero, por que va en orden cascada')




print()
mifuncion()
print()
print('aqui va despues de mi funcnion')
print()
#



#########---------------------

print(' FUNCION CON PARAMTROS, un parametro ES UNA VARIABLE QUE VA A UTILIZAR UNA FUNCNION')
print()


def sumar (a,b):
     a + b
     print(a+b)
     
sumar(4,3)
print(sumar)


print()
print('Se puede crear una funcnion dentro de otra funcion')

def matematicas (c,d):
    
    def sumar (c,d):
        print(c+d)
    def restar (c,d):
        print(c-d)
    def multiplicar(c,d):
        print(c*d)
    sumar(2,3)
    restar(3,1)
    multiplicar(3,4)
matematicas(2,3)
        

print()
print(' FUNCION CON PARAMTROS, un parametro ES UNA VARIABLE QUE VA A UTILIZAR UNA FUNCNION, SE PUEDE UTILIZAR UNA VARIABLE DENTRO DE UNA FUNCION, ESTAS VARIABLES DE FUNCION SOLO  Y SOLO FUNCIONAN DENTRO DE LA FUNCION M NO SE PUEDE INVOCAR DESDE AFUERA, PERO SI SE PUEDE INVOCAR DESDE ADENTRO UNA VARIABLE DESDE FUERA DEL AMBITO DE LA FUNCION')

def nombre (nombres):
    edad = 26
    print("Hola me llamo", nombres , " y tengo",edad, "de edad")
    
nombre("Jimmy")

print()
print(' LAS VARIABLES SON DE AMBITO GLOBAL O DE AMBITO LOCAL, LAS VARIABLES SHADOWIN: SON VARIABLES QUE SE LLAMAN IGUAL PERO UNA ES DE AMBITO GLOBAL Y OTRA DE AMBITO LOCAL.')

print()
print('UNA VARIABLE LOCAL , PUEDE TRANSFORMASE EN UNA VCARIABLE GLOBAL UTILIZANDO LA PALABRA RESERVAD GLOBAL')

TEMPERATURA = 32

def clima (dia):
    TEMPERATURA = 64
    print("hoy es ", dia , "con una temperatura de", TEMPERATURA)

clima ("lunes")
print(TEMPERATURA)
    
#vemos que la variable temperatura dentro de la funcion sobrepone al variable fuera dela funcion, anque no se desaparece la primera variable.
# si utilizamos GLOBAL A la variable local esta se convertitara en global
print()
TEMPERATURA = 32

def clima (dia):
    global TEMPERATURA
    TEMPERATURA = 64
    print("hoy es ", dia , "con una temperatura de", TEMPERATURA)

clima ("lunes")
print(TEMPERATURA)

print()
print(' PARAMETROS OPCIONALES : son parametros que se declaran deltro de la funcion para que cuando se llame a la funcion, funciones sin necesidad de declararlos. para que se pueda realizar esto es necesario siempre delclara todos los parametros o solo el ultimo.')
print()


def usuario (nombre = 'Jimmy'):
    print ( ' mi nombre es ' , nombre)

usuario()

print()

print("Tambien puedo modificar los valores cuando llamo mi funcnion, a pesar de que esta ya declarada en mis parametros.")

def usuario (nombre = 'Jimmy', apellido = "Galarza" , edad = 29):
    print ( ' mi nombre es ' , nombre, apellido, "y tengo " , edad)

usuario("Miguel","Guachizaca")

print()

print("")

def usuario (nombre, apellido , edad = 29):
    print ( ' mi nombre es ' , nombre, apellido, "y tengo " , edad)

usuario("jimmy", "Galarza")

print()

print("Cuando las funciones lleguen a tener un numero de parametros gigantes es mejor hacer esto, un numero de parametros variables")

def suma (a,b,c,d,e,f,g,h,i,j):
    print(a,b,c,d,e,f,g,h,i,j)

suma(1,2,4,3,0,0,0,0,0,0)

#EVITAR HACER ESTO

print()

print("*args, es una conveccion donde se convirte todos los parametros que llamamos en una tupla")

def suma (*args):
    print(args)

suma(1,2,4,3,0,0,0,0,0,0)

print()

print("**kwargs, en este caso es para los parametros que estan en texto, y los parametrso se convierten en diccionario")

def suma (**kwargs):
    print(kwargs)

suma(nombre='jimmy', Apellido="galarza")

print()

print('la funcion RETURN nos devulve el resultado de la operacion, ademas se hacer multiples operaciones , pero la devulve como una tupla , eso se puede cambiar si asignamos una variable a cada parametro.')

def suma (a,b):
    return a + b, a*b , a/b

resulltado = suma(2,4)
print(resulltado[1])

print()
print('de esta manera me devuelve el resutado en variables')

def suma (a,b):
    return a + b, a*b , a/b

sum,_,_ = suma(2,4)
print(sum)

print()
print('lambda: es una funcnion aninima  se utiliza cuando queremos hacer rapido una funcion, las funcniones anonimas no tienen nombre y tiene  que asignarse a una variable')

print()

funcionAnonim = lambda: print('ola')

funcionAnonim

print( ' tambien pueden tener parametros')

anonima = lambda nombre: print('hola ', nombre)

anonima("jimmy")

print( ' varios paremetros')

anonima = lambda nombre, apellido: print('hola ', nombre , 'y mi aperrido es ', apellido)

anonima("jimmy", 'galarza')


suma = lambda numero: numero * 5

print(suma(1))
