print("----------")
print("advinhe so")
print("----------")

numero_secreto = 50
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("tentativa {} de {}" , format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("voce digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
    print("voce acertou")
    else:
        if(maior):
            print("voce errroouuu, a seu chute foi maior do que o numero secreto")
        elif(menor):
            print("voce errouuu, o seu chute foi menor do que o numero secreto")

    rodada = rodada + 1

print("fim de jogo")
