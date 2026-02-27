temperatura: str
fahrenheit: float
celsius: float

temperatura = str(input("Voce vai digitar a temperatura em qual escala (C/F)?"))

if temperatura == 'F':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:"))
    celsius = (fahrenheit - 32)/1.8
    print(f"Temperatura equivalente em Celsius:{celsius:.2f}")
elif temperatura == 'C':
    celsius = float(input("Digite a temperatura em Celsius:"))
    fahrenheit = (celsius * 1.8) + 32
    print(f"Temperatura equivalente em fahreinheit:{fahrenheit:.2f}")