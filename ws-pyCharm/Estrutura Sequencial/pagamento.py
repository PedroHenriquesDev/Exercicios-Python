nome: str
valorHora: float
horasTrabalhadas: int
total: float

nome = str(input("Nome:"))

valorHora = float(input("Valor por hora: "))

horasTrabalhadas = int(input("Horas trabalhadas: "))

total = valorHora * horasTrabalhadas

print(f"O pagamento para {nome} deve ser {total:.2f}")