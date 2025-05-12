#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
while True:
    numero = int (input ("Ingresa un numero: "))
    if numero == 0:
        break
    suma += numero
    print("la suma total es: ", suma)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
import random
numero_secreto = random.randint (1,100)
intento =None

while intento != numero_secreto:
    intento = int(input("Adivina el numero en te el 1 y el 100:  "))
    if intento < numero_secreto:
        print (" Mayor")
    elif intento > numero_secreto:
        print("MENOR")
    else:
        print("Muy bien el numero secreto era", numero_secreto)

#Validar contraseña (repetir hasta que coincida con una guardada).
contraseña= "mateo"
while True:
    entrada = input ("Ingresa la contraseña ")
    if entrada == contraseña:
        print ("contraseña correcta . ")
        break
    else:
        print ("contrase;a incorrecta . intentalo nuevamente.")
#Simular un cajero automático (menú: retirar, depositar, salir).

#Calcular la raíz cuadrada por aproximación (método babilónico).

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.

# MIENTRAS - WHILE
# VISUALIZAR LOS PRIMEROS LOS 5 PRIMEROS NUMEROS DE minestras + WHILE

contador = 0
while contador <= 9:
    print("Numero: ", contador)
    contador +=1
    