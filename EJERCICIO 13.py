
#------------------------- EJERCICIO 13 ---------------
#FUNCIONES - SON BLOQUES DE CODIGO QUE REALIZA UNA TAREA ESPECIFICA 
# Y QUE SON REUTILIZABLES

#FUNCION SIN PARAMETROS NI DEVOLUCION DE VALOR 
def saludar():
    print("Hola, bienvenido a Python")
    
#FUNCION CON PARAMETROS 
def saludo(nombre):
    print("Hola " + nombre + ", bienvenido a Clases")
    
#FUNCION QUE DEVUELVE VALORES
def suma(a, b):
    return a + b

#ESTABLECER VALORES POR DEFECTO EN LOS PARAMETROS DE UNA FUNCION
def bienvenida(nombre = "Estudiante"):
    print ("Bienvenido",nombre)

#FUNCION CON ARGUMENTOS VARIABLES
def sumador(*args):
    return sum(args)

#LLAMADA A LA FUNCION 
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))
