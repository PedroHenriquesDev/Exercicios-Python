times = ('Palmeiras','São Paulo','Fluminense',
         'Flamengo','Bahia','Atlético-PR','Coritiba',
         'Grêmio','Vasco da Gama','EC Vitória','Corinthians',
         'Internacional','Atlético-MG','Bragantino','Chapecoense',
         'Santos','Botafogo','Mirassol','Remo','Cruzeiro')

print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os 4 ultimos times são {times[15:-1]}')
print(f'Os times em ordem alfabética {sorted(times)}')
print(f'O time Chapecoense está na {times.index('Chapecoense')+1}ª posição')