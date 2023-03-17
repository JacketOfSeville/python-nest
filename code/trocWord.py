import os

def substituir_palavra(diretorio, extensao, palavra_antiga, palavra_nova):
    for nome_arquivo in os.listdir(diretorio):  # Loop através de cada arquivo na pasta
        if nome_arquivo.endswith(extensao) and os.path.isfile(os.path.join(diretorio, nome_arquivo)): # Verifica se o arquivo é um arquivo de texto com a extensão desejada
            with open(os.path.join(diretorio, nome_arquivo), 'r') as arquivo:  # Abre o arquivo para leitura e le o conteúdo
                conteudo = arquivo.read()
            conteudo = conteudo.replace(palavra_antiga, palavra_nova) # Substitui a palavra antiga pela nova    
            with open(os.path.join(diretorio, nome_arquivo), 'w') as arquivo: # Abre o arquivo novamente para escrita e escreve o conteúdo modificado
                arquivo.write(conteudo)

# Parâmetros de uso
diretorio = 'C:/Users/Usuario/Desktop/'
extensao = '.txt'
palavra_antiga = 'exemplo'
palavra_nova = 'substituto'
substituir_palavra(diretorio, extensao, palavra_antiga, palavra_nova)
