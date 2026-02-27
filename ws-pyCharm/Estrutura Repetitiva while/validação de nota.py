primeiraNota:float
segundaNoita:float
media:float

primeiraNota = float(input())

while primeiraNota < 0 or primeiraNota > 10:
    print("Valor invalido! Tente novamente:")
    primeiraNota = float(input())

segundaNota = float(input())

while segundaNota < 0 or segundaNota > 10:
    print("Valor invalido! Tente novamente:")
    segundaNota = float(input())

media = (primeiraNota + segundaNota) / 2

print(f"MEDIA = {media:.2f}")
meiraNota = float(input('Valor invalido! Tente novamente:'))