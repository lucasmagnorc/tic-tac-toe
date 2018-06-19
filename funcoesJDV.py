# Função que verifica todas as possibilidades de vencedor e retorna se venceu ou não
def verificaCampeao(tabuleiro, simbolo):
    if tabuleiro[0] == simbolo and tabuleiro[1] == simbolo and tabuleiro[2] == simbolo:
        return simbolo
    elif tabuleiro[3] == simbolo and tabuleiro[4] == simbolo and tabuleiro[5] == simbolo:
        return simbolo
    elif tabuleiro[6] == simbolo and tabuleiro[7] == simbolo and tabuleiro[8] == simbolo:
        return simbolo
    elif tabuleiro[0] == simbolo and tabuleiro[3] == simbolo and tabuleiro[6] == simbolo:
        return simbolo
    elif tabuleiro[1] == simbolo and tabuleiro[4] == simbolo and tabuleiro[7] == simbolo:
        return simbolo
    elif tabuleiro[2] == simbolo and tabuleiro[5] == simbolo and tabuleiro[8] == simbolo:
        return simbolo
    elif tabuleiro[0] == simbolo and tabuleiro[4] == simbolo and tabuleiro[8] == simbolo:
        return simbolo
    elif tabuleiro[2] == simbolo and tabuleiro[4] == simbolo and tabuleiro[6] == simbolo:
        return simbolo
    else:
        return None

# Função para exibir o tabuleiro de exemplo e o tabuleiro de jogo
def imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa):
    print("Humano = " + simboloHumano)
    print("Inteligencia Artificial = " + simboloIa + "\n")
    print("   Jogo\t\t   Posições do tabuleiro")
    print(str(tabuleiro[0])+" | "+str(tabuleiro[1])+" | "+str(tabuleiro[2]) + "\t\t1 | 2 | 3")
    print("--+---+--\t\t--+---+--")
    print(str(tabuleiro[3])+" | "+str(tabuleiro[4]) +
          " | "+str(tabuleiro[5]) + "\t\t4 | 5 | 6")
    print("--+---+--\t\t--+---+--")
    print(str(tabuleiro[6])+" | "+str(tabuleiro[7]) +
          " | "+str(tabuleiro[8]) + "\t\t7 | 8 | 9")

# Função para pegar a posição da jogada do humano, e verificar se ela é válida, e retorna a posição se ela for válida
def validaPosicao(tabuleiro):
    posicao = int(input("\nQual posição deseja jogar ? "))
    while (posicao < 1 or posicao > 9) and tabuleiro != ".":
        posicao = int(input("\nQual posição deseja jogar ? "))
    return posicao-1

# Função para verificar se ocorreu empate no jogo
def verificaEmpate(tabuleiro):
    if not "." in tabuleiro:
        os.system('clear')
        print("EMPATE\n\n")
        funcoesJDV.imprimiTabuleiro(tabuleiro, simboloHumano, simboloIa)
        return True
