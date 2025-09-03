
"""
  =====================================================================================
  |                                  CALCULADORA SIMPLE-MENU                          |                       
  =====================================================================================
  Esta calculadora tiene un menú simple con las opciones de suma, resta, multiplicación y
  división. El usuario puede elegir la operación que desea realizar y luego ingresar los
  dos números que se van a utilizar en la operación. La calculadora realizará la oper
  ción y mostrará el resultado en pantalla.

  Autor: Ingeniero borojo
  Fecha: 2025-08-25
"""

opcion=input("selecciona una opcion del 1-5")
if opcion == 1:
    texto=input("Ingrese el texto: ")
    resultado= texto.capitalize()
    print (f"Resultado: {resultado}")
    
elif opcion == "2":
    texto=input("Ingrese el texto: ")
    resultado=texto.upper()
    print(f"Resultado{resultado}")

elif opcion == "3":
    texto=input("Ingrese el texto: ")
    resultado=texto.lower()
    print(f"Resultado{resultado}")

elif opcion == "4":
    texto=input("Ingrese el texto: ")
    resultado=texto.title()
    print(f"Resultado{resultado}")
