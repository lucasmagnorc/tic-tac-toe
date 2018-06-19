from random import randint

# Verifica o cenário atual para tomar a decisão da jogada
def jogadaIa(tabuleiro, simboloIa):
    if not "X" in tabuleiro or not "O" in tabuleiro:
        posicao = randint(0, 8)
        tabuleiro[posicao] = simboloIa
    else:
        while True:
            posicao = randint(0, 8)
            if tabuleiro[posicao] == ".":
                tabuleiro[posicao] = simboloIa
                return
            
    # PRIMEIRA LINHA HORIZONTAL
    if tabuleiro[0] == simboloIa and tabuleiro[1] == simboloIa and tabuleiro[2] == ".":
        tabuleiro[2] = simboloIa
        return
    elif tabuleiro[0] == simboloIa and tabuleiro[1] == "." and tabuleiro[2] == simboloIa:
        tabuleiro[1] = simboloIa
        return
    elif tabuleiro[0] == "." and tabuleiro[1] == simboloIa and tabuleiro[2] == simboloIa:
        tabuleiro[0] = simboloIa
        return

    # SEGUNDA LINHA HORIZONTAL
    elif tabuleiro[3] == simboloIa and tabuleiro[4] == simboloIa and tabuleiro[5] == ".":
        tabuleiro[5] = simboloIa
        return
    elif tabuleiro[3] == simboloIa and tabuleiro[4] == "." and tabuleiro[5] == simboloIa:
        tabuleiro[4] = simboloIa
        return
    elif tabuleiro[3] == "." and tabuleiro[4] == simboloIa and tabuleiro[5] == simboloIa:
        tabuleiro[3] = simboloIa
        return

    # TERCEIRA LINHA HORIZONTAL
    elif tabuleiro[6] == simboloIa and tabuleiro[7] == simboloIa and tabuleiro[8] == ".":
        tabuleiro[8] = simboloIa
        return
    elif tabuleiro[6] == simboloIa and tabuleiro[7] == "." and tabuleiro[8] == simboloIa:
        tabuleiro[7] = simboloIa
        return
    elif tabuleiro[6] == "." and tabuleiro[7] == simboloIa and tabuleiro[8] == simboloIa:
        tabuleiro[6] = simboloIa
        return

    # PRIMEIRA LINHA VERTICAL
    elif tabuleiro[0] == simboloIa and tabuleiro[3] == simboloIa and tabuleiro[6] == ".":
        tabuleiro[6] = simboloIa
        return
    elif tabuleiro[0] == simboloIa and tabuleiro[3] == "." and tabuleiro[6] == simboloIa:
        tabuleiro[3] = simboloIa
        return
    elif tabuleiro[0] == "." and tabuleiro[3] == simboloIa and tabuleiro[6] == simboloIa:
        tabuleiro[0] = simboloIa
        return

    # SEGUNDA LINHA VERTICAL
    elif tabuleiro[1] == simboloIa and tabuleiro[4] == simboloIa and tabuleiro[7] == ".":
        tabuleiro[7] = simboloIa
        return
    elif tabuleiro[1] == simboloIa and tabuleiro[4] == "." and tabuleiro[7] == simboloIa:
        tabuleiro[4] = simboloIa
        return
    elif tabuleiro[1] == "." and tabuleiro[4] == simboloIa and tabuleiro[7] == simboloIa:
        tabuleiro[1] = simboloIa
        return

    # TERCEIRA LINHA VERTICAL
    elif tabuleiro[2] == simboloIa and tabuleiro[5] == simboloIa and tabuleiro[8] == ".":
        tabuleiro[8] = simboloIa
        return
    elif tabuleiro[2] == simboloIa and tabuleiro[5] == "." and tabuleiro[8] == simboloIa:
        tabuleiro[5] = simboloIa
        return
    elif tabuleiro[2] == "." and tabuleiro[5] == simboloIa and tabuleiro[8] == simboloIa:
        tabuleiro[2] = simboloIa
        return

    # PRIMEIRA DIAGONAL
    elif tabuleiro[0] == simboloIa and tabuleiro[4] == simboloIa and tabuleiro[8] == ".":
        tabuleiro[8] = simboloIa
        return
    elif tabuleiro[0] == simboloIa and tabuleiro[4] == "." and tabuleiro[8] == simboloIa:
        tabuleiro[4] = simboloIa
        return
    elif tabuleiro[0] == "." and tabuleiro[4] == simboloIa and tabuleiro[8] == simboloIa:
        tabuleiro[0] = simboloIa
        return

    # SEGUNDA DIAGONAL
    elif tabuleiro[2] == simboloIa and tabuleiro[4] == simboloIa and tabuleiro[6] == ".":
        tabuleiro[6] = simboloIa
        return
    elif tabuleiro[2] == simboloIa and tabuleiro[4] == "." and tabuleiro[6] == simboloIa:
        tabuleiro[4] = simboloIa
        return
    elif tabuleiro[2] == "." and tabuleiro[4] == simboloIa and tabuleiro[6] == simboloIa:
        tabuleiro[2] = simboloIa
        return
    else:
        return None
        
    
