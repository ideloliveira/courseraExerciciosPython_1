import math

def delta(a,b,c):
    return b**2 - 4*a*c

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
print()



def raizPositivo(a,b,delta):
    x1 = (-b + math.sqrt(delta))/ (2 * a)
    return x1

def raizNegativo(a,b,delta):
    x2 = (-b - math.sqrt(delta))/ (2 * a)
    return x2

def equacaoSegGrau(a,b,delta):
    if delta >=0:
        if delta > 0:
            if raizPositivo(a,b,delta) > raizNegativo(a,b,delta):
                print("as raízes da equação são %g e %g" %(raizNegativo(a,b,delta),raizPositivo(a,b,delta)))
            else:
                print("as raízes da equação são %g e %g" %(raizPositivo(a,b,delta),raizNegativo(a,b,delta)))
        else:
            print("a raiz dupla desta equação é %g" %(raizPositivo(a,b,delta)))
    else:
        print("esta equação não possui raízes reais")
    
