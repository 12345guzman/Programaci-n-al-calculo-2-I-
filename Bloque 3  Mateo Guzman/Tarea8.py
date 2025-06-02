#1. Crear una función que imprima un mensaje.Escribe una función llamada saludo() que imprima '¡Hola, mundo!'.
def saludo():
    print("¡Hola, mundo!")

#2. Función con un argumento.Crea una función llamada saludar(nombre) que imprima 'Hola, <nombre>'.
def saludar(nombre):
    print(f"Hola, {nombre}")

#3. Suma de dos números.Define una función sumar(a, b) que retorne la suma de ambos números.
def sumar(a, b):
    return a + b

#4. Calcular el salario.Escribe la función computepay(horas, tarifa) para calcular el pago con horas extra.
def computepay(horas, tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else:
        salario = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return salario

#5. Función para determinar el mayor carácter.Escribe una función mayor_caracter(cadena) que retorne el carácter mayor en una cadena.
def mayor_caracter(cadena):
    if not cadena:
        return None  # Retorna None si la cadena está vacía
    mayor = cadena[0]
    for caracter in cadena:
        if caracter > mayor:
            mayor = caracter
    return mayor

#6. Conversión de tipo. Crea una función convertir_a_flotante(valor) que intente convertir una cadena a float.
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except ValueError:
        return None  
    
#7. Función que retorna un saludo en diferentes idiomas.Escribe saludo_idioma(lang) que retorne 'Hola' si es 'es', 'Bonjour' si es 'fr', y 'Hello' por defecto.
def saludo_idioma(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"
    
#8. Comprobar si un número es par.Crea una función es_par(numero) que retorne True si el número es par.
def es_par(numero):
    return numero % 2 == 0

#9. Concatenar cadenas.Crea una función concatenar(cad1, cad2) que retorne la concatenación de ambas cadenas.
def concatenar(cad1, cad2):
    return cad1 + cad2
#10. Calcular promedio.Define una función promedio(lista) que calcule el promedio de una lista de números.
def promedio(lista):
    if not lista:
        return 0 
    return sum(lista) / len(lista)

#11. Contar vocales.Escribe contar_vocales(cadena) que retorne cuántas vocales hay en la cadena.
def contar_vocales(cadena):
    contador = 0
    for caracter in cadena.lower():
        if caracter in 'aeiou':
            contador += 1
    return contador

#12. Revertir cadena.Define una función invertir(cadena) que devuelva la cadena al revés.
def invertir(cadena):
    return cadena[::-1]

#13. Tabla de multiplicar.Crea una función tabla(numero) que imprima la tabla de multiplicar del número del 1 al 10.
def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#14. Función sin parámetros.Crea una función llamada mensaje() que imprima tres líneas de texto distintas.
def mensaje():
    print("Esta es la primera línea.")
    print("Esta es la segunda línea.")
    print("Esta es la tercera línea.")

#15. Función que retorne el número más pequeño.Define menor_valor(lista) que retorne el número más pequeño de una lista.
def menor_valor(lista):
    if not lista:
        return None  # Retorna None si la lista está vacía
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

#16. Calcular factorial.Crea una función factorial(n) que calcule el factorial de un número.
def factorial(n):
    if n < 0:
        return None  # Factorial no está definido para números negativos
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

#17. Determinar si un número es primo.Escribe una función es_primo(numero) que retorne True si es primo, False si no.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
#18. Repetir una cadena n veces.Crea una función repetir(cadena, n) que retorne la cadena repetida n veces.
def repetir(cadena, n):
    return cadena * n

#19. Función con múltiples parámetros.Define una función descripcion(nombre, edad, ciudad) que imprima una frase con esos datos.
def descripcion(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

#20. Verificar palíndromo.Escribe es_palindromo(cadena) que retorne True si la cadena es un palíndromo.
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  
    return cadena == cadena[::-1]  
