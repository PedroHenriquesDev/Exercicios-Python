num1: float
num2: float
funcao: str
resultado: float


num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
funcao = str(input("Agora escolha uma função matemática: soma(+),subtração(-),divisão(/) ou multiplicação(*):"))

if funcao == '+':
    resultado = num1 + num2
elif funcao == '-':
    resultado = num1 - num2
elif funcao == '/':
    resultado = num1 / num2
elif funcao == '*':
    resultado = num1 * num2
else:
    print(f"{funcao} não é válido")

print(f"RESULTADO = {resultado}")