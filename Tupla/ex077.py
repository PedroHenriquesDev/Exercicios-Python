palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar','trabalhar',
            'mercado','programador','futuro')
for p in palavras:
    print(f'Na palavra {p} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')