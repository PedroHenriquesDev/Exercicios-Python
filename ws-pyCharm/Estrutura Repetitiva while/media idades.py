idade:int
soma:int
contador:int

print("Digite as idades:")

soma = 0
contador = 0

idade = int(input())

while idade >= 0:
    soma += idade
    contador += 1
    idade = int(input())

if contador == 0:
    print("IMPOSSIVEL CALCULAR")
else:
    media = soma / contador
    print(f"MEDIA = {media:.2f}")





