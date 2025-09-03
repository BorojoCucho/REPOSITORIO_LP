
numero = int(input ("Ingrese un numero para generar su tabla de multiplicar  =   "))

print (f"Tabla de multiplcar del {numero} :")

for i in range (1, 11):
    resultado = numero * i 
    print (f"{numero} x {i} = {resultado}")