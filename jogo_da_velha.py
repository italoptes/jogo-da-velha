import random
tabuleiro = [" " for _ in range(9)]

def verifica_vitoria(simbolo):
    #verifica linha
    if(tabuleiro[0] == simbolo and tabuleiro[1] == simbolo and tabuleiro[2] == simbolo) or \
    (tabuleiro[3] == simbolo and tabuleiro[4] == simbolo and tabuleiro[5] == simbolo) or \
    (tabuleiro[6] == simbolo and tabuleiro[7] == simbolo and tabuleiro[8] == simbolo):
        return True
    
    #verifica coluna
    if(tabuleiro[0] == simbolo and tabuleiro[3] == simbolo and tabuleiro[6] == simbolo) or \
    (tabuleiro[1] == simbolo and tabuleiro[4] == simbolo and tabuleiro[7] == simbolo) or \
    (tabuleiro[2] == simbolo and tabuleiro[5] == simbolo and tabuleiro[8] == simbolo):
        return True

    #verifica diagonal
    if(tabuleiro[0] == simbolo and tabuleiro[4] == simbolo and tabuleiro[8] == simbolo) or \
    (tabuleiro[2] == simbolo and tabuleiro[4] == simbolo and tabuleiro[6] == simbolo):
        return True
    
    #caso nenhum caso seja satisfeito
    return False

def exibe_tabuleiro():
    print("╔═══╦═══╦═══╗")
    print(f"║ {tabuleiro[0] if tabuleiro[0] != ' ' else '1'} ║ {tabuleiro[1] if tabuleiro[1] != ' ' else '2'} ║ {tabuleiro[2] if tabuleiro[2] != ' ' else '3'} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {tabuleiro[3] if tabuleiro[3] != ' ' else '4'} ║ {tabuleiro[4] if tabuleiro[4] != ' ' else '5'} ║ {tabuleiro[5] if tabuleiro[5] != ' ' else '6'} ║")
    print("╠═══╬═══╬═══╣")
    print(f"║ {tabuleiro[6] if tabuleiro[6] != ' ' else '7'} ║ {tabuleiro[7] if tabuleiro[7] != ' ' else '8'} ║ {tabuleiro[8] if tabuleiro[8] != ' ' else '9'} ║")
    print("╚═══╩═══╩═══╝")

def continuar():
    continuar = input("Deseja continuar?\n1 = Sim\n2 = Não\n→ ")
    if continuar == "1":
        novo_tabuleiro = [" " for _ in range(9)]
        return True, novo_tabuleiro, 0, "X"
    else:
        return False, None, None, None


jogador_atual = input("1 -> X\n2 -> O\nEscolha sua opção: ")
simbolo_jogador = "X" if jogador_atual == "1" else "O"
simbolo_computador = "O" if simbolo_jogador == "X" else "X"

print("Vamos jogar!\nVocê é", simbolo_jogador)
print("O computador é", simbolo_computador)

simbolo = "X"  # X sempre começa
jogo_ativo = True
jogadas = 0

while jogo_ativo:
    exibe_tabuleiro()

    if(simbolo_jogador == simbolo):
        try:
            posicao = int(input("Escolha uma posição(1-9): ")) - 1
            if posicao < 0 or posicao > 8:
                print("Posição inválida. Escolha de 1 a 9.")
                continue
            if tabuleiro[posicao] != " ":
                print("Posição ocupada! Tente novamente.")
                continue
        except ValueError:
            print("Digite um número válido (1-9).")
            continue
    else:
        print("Vez do computador ...")
        posicoes_vazias = [i for i in range(9) if tabuleiro[i] == " "]
        posicao = random.choice(posicoes_vazias)

    #Realiza a jogada
    tabuleiro[posicao] = simbolo
    jogadas += 1

    #Verifica vitória
    if(verifica_vitoria(simbolo)):
        exibe_tabuleiro()
        if simbolo == simbolo_jogador:
            print("Você venceu!")
        else:
            print("Computador venceu!")
        jogo_ativo, tabuleiro, jogadas, simbolo = continuar()
        continue

    #Verifica Empate
    if(jogadas == 9):
        exibe_tabuleiro()
        print("Empate!")
        jogo_ativo, tabuleiro, jogadas, simbolo = continuar()
        continue

    simbolo = "O" if simbolo == "X" else "X"
