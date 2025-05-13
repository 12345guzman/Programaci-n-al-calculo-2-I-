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
    intento = int(input("Adivina el numero entre el 1 y el 100:  "))
    if intento < numero_secreto:
        print (" Mayor")
    elif intento > numero_secreto:
        print("MENOR")
    else:
        print("Muy bien el numero secreto era", numero_secreto)

#Validar contraseña (repetir hasta que coincida con una guardada).
contraseña= "mateo"
while True:
    entrada = input ("Ingresa la contraseña correspondiente ")
    if entrada == contraseña:
        print (" la contraseña es correcta . ")
        break
    else:
        print ("la contraseña es incorrecta . intentalo nuevamente.")
#Simular un cajero automático (menú: retirar, depositar, salir)
opcion = ""
while opcion != "3":
    print(" Bienvenido a Nuestro cajero ")
    print(" Ingrese 1 para retirar ")
    print(" Ingrese 2 para depositar ")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Cuánto deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas depositar? "))
        print("Has depositado $",monto)
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Que tenga un gran dia !")
    else:
        print("Opción no válida. Intentalo nuevamente.")
#Calcular la raíz cuadrada por aproximación (método babilónico).
numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))
tolerancia = 0.00001
aproximacion = numero / 2

while abs(aproximacion**2 - numero) > tolerancia:
    aproximacion = (aproximacion + numero / aproximacion) / 2

print(f"La raíz cuadrada aproximada de {numero} es {aproximacion}")

#Contar dígitos de un número entero (ej: 456 → 3).
numero = int(input("Ingresa un número entero: "))
contador = 0
temporal = abs(numero)  # para que funcione también con negativos

if numero == 0:
    contador = 1
else:
    while temporal > 0:
        temporal //= 10
        contador += 1

print(f"El número {numero} tiene {contador} dígitos.")

#Generar la secuencia de Fibonacci hasta un límite.
limite = int(input("Generar la secuencia de Fibonacci hasta: "))
a, b = 0, 1

print("Secuencia de Fibonacci:")
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

#Encontrar números primos en un rango dado.

inicio = int(input("El inicio del rango es: "))
fin = int(input("El fin del rango es: "))

print(f"Números primos entre {inicio} y {fin}:")

for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num, end=" ")

#Simular un temporizador (contar regresivamente desde N).
import time 
n = int(input("Ingresa el número desde donde iniciar el conteo regresivo: "))
print("Iniciando temporizador...\n")

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

print("¡Tiempo terminado!")
#Leer archivos línea por línea hasta fin de archivo.
ruta = input("Ingresa la ruta del archivo: ")

try:
    with open(ruta, "r") as archivo:
        print("\nContenido del archivo línea por línea:")
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("Archivo no encontrado. Verifica la ruta ingresada.")

# MIENTRAS - WHILE
# VISUALIZAR LOS PRIMEROS LOS 5 PRIMEROS NUMEROS DE minestras + WHILE

contador = 0
while contador <= 9:
    print("Numero: ", contador)
    contador +=1
    