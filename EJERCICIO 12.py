
#--------------------- EJERCICIO 12 -----------------------
#DICCIONARIO -> ALMACEN A PARES DE CLVE-VALOR

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

