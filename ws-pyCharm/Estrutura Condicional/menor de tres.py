primeiro: int
segundo: int
terceiro: int

primeiro = int(input("Primeiro valor:"))
segundo = int(input("Segundo valor:"))
terceiro = int(input("Terceiro valor:"))

if primeiro <= segundo and primeiro <= terceiro:
    print(f"MENOR = {primeiro}")
elif segundo <= primeiro and segundo <= terceiro:
    print(f"MENOR = {segundo}")
else:
    print(f"MENOR = {terceiro}")
