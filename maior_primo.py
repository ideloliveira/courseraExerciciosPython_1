def ePrimo(k):
    i = 1
    p = 0
    contador = 0

    while i <= k:
        if k % i == 0:
            contador += 1
            if contador > 2:
                break
        i = i + 1
    if contador == 2:
        return 1
    else:
        return 0
    
def maior_primo(n):
    i = 1
    maior = 0
    p = 0
    
    while i <= n :
        if(ePrimo(i) == 1):
            if i > p:
               maior = i
            elif i < p:
                maior = p

            p = i
           
        i += 1
    return maior
