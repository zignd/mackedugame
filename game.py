textos = [
    "Olá, sou a professora Niko (≧∀≦) Digamos que eu saiba todos os idiomas do mundo (de fora dele também), se você está com dificuldade em português… eu posso ajudar!",
    "(★≧▽^))★☆",
    '''Vamos falar um pouco sobre o que é gramática normativa:
Chama-se gramática normativa a gramática que busca ditar ou prescrever as regras gramaticais de uma língua…''',
    "… É como se fosse uma padronização! ☆=(ゝω･)/",
    "Você escolheu o nível fácil, portanto, estudaremos aqui um pouco de fonologia.",
    "Fonologia é a área da linguística que estuda o sistema sonoro de um idioma. A maneira como os fones (sons) se organizam dentro de uma língua, as unidades capazes de distinguir significados, chamadas fonemas. Na fonologia existem muuuuitos tópicos… Focaremos  na ortografia, porém, ensinaremos conceitos básicos dos tópicos necessários!",
    "Eis alguns conceitos básicos que precisamos saber:",
    "# Fonema e letra",
    "É o menor elemento sonoro capaz de estabelecer uma distinção de significado entre as palavras.",
    "Não deve ser confundido com a letra. Representamos os fonemas por meio de sinais chamados letras. A letra é a representação gráfica do fonema.",
    "Na palavra sapo, por exemplo, a letra s representa o fonema /s/ (lê-se sê); já na palavra brasa, a letra s representa o fonema /z/ (lê-se zê).",
    "...às vezes, o mesmo fonema pode ser representado por mais de uma letra do alfabeto. É o caso do fonema /z/, que pode ser representado pelas letras *z*, *s*, *x*: ",
    '''(z)ebra
    ca(s)amento
    e(x)ílio''',
    "...em alguns casos, a mesma letra pode representar mais de um fonema. A letra x, por exemplo, pode representar:",
    "o fonema sê: te(x)to",
    "o fonema zê:  e(x)ibir",
    "o fonema chê: en(x)ame",
    "o grupo de sons ks: tá(x)i",
    "Vamos deixar isso mais divertido, se você acertar, ganha { } pontos!",
    {"pergunta": "Em qual das palavras abaixo a letra x apresenta não um, mas dois fonemas?",
     "solucao": "b",
     "alternativas": [
         "exemplo",
         "complexo",
         "próximos",
         "executivo",
         "luxo",
     ]},
    "# Vogais",
    "Toda sílaba há necessariamente uma única vogal.",
    "# Semivogais",
    "Os fonemas /i/ e /u/, algumas vezes, não são vogais. Aparecem apoiados em uma vogal, formando com ela uma só emissão de voz (uma sílaba). Nesse caso, esses fonemas são chamados de semivogais.",
    "Observe a palavra papai. Ela é formada de duas sílabas: pa-pai. Na última sílaba, o fonema vocálico que se destaca é o *a*. Ele é a vogal. O outro fonema vocálico i não é tão forte quanto ele. É a semivogal.",
    "Outros exemplos: s(au)dade, histór(ia), sér(ie).",
    "Okay, agora um pouco de fixação! Vale { } pontos (⌒∇⌒):",
]

def main():
    escolherNivel()

def escolherNivel():
    print('''
Escolha o nível em que você deseja jogar:
1. Fácil
2. Intermediário
3. Avançado''')
    while True:
        opcao = input("@> ")
        if opcao == "1":
            return 1
        elif opcao == "2":
            return 2
        elif opcao == "3":
            return 3
        else:
            print("Nível inválido. Digite novamente.")


def exibirTexto(texto):
    print(texto)
    input("[Enter para continuar]")


if __name__ == "__main__":
    main()
