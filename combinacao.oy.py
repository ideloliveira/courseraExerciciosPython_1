# Escreva o seu programa
def fatorial(n):
     fatorial = i = 1
     if n < 0:
            return 0
     while i <=n:
            fatorial = fatorial * i
            i += 1
     return fatorial
        
def combinacao(m,n):
    return fatorial(m) / (fatorial(n)*fatorial(m-n))
