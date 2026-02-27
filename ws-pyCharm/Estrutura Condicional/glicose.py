glicose: float

glicose = float(input("Digite a medida da glicose:"))

if glicose <= 100.0:
    print("Classificacao: normal")
elif glicose > 100 and glicose <= 140:
    print("Classificacao: elevado")
else:
    print("Classificacao: diabetes ")

