horaInicial : int
horaFinal : int
duracao: int

horaInicial = int(input('Hora inicial:'))
horaFinal = int(input('Hora final:'))

if horaInicial > horaFinal:
    duracao = (24 - horaInicial) + horaFinal
    print(f'O JOGO DUROU {duracao} HORA(S)')
elif horaInicial < horaFinal:
    duracao = horaFinal - horaInicial
    print(f'O JOGO DUROU {duracao} HORA(S)')
elif horaInicial == horaFinal:
    print(f'O JOGO DUROU 24 HORAS(S)')