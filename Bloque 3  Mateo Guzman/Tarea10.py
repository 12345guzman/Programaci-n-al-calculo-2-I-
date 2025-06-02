#Actividad 2: En grupos de 4-5 personas
#Cada grupo recibe un reto:
# #•	Calculadora básica (suma, resta, etc.)

def calculadora():
    print("Bienvenido a la calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("Elige una opción (1-5): ")
        if opcion == "5":
            print("Gracias por utilizar esta calculadora.")
            break
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida, intenta de nuevo.")
            continue
        elif opcion in ["1", "2", "3", "4"]:
            if opcion == "1":
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif opcion == "2":
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif opcion == "3":
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif opcion == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                else:
                    print("Error: División por cero.")
        else:
            print("Opción no válida, intenta de nuevo.")

calculadora()

dibujo.rectangle([50, 50, 350, 250], fill='blue', outline='black')