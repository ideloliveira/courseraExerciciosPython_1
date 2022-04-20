numero = int(input("digite um número inteiro: "))

if numero % 2 == 0:
    if numero == 2:
        print("primo")
    else:
        print("não primo")
elif numero % 3 == 0:
    if numero == 3:
        print("primo")
    else:
        print("não primo")
elif numero % 5 == 0:
    if numero == 5:
        print("primo")
    else:
        print("não primo")
elif numero % 7 == 0:
    if numero == 7:
        print("primo")
    else:
        print("não primo")
else:
    print("Primo")
