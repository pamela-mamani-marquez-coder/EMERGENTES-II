
#------------------ EJERCICIO 3 -----------------------
#MAYUSCULAS A MINUSCULAS VICEVERSA
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