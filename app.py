print("Hola mundo desde python!!")

#variables en Python
#enteros
edad = 20
#Float
precio = 50.5
#Str
nombre = "Bruno Diaz"
#Bool
bandera = True

#SALIDA DE DATOS
print("Nombre;", nombre)
print("Edad: ", edad)
print("Precio: " + str(precio))


#ENTRADA DE DATOS
nombre = input("introduce un nombre: ")
print("Hola "+nombre)


#---- ENTRADA DE DATOS DE STR Y FLOAT
num1 = input("Ingresa el primer numero: ")
num2 = input("Ingresa el segundo numero: ")

#Conversion de str a float, str a float
suma = float(num1) + float(num2)

print("La suma total es: ", suma)




#---------MAYUSCULAS A MINUSCULAS VICEVERSA
curso = "Python para iniciantes"
print (curso.upper()) #todo mayuscula
print (curso)
print (curso.lower()) #todo minuscula
print (curso.capitalize()) #primera letra mayuscula


#--- busquedas
print (curso.find("y"))
print (curso.find("h"))
print (curso.find("cia"))

#---reemplazos
print(curso.replace("para","FOR"))
print(curso)

#---operador
print("FOR" in curso)
print("para" in curso)
print("PARA" in curso)

#operadores matematicos
print (10 + 5)
print (10 - 5)
print (10 * 5)
print (10 / 5)

# division entera
print (10 //4)

# modulo - residuo
print (10 % 3)

#exponente 
print (2 ** 4)

x = 10
x = x + 5
print (x)

#--operador de asignacion compacto
y = 20
y += 5
print(y)

#Precedencia 
x = 10 + (3 * 2)
print (x)

#Expresiones boleanas True o False
#>, >=, <, <=, ==, != op. relacionales

x = 3 > 2
print(x)

x = 5 ==  3 
print(x)

x = 5 !=3
print(x)

#operadores logicos and, or, not operadores logicos
precio = 25
print(precio > 20 and precio < 30)

precio = 5
print(precio > 20 or precio < 30)
print( not precio > 10)


#-- sentencia if 
temperatura = int(input ("indica la temperatura: "))

if temperatura > 28:
    print ("esta haciendo calor")
else:
    print ("hace frio")


if temperatura > 28:
    print ("esta haciendo calor")
elif temperatura > 20:
    print ("es un dia agradable")
elif temperatura > 10:
    print ("hace un poco de frio")
else:
    print ("hace frio,brrrrrrrrrr")
    
print("proceso concluido")


#----bucles
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1
    
i = 1
while (i <= 10):
    print(i * "#")
    i += 1
        
        


#-----Listas

frutas = ["Manzana", "Fresa", "Naranja", "Pera" , "Maracuya"]
print(frutas)
print(frutas[0])
print(frutas[4])
print(frutas[-2])
print(frutas[1:4])



#------METODOS DE LISTAS 

numeros = [1, 2, 3, 4, 5]

#ADICIONAR ELEMENTOS A UNA LISTA
numeros.append(6) #Agrega un elemento al final de la lista
print(numeros)   #[1, 2, 3, 4, 5, 6]  

numeros.insert(0, -1) #Agrega un elemento en una posici n espec fica
print(numeros)  

numeros.insert(1, 0)
print(numeros) 

#ELIMINAR ELEMENTOS DE UNA LISTA
numeros.remove(1) #Elimina la primera ocurrencia de un elemento espec fico
print(numeros)

#VERIFICA SI UN ELEMENTO SE ENCUENTRA EN LA LISTA 
print(4 in numeros) #True

#TAMA O DE LA LISTA
print(len(numeros)) #0

#ELIMINAR EL CONTENIDO DE LA LISTA

numeros.clear() #Elimina todos los elementos de la lista
print(numeros) #[]




#--------OBJETO RANGE

numeros = range(5)
print(numeros)

for item in numeros:
    print(item)
    
for item in range(5, 10):
    print(item)
    
for item in range(10, 20, 2):
    print(item)
    


#------------------TUPLAS (INMUTABLES)

numeros = (1, 2, 3, 4, 5, 6)

#IMPRIMIENDO UN ELEMENTO 

print(numeros[3]) #IMPRIME EL CUARTO ELEMENTO DE LA TUPLA

#OCURRENCIA 
print(numeros.count(5)) #IMPRIME CUANTAS VECES SE REPITE EL NUMERO 5 EN LA TUPLA

print(numeros.index(5)) #IMPRIME LA POSICION DEL NUMERO 5 EN LA TUPLA


#----------------DICCIONARIO -> ALMACEN A PARES DE CLVE-VALOR

mi_diccionario = {'nombre': 'bruno', 'edad': 25, 'ciudad': 'La Paz'}
print(mi_diccionario)

#ACCESO A LOS VALORES
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])

#AGREGAR ELEMENTOS
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

#ELIMINAR UN ELEMENTO

del mi_diccionario['ciudad']
print(mi_diccionario)       

#OBTENER LAS CLAVES DEL DICCIOARIO

claves = (mi_diccionario.keys()) 

#OBTENER LOS VALORES DEL DICCIONARIO

print(mi_diccionario.values())

#VERIDICAR SI UNA CLAVE EXISTE EN EL DICCIONARIO

if 'ciudad' in mi_diccionario:
    print('La clave "ciudad" existe en el diccionario')
    
#RECORIDO DE UN DICCIONARIO

for clave, valor in mi_diccionario.items():
    print ("[Clave: ]",clave, "[Valor:]" , valor )


#---------------FUNCIONES - SON BLOQUES DE CODIGO QUE REALIZA UNA TAREA ESPECIFICA 
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
