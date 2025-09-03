# -*- coding: utf-8 -*-
"""
  =====================================================================================
  |                                  CALCULADORA SIMPLE-MENU                          |                       
  =====================================================================================
  Esta calculadora tiene un menú simple con las opciones de suma, resta, multiplicación y
  división. El usuario puede elegir la operación que desea realizar y luego ingresar los
  dos números que se van a utilizar en la operación. La calculadora realizará la oper
  ción y mostrará el resultado en pantalla.

  Autor: Ingeniero borojo
  Fecha: 2025-08-13
"""
# Crear un blucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    print ("\nCalculadora Simple-Menu")
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Salir")
    opcion = input ("Ingrese la opción que desea realizar: ")
    # ==========================OPERACIONES==============================
    # SUMA
    elif opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma {num1} y {num2} es: {resultado}")


# RESTA 
elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
     num2 = float(input("Ingrese el segundo número: "))
     resultado = num1 - num2
        print(f"El resultado de la resta {num1} y {num2} es: {resultado}")


# MULTIPLICACION

elif opcion == "3":
       num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = num1 * num2
print(f"El resultado de la multiplicación {num1} y {num2} es: {resultado}")
    # DIVISION
elif opcion == "4":
      num1 = float(input("Ingrese el primer número: "))
      num2 = float(input("Ingrese el segundo número: "))
      if num2 != 0:
resultado = num1 / num2
print (f"El resultado de la división {num1} y {num2} es: {resultado }")

elif opcion == "5"
print ("Gracias por utilizar la calculadora")
 break
    else:
    print ("Opción no válida. Por favor, ingrese una opción válida.")
input ("Presione Enter para contiruar")