valor = input("Digite um valor para somarmos duas unidades: ")
valorDigito = int(valor)
i = 0
soma = 0
while i < len(valor):
    soma = soma + (valorDigito % 10)
    valorDividido = valorDigito // 10
    valorDigito = valorDividido
    i = i + 1

print(soma)
