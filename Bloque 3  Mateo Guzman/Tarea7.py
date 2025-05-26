def computepay(horas, tarifa):
    if horas <= 40:
        salario = horas * tarifa
    else:
        salario = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return salario

horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
salario = computepay(horas_trabajadas, tarifa_por_hora)
print("Salario:", salario)