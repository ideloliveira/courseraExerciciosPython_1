import math

x_1Plano = float(input("Entre com  coordenada X do primeiro plano: "))
y_1Plano = float(input("Entre com  coordenada Y do primeiro plano: "))
x_2Plano = float(input("Entre com  coordenada X do segundo plano: "))
y_2Plano = float(input("Entre com  coordenada Y do segundo plano: "))
print()
valorXY = (x_1Plano - x_2Plano)**2 + (y_1Plano - y_2Plano)**2
distanciaXY = math.sqrt(valorXY)

if distanciaXY >= 10:
    print("longe")
else:
    print("perto")
