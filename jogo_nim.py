from operator import truediv


def campeonato():
    print("Voce Escolheu um campeonato!")
    for x in range(3):
        print()
        print("***** Rodada ",x+1," ***")
        print()
        partida()
        
    print("**** Final do Campeonato! ****")
    print()
    print("Placar: Voce 0 X 3 Computador")
    

# Função do Usuario *************************************************
def usuario_escolhe_jogada(n,m):
    
    retira = True
    while retira:
        usuario_retira = int(input("Quantas Peças voce vai tirar? "))
        if usuario_retira > m or usuario_retira < 1 or usuario_retira > n:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            retira = False
        
    return usuario_retira
# função do Computador **********************************************
def computador_escolhe_jogada(n,m):
    i = m
    while i > 0:
        if (n-i)%(m+1)== 0:
            computador_retira = i            
            i = i - 1
            break
        elif n == m:
               computador_retira = m
               break
        else:
            computador_retira = i            
            i = i - 1    
    
    return computador_retira

# Função Partida *****************************************************
def partida():
    n = int(input("Quantas peças? "))
    escolheMax = True
    while escolheMax:
        m = int(input("Limite de peças por partida? "))
        if m > n:
            print("Limite deve ser menor que Peças.")
           
        else:
            escolheMax = False    

    quemJoga = 1

    if n%(m+1)==0:
        print()
        print("Você Começa!")
        print()
        quemJoga = 1
    else:
        print()
        print("Computador Começa!")
        print()
        quemJoga = 0

    while n > 0:
        if quemJoga == 0:
            jogada = computador_escolhe_jogada(n,m)
            n = n-jogada
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:                
                print("Computador tirou",jogada,"peças.")
            quemJoga = 1
        else:
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            if jogada == 1:
                print()
                print("Você tirou uma peça.")
            else:
                print()
                print("Voce tirou",jogada,"peças.")
            quemJoga = 0
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        elif n !=0:
            print("Agora restam",n, " peças no tabuleiro.")
            print()

    print("Fim do Jogo! Computador Ganhou!")
    print()

# Inicio do Program    

def inicio_partida():
    print("Bem vindo ao jogo do MIN! Escolha:")
    print()

    inicio = True
    while inicio:
        escolher = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
        print()
        if escolher > 2 or escolher < 1:
            print("Voce deve escolher : ")
        else:
            print()
            inicio = False

    if escolher == 2:
       campeonato()
    else:
        partida()

inicio_partida()