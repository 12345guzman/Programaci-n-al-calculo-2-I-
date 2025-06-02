numero = -1
print('Antes', numero)
for el_numero in {9,41,12,3,74,15,87}:
    if el_numero > numero:
        numero = el_numero
    print(numero, el_numero)

print('Despues', numero)