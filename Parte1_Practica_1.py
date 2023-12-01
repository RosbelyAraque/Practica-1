
print(".....................Datos tipos numericos..................")
print(".............................int............................")

#Numeros enteros int
#Se declara la variable entero_1 de tipo int y se le asigna erl valor 20 
entero_1 = 20
tipo_numero_1 = type(entero_1)
print("tipo_numero_1:",tipo_numero_1)

print("...........................float.............................")
#Numeros Flotantes
float_1, float_2 ,float_3 = 0.348, 10.5, 1.5e2
print("float_1:",float_1)
print("float_2:",float_2)
print("float_3:",float_3)
tipo_float_1=type(float_1)
print("tipo_float:",tipo_float_1)

print("..........................complex..............................")
#Numeros complejos
#A continuación se declara la variable complejo_1 de tipo complex y se le asigna el valor 2.1+7.8
complejo_1=2.1+7.8j
print("complejo_1:",complejo_1)
tipo_complejo_1=type(complejo_1)
print("tipo_complejo_1,",tipo_complejo_1)
print("complejo_1.imag:",complejo_1.imag)
print("complejo_1.real:",complejo_1.real)
abs_complejo_1 = abs(complejo_1)
print("abs_complejo_1:",abs_complejo_1)

print (".......................Datos tipo booleano...................")

bool1 = False
print("bool1:",bool1)
bool2 = False
print ("bool2:",bool2)
bool3 = 0
print("bool3:",bool3)
bool4 = '" "'
print("bool2:",bool4)
bool5 = None
print("bool5",bool5)
bool6 = []
print ("bool6:",bool6)
bool7 = ()
print ("bool7:",bool7)
bool8 = {}
print ("bool8:",bool8) 
bool9 = [","]
print ("bool9:",bool9)
print("bool1 == bool2:",bool1 == bool2)
print("bool3 == bool1:", bool3 == bool1)
print ("bool4 == bool1:", bool4==bool1)
print ("bool4 == bool1:", bool4==bool1)
print ("bool5 == bool1:",bool5 == bool1)
print ("bool6 == bool1:", bool6 == bool1)
print ("bool7==bool1:", bool7 == bool1)
print ("boll8== bool1:", bool8==bool1)
print ("bool9 == bool1:", bool9 == bool)

print(".....................................................")
bool12 = True

Numero_entero1= int(bool1)
print("numero_entero1:",Numero_entero1)
Numero_entero2= int (bool12)
print ("numero_entero2:",Numero_entero2)

print(".....................................................")

tipo_bool12= type(bool12)
print("tipo_bool12:",tipo_bool12)

print ("....................................................")

tipo_str=str(bool12)
print("tipo_str:",tipo_str)

print(".....................................................")

tipo_str_1 = type(str(True))
print("tipo_str_1:",tipo_str_1)

print(".....................................................")
tipo_bool1=type (bool)
print("tipo_bool1:",tipo_bool1)
print(".....................................................")

tipo_str2=str(bool1)
print ("tipo_str2:",tipo_str2)

print ("....................................................")

tipo_str3= type(str(bool1))
print ("tipo_str3:",tipo_str3)


print (".......................Datos tipo arreglo........................")
#A continuación se declara la variable factura tipo lis y se le asigna una lista con cuatro elementos distintos
#Lista
factura = ['pan', 'huevos', 100,1234]
print("factura:",factura)

print (".......................................................................")
print("factura [0]:",factura [0] )
print("factura [3:]",factura[3])

num_elementos= len (factura)
print("num_elemento:",num_elementos)
num_elementos2= len(factura)-1
print("num_elementos2:",num_elementos2)
print("factura[-1]:",factura [-1])
print("factura [-len(factura)]:",factura [-len(factura)])
factura = ['pan', "carne",'huevos',100, 1234]
print ("factura:",factura)
print("factura [1]:",factura [1])

print(".....................................................................")

versiones_plone=[2.5,3.6,4,5]
print("versiones_plone:",versiones_plone)
versiones_plone.append(6)
print("versiones_plone:",versiones_plone)

print(".....................................................................")
versiones_plone = [2.1,2.5,3.6,4,5,5,6]
print("versiones_plone.count:",versiones_plone.count(6))
print("versiones_plone.count:",versiones_plone.count (5))

print("....................................................................")
versiones_plone = [2.1,2.5,3.6]
print ("versiones_plone:",versiones_plone)
versiones_plone.extend ([4])
print(versiones_plone)

print(".....................................................................")
versiones_plone=[2.1,2.5,3.6,4,5,6,4]
print("versiones_plone.index(4):",versiones_plone.index(4))

print("...................................................................")
versiones_plone= [2.1,2.5,3.6,4,5,6]
print("versiones_plone:",versiones_plone)
versiones_plone.insert(2,3.7)
print("versiones_plone:",versiones_plone)

print ("..................................................................")
versiones_plone= [4,2.5,5,3.6,2.1,6]
print("versiones_plone:",versiones_plone)
versiones_plone.sort()
print("versiones_plone:",versiones_plone)

print ("............................Datos tipo string........................")

#string (str)
print("'Hola mundo'")
hla_mmd= " 'Hola mundo' "
print("hla_mmd=",hla_mmd)

print (".....................................................................")

a,b= "uno", "dos"
print("a+b=",a+b)

print ("......................................................................")

c="tres"
print("c*3:", c*3)

print ("......................................................................")

tipo_calculo="raiz cuadrada de dos"
valor=2**0.5
print ("el resultado de {} es {}". format(tipo_calculo,valor))
