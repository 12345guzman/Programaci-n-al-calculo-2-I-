def saludo(lang):
    if lang == "es":
        return ("Hola")
    elif lang == "fr":
        return("Bonjour")
    else:
        return('Hello')


print(saludo ('en'),'mateo guzman')

print(saludo ('es'),'sally')

print(saludo ('fr'),'juan perez')