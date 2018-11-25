import string
import textos


def main():
    telaInicial()
    nivel = escolherNivel()
    if nivel == 1:
        pontuacao_atingida, pontuacao_maxima, codigo = rodarJogo(textos.nivel_1)
    else:
        pontuacao_atingida, pontuacao_maxima, codigo = rodarJogo(textos.nivel_2)

    if pontuacao_maxima > 0:
        teleFinal(pontuacao_atingida, pontuacao_maxima, codigo)


def rodarJogo(roteiro):
    pontuacao_atingida = 0
    pontuacao_maxima = 0
    codigo_proximo_nivel = None
    for _, item in enumerate(roteiro):
        if type(item) == str:
            exibirTexto(item)
        elif type(item) == dict:
            if item["tipo"] == "pergunta":
                resposta = fazerPergunta(item)
                if resposta:
                    pontuacao_atingida += 1
                pontuacao_maxima += 1
            elif item["tipo"] == "codigo":
                codigo_proximo_nivel = item["codigo"]
            elif item["tipo"] == "solicitar_codigo":
                print("O acesso a esse nível é restrito a jogadores que passaram do nível anterior e receberam o código especial. Por favor insira o código especial para continuar.")
                codigo_jogador = input("Código especial: ")
                if codigo_jogador == item["codigo_correto"]:
                    print("Código correto. Iniciando nível.")
                else:
                    print("Código incorreto.")
                    break

    return (pontuacao_atingida, pontuacao_maxima, codigo_proximo_nivel)


def telaInicial():
    print('''============================
|| Gramática com a Niko! ||
============================

Olá jogador! Está preparado para embarcar numa jornada inesquecível?! Pois a Niko está pronta para te ajudar!

Nessa jornada você irá aprender um pouco de gramática com a professora Niko, intergalaticamente conhecida como a melhor professor de Português!

Faixa etária: crianças e adolescentes que estão cursando o primeiro ano do ensino médio.
''')


def teleFinal(pontuacao_atingida, pontuacao_maxima, codigo):
    print('''
Nossa jornada chegou ao fim... Mas você pode revive-la a qualquer momento reiniciando esse mesmo nível, ou explorando o outro!

Sua pontuação final foi: {0}/{1} ({2:.2f}%)\n'''.format(pontuacao_atingida, pontuacao_maxima, pontuacao_atingida/pontuacao_maxima*100))
    if pontuacao_atingida/pontuacao_maxima >= 0.5:
        print('''Sua pontuação atingiu a média de 50% ou mais! Então como prêmio você irá receber um código especial que lhe dará acesso ao próximo nível!
Código especial: {0}'''.format(codigo))
    else:
        print("Infelizmente sua pontuação não atingiu a média de 50% ou mais... Estude mais um pouco e tente novamente, tenho certeza que irá passar! E lembre-se que quando passar irá receber um código especial como prêmio!")


def escolherNivel():
    print('''Escolha o nível em que você deseja jogar:
1. Nivel I
2. Nivel II''')
    while True:
        opcao = input("@> ")
        if opcao == "1":
            return 1
        elif opcao == "2":
            return 2
        else:
            print("Nível inválido. Digite novamente.")


def fazerPergunta(pergunta):
    print("\nPergunta: {0}".format(pergunta["texto"]))

    alternativas = pergunta["alternativas"]
    num_alternativas = len(alternativas)
    letras_alternativas = list(string.ascii_lowercase[:num_alternativas])
    for index, letra in enumerate(letras_alternativas):
        print("{0}) {1}".format(letra, alternativas[index]))

    while True:
        resposta = input("@> Resposta: ")
        eh_computavel = resposta in letras_alternativas
        if eh_computavel == False:
            print("Sua resposta está num formato inválido. Tente novamente.")
            continue
        else:
            esta_correta = resposta == pergunta["solucao"]
            if esta_correta:
                print("Você acertou! Parabéns!\n")
            else:
                print("Não foi dessa vez... Mas continue estudando que irá acertar!\n")
            return esta_correta


def exibirTexto(texto):
    print(texto)
    input("@> [Enter]")


if __name__ == "__main__":
    main()
