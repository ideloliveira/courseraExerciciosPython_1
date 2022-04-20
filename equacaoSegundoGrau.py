import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
print()
print("Encontrando as raizes da equação do segundo grau baixo")
if b >= 0 and c >= 0:
    print("%dx² + %dx + %d = 0" %(a,b,c))
elif b >=0 and c < 0:
    print("%dx² + %dx %d = 0" %(a,b,c))
elif b < 0 and c >=0:
    print("%dx² %dx + %d = 0" %(a,b,c))
else:
    print("%dx² %dx %d = 0" %(a,b,c))
print()

delta = ((b**2) - (4*a*c))

if delta >=0:
    x1 = (-b + (math.sqrt(delta)))/ (2*a)
    x2 = (-b - (math.sqrt(delta)))/ (2*a)
else:
    print("não tem raizes reais")
    print("Valor de delta é %d" %(delta))

if delta > 0:
    print("As raízes de x são %d e %d" %(x1,x2))
elif delta == 0:
    print("As raízes de x são %d" %(x1))
