valorInteiro = input("Digite um número inteiro: ")
valorConvertido = int(valorInteiro)
parada = False
anterior = 0
i = 0

while parada == False:
    valor = valorConvertido % 10
    if len(valorInteiro) == 1:
        print("não")
        break
    elif i == 0 and valor == 0:
        i = i + 1
    elif valor == anterior:
        print("sim")
        parada = True
    elif len(valorInteiro) == i:
        print("não")
        break
    
    anterior = valor
    valorConvertido = valorConvertido // 10
    i = i + 1          
        
        
        

"""

    if len(valorInteiro) > 0:
        valor = valorConvertido % 10
        if valor == anterior:
            print("sim")
            parada = True
        elif len(valorInteiro) == i:
            print("não")
            break
    else:
        print("não")
        break
    anterior = valor
    valorConvertido = valorConvertido // 10
    i = i + 1
"""
