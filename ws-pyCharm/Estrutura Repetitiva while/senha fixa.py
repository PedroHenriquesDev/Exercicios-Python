senha:int

senha = int(input('Digite a senha:'))

while senha != 2002:
    senha = int(input('Senha inválida! Tente novamente:'))

    if senha == 2002:
        print('Acesso permitido! ')