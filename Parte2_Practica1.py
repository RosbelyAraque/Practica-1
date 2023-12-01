

print("...................................Primer ejercio....................")
print("Solicitar al usuario 3 numeros enteros y dar como resultado una lista con los valores ordenados")

# Input ingresa los datos en forma de str, por lo que se usa la funcion int para transformalos a enteros.
input_1 = input("Ingrese el primer numero entero")
numero_1 = int(input_1)
input_2 = input("Ingrese el segundo numero entero")
numero_2 = int(input_2)
input_3 = input("Ingrese el tercer numero entero")
numero_3 = int(input_3)


#Crear una lista con los numeros enteros
Numeros_ingresados = [numero_1,numero_2,numero_3]
print("Numeros ingresados:",Numeros_ingresados)

#Ordenar la lista de numeros

Numeros_ingresados.sort ()

print("Lista con los numeros ordenados:",Numeros_ingresados) 

print (".........................segundo ejercicio...........................")

print("Solicitar al usuario una cadena de caracteres en mayuscula e imprimir una lista con cada palabra en minuscula")

#Solicitar al usuario una cadena de caracteres en mayuscula
cadena_mayuscula=input("ingurese una cadena de caracteres en mayuscula")

#Convertir la cadena de caracteres en palabras minuscula
palabras_minusculas=[palabra.lower() for palabra in cadena_mayuscula.split ()]

#Imprimir la lista con palabras en minuscula 
print("Lista de palabras en minuscula:",palabras_minusculas)