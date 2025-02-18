"""
multiplos
"""

# Declaraciones
try:

# Entradas
    numero1 = int(input("Introduzca un número "))
    numero2= int(input("Introduzca otro número "))

# Proceso
    if numero1 % numero2 == 0:
        print("El número " + str(numero1) + " es múltiplo del " + str(numero2))

    elif numero2 % numero1 == 0:
       print("El número " + str(numero2) + " es múltiplo del " + str(numero1)) 

    else:
       print("Ningún número es múltiplo del otro")

except ValueError:
    print("Error. Introduzca un número válido")