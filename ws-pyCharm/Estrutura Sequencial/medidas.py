a:float
b:float
c:float
areaQuadrado:float
areaTriangulo:float
areaTrapezio:float

a = float(input("Digite a medida A: "))

b = float(input("Digite a medida B: "))

c = float(input("Digite a medida B: "))

areaQuadrado = a ** 2

areaTriangulo = (a * b) / 2

areaTrapezio = ((a + b) * c) / 2

print(f"AREA DO QUADRADO = {areaQuadrado:.4f}")
print(f"AREA DO TRIANGULO = {areaTriangulo:.4f}")
print(f"AREA DO TRAPEZIO = {areaTrapezio:.4f}")