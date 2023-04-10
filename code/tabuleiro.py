# Definindo as dimensões do tabuleiro
linhas = 8
colunas = 8

# Definindo os símbolos das peças
peca_branca = 'b'
peca_preta = 'p'
vazio = ' '

# Loop para imprimir o tabuleiro
for linha in range(linhas):
    for coluna in range(colunas):
        if linha % 2 == 0:
            if coluna % 2 == 0:
                print(vazio, end=' ')
            else:
                if linha < 3:
                    print(peca_preta, end=' ')
                elif linha > 4:
                    print(peca_branca, end=' ')
                else:
                    print(vazio, end=' ')
        else:
            if coluna % 2 == 0:
                if linha < 3:
                    print(peca_preta, end=' ')
                elif linha > 4:
                    print(peca_branca, end=' ')
                else:
                    print(vazio, end=' ')
            else:
                print(vazio, end=' ')
    print()