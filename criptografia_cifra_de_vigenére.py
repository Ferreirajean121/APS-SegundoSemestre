a = 5
abcdario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print("Bem vindo!")
print("programa feito por:")
print("Jean Ferreira")
print("Lucas Marques")

print("Tecle enter para continuar:")
input()

while a!=0:
    TextoFinal = ""
    print("Digite uma opção")
    print("Digite '1' para criptografar")
    print("Digite '2' para descriptografar")
    opcao = int(input("Sua escolha:"))
    texto = ''.join(str(input("Digite o texto: ")).upper().split())
    key = str(input("Digite a key: ")).upper()
    keyfinal = ""
    
    if(len(key)>len(texto)):
        print("A key é maior que a frase!")
    else:
        i = int(0)
        while (len(keyfinal)<len(texto)):
            keyfinal += key[i]
            i+=1
            if(i == len(key)):
                i = 0
        for i in range(len(texto)):
            if(texto[i]) != '':
                posicao_letra_frase = int(abcdario.index(texto[i]))
                posicao_letra_chave = int(abcdario.index(keyfinal[i]))
                if(opcao == 1):
                    TextoFinal += str(abcdario[(posicao_letra_frase+posicao_letra_chave) % len(abcdario)])
                else:
                    TextoFinal += str(abcdario[(posicao_letra_frase-posicao_letra_chave) % len(abcdario)])
            else:
                TextoFinal += ''
        print("Frase final: {}".format(TextoFinal))
        input()
pass
                
    
