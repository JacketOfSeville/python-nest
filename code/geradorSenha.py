import random
import string

def gerar_senha(tamanho, letras_maiusculas=True, letras_minusculas=True, simbolos=True, numeros=True):
    caracteres = ''
    if letras_maiusculas:
        caracteres += string.ascii_uppercase
    if letras_minusculas:
        caracteres += string.ascii_lowercase
    if simbolos:
        caracteres += string.punctuation
    if numeros:
        caracteres += string.digits
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
letras_maiusculas = input("Incluir letras maiúsculas? (S/N): ").lower() == 's'
letras_minusculas = input("Incluir letras minúsculas? (S/N): ").lower() == 's'
simbolos = input("Incluir símbolos? (S/N): ").lower() == 's'
numeros = input("Incluir números? (S/N): ").lower() == 's'

senha = gerar_senha(tamanho, letras_maiusculas, letras_minusculas, simbolos, numeros)
print("Senha gerada:", senha)
