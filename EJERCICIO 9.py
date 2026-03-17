
#---------------- EJERCICIO 9 ---------------
#METODOS DE LISTAS 

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

