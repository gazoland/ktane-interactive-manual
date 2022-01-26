import time


def morse():
    """Deals with the 'morse code' module of the bomb in the game."""
    print('\nMorse')

    mor = {'.-': 'a', '-.-.': 'c', '.': 'e', '..-.': 'f', '..': 'i', '.-..': 'l', '--': 'm',
           '-.': 'n', '---': 'o', '.--.': 'p', '.-.': 'r', '...': 's', '-': 't', '..-': 'u'}

    freq = {'po': '3.505',  # podre
            'fr': '3.515',  # frase
            'un': '3.522',  # unido
            'op': '3.532',  # opera
            'tr': '3.535',  # trufa
            'mi': '3.542',  # misto
            'pa': '3.545',  # parar
            'ri': '3.552',  # ritmo
            'mu': '3.555',  # mundo
            'se': '3.565',  # senado
            'su': '3.572',  # surfe
            'ti': '3.575',  # times
            'mo': '3.582',  # moeda
            'ma': '3.592',  # malote
            'pe': '3.595',  # pesca
            'pu': '3.600'}  # pudim

    while True:
        cod = input('\n"fim" para terminar'
                    '\n"." para "ponto"'
                    '\n"-" para traço'
                    '\nDigite as letras em morse, separando por espaços: ').lower()

        if cod == 'fim':
            break

        p = cod.split(sep=' ')
        aux = ''
        c = 0
        for k in p:
            aux += mor[k]
            c += 1
            if c == 2:
                break

        try:
            print(f'\nA frequência é: {freq[aux]}')
            f = input('Digite "fim" para terminar o módulo: ').lower().strip()
        except KeyError:
            print('\nTente as duas primeiras letras novamente.')
            time.sleep(1.3)
            f = ''

        if f == 'fim':
            break


if __name__ == '__main__':
    morse()
