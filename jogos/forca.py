import os
import funcs_forca

os.system('cls')

def jogar():
    funcs_forca.escreve_palavras_possiveis()
    funcs_forca.msg_abertura()
    palavra_secreta = funcs_forca.escolhe_palavra()
    letras_acertadas = funcs_forca.inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas, "\n")
    while(not enforcou and not acertou):
        
        chute = funcs_forca.pede_chute()

        if(chute in palavra_secreta):
            funcs_forca.marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            funcs_forca.desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas 
        print(letras_acertadas)

    if(acertou):
        funcs_forca.imprime_msg_vencedor()
    else:
        funcs_forca.imprime_msg_perdedor(palavra_secreta)


if(__name__ == "__main__"):
    jogar()