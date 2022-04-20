
def chamada():
    return int(input("Digite o valor de n:"))

def fatorial(n):
    fatorial = i = 1
    if n < 0:
        return 0
    while i <= n:
        fatorial = fatorial * i
        i = i + 1
    return fatorial
