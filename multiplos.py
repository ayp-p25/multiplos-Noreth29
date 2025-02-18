"""
multiplos
"""

# Declaraciones
try:

# Entradas
    numero1 = int(input("Introduzca un número "))
    numero2= int(input("Introduzca otro número "))

    if numero1 != 0 :
       
# Proceso
        if numero1 % numero2 == 0:
            resultado = "El número " + str(numero1) + " es múltiplo del " + str(numero2)

        elif numero2 % numero1 == 0:
            resultado = "El número " + str(numero2) + " es múltiplo del " + str(numero1)

        else:
            resultado = "Ninguno de los números es múltiplo del otro "

    
    else:
        resultado = "Error. Introduzca un número válido"

except ZeroDivisionError :
    resultado ="Error. Introduzca un número válido"

except ValueError :
    resultado = "Error. Introduzca otro valor."

print(resultado)