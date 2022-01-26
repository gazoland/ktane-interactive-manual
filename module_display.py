from unidecode import unidecode


def display():
    """Deals with the 'display' module of the bomb in the game."""
    print('\nDisplay')

    tela = {'sim': {'linha': 'Segunda', 'coluna': 'primira'},
            'vocee': {'linha': 'Primeira', 'coluna': 'segunda'},
            'display': {'linha': 'Terceira', 'coluna': 'segunda'},
            'ok': {'linha': 'Primeira', 'coluna': 'segunda'},
            'tafalando': {'linha': 'Terceira', 'coluna': 'segunda'},
            'nada': {'linha': 'Segunda', 'coluna': 'primeira'},
            '': {'linha': 'Terceira', 'coluna': 'primeira'},
            'vazio': {'linha': 'Segunda', 'coluna': 'segunda'},
            'nao': {'linha': 'Terceira', 'coluna': 'segunda'},
            'cela': {'linha': 'Segunda', 'coluna': 'primeira'},
            'sela': {'linha': 'Terceira', 'coluna': 'segunda'},
            'cem': {'linha': 'Segunda', 'coluna': 'segunda'},
            'sexta': {'linha': 'Segunda', 'coluna': 'segunda'},
            'cesta': {'linha': 'Terceira', 'coluna': 'primeira'},
            'sem': {'linha': 'Terceira', 'coluna': 'primeira'},
            'calmaai': {'linha': 'Terceira', 'coluna': 'segunda'},
            'denovo': {'linha': 'Segunda', 'coluna': 'segunda'},
            'cauda': {'linha': 'Terceira', 'coluna': 'segunda'},
            'calda': {'linha': 'Segunda', 'coluna': 'segunda'},
            'vce': {'linha': 'Segunda', 'coluna': 'segunda'},
            'boom': {'linha': 'Primeira', 'coluna': 'primeira'},
            'errou': {'linha': 'Terceira', 'coluna': 'segunda'},
            'mas': {'linha': 'Terceira', 'coluna': 'primeira'},
            'mais': {'linha': 'Segunda', 'coluna': 'segunda'},
            'nunca': {'linha': 'Segunda', 'coluna': 'primeira'},
            'se': {'linha': 'Terceira', 'coluna': 'segunda'},
            'c': {'linha': 'Primeira', 'coluna': 'segunda'},
            'ser': {'linha': 'Terceira', 'coluna': 'segunda'}}

    pals = {
        'pronto': ['SIM', 'OK', 'O QUÊ?', 'MEIO', 'ESQUERDA', 'APERTA', 'CERTO', 'ASSENTO', 'PRONTO', 'NÃO', 'PRIMEIRO',
                   'HMMMMM', 'NADA', 'ACENTO'],
        'primeiro': ['ESQUERDA', 'OK', 'SIM', 'MEIO', 'NÃO', 'CERTO', 'NADA', 'HMMMMM', 'ACENTO', 'PRONTO', 'ASSENTO',
                     'O QUÊ?', 'APERTA', 'PRIMEIRO'],
        'nao': ['ASSENTO', 'HMMMMM', 'ACENTO', 'PRIMEIRO', 'O QUÊ?', 'PRONTO', 'CERTO', 'SIM', 'NADA', 'ESQUERDA',
                'APERTA', 'OK', 'NÃO', 'MEIO'],
        'assento': ['ACENTO', 'CERTO', 'OK', 'MEIO', 'ASSENTO', 'APERTA', 'PRONTO', 'NADA', 'NÃO', 'O QUÊ?', 'ESQUERDA',
                    'HMMMMM', 'SIM', 'PRIMEIRO'],
        'nada': ['HMMMMM', 'CERTO', 'OK', 'MEIO', 'SIM', 'ASSENTO', 'NÃO', 'APERTA', 'ESQUERDA', 'O QUÊ?', 'ACENTO',
                 'PRIMEIRO', 'NADA', 'PRONTO'],
        'sim': ['OK', 'CERTO', 'HMMMMM', 'MEIO', 'PRIMEIRO', 'O QUÊ?', 'APERTA', 'PRONTO', 'NADA', 'SIM', 'ESQUERDA',
                'ASSENTO', 'NÃO', 'ACENTO'],
        'oque?': ['HMMMMM', 'O QUÊ?', 'ESQUERDA', 'NADA', 'PRONTO', 'ASSENTO', 'MEIO', 'NÃO', 'OK', 'PRIMEIRO',
                  'ACENTO', 'SIM', 'APERTA', 'CERTO'],
        'hm': ['PRONTO', 'NADA', 'ESQUERDA', 'O QUÊ?', 'OK', 'SIM', 'CERTO', 'NÃO', 'APERTA', 'ASSENTO', 'HMMMMM',
               'MEIO', 'ACENTO', 'PRIMEIRO'],
        'esquerda': ['CERTO', 'ESQUERDA', 'PRIMEIRO', 'NÃO', 'MEIO', 'SIM', 'ASSENTO', 'O QUÊ?', 'HMMMMM', 'ACENTO',
                     'APERTA', 'PRONTO', 'OK', 'NADA'],
        'certo': ['SIM', 'NADA', 'PRONTO', 'APERTA', 'NÃO', 'ACENTO', 'O QUÊ?', 'CERTO', 'MEIO', 'ESQUERDA', 'HMMMMM',
                  'ASSENTO', 'OK', 'PRIMEIRO'],
        'meio': ['ASSENTO', 'PRONTO', 'OK', 'O QUÊ?', 'NADA', 'APERTA', 'NÃO', 'ACENTO', 'ESQUERDA', 'MEIO', 'CERTO',
                 'PRIMEIRO', 'HMMMMM', 'SIM'],
        'ok': ['MEIO', 'NÃO', 'PRIMEIRO', 'SIM', 'HMMMMM', 'NADA', 'ACENTO', 'OK', 'ESQUERDA', 'PRONTO', 'ASSENTO',
               'APERTA', 'O QUÊ?', 'CERTO'],
        'acento': ['HMMMMM', 'NÃO', 'ASSENTO', 'OK', 'SIM', 'ESQUERDA', 'PRIMEIRO', 'APERTA', 'O QUÊ?', 'ACENTO',
                   'NADA', 'PRONTO', 'CERTO', 'MEIO'],
        'aperta': ['CERTO', 'MEIO', 'SIM', 'PRONTO', 'APERTA', 'OK', 'NADA', 'HMMMMM', 'ASSENTO', 'ESQUERDA',
                   'PRIMEIRO', 'O QUÊ?', 'NÃO', 'ACENTO'],
        'voce': ['CLARO', 'VOCÊ É', 'OCÊ', 'CÊ É', 'PRÓXIMO', 'AHÃ', 'C É', 'CENSO', 'QUÊ?', 'VOCÊ', 'NÃO SEI', 'SENSO',
                 'BORA', 'REPETE'],
        'vocee': ['OCÊ', 'PRÓXIMO', 'SENSO', 'AHÃ', 'QUÊ?', 'BORA', 'NÃO SEI', 'CENSO', 'VOCÊ', 'REPETE', 'CÊ É',
                  'CLARO', 'C É', 'VOCÊ É'],
        'oce': ['NÃO SEI', 'VOCÊ É', 'AHÃ', 'OCÊ', 'PRÓXIMO', 'C É', 'CLARO', 'REPETE', 'CÊ É', 'VOCÊ', 'QUÊ?', 'CENSO',
                'SENSO', 'BORA'],
        'cee': ['VOCÊ', 'CÊ É', 'C É', 'PRÓXIMO', 'NÃO SEI', 'VOCÊ É', 'REPETE', 'OCÊ', 'QUÊ?', 'AHÃ', 'CLARO', 'BORA',
                'SENSO', 'CENSO'],
        'ce': ['BORA', 'REPETE', 'C É', 'AHÃ', 'QUÊ?', 'CLARO', 'OCÊ', 'CENSO', 'CÊ É', 'SENSO', 'PRÓXIMO', 'NÃO SEI',
               'VOCÊ É', 'VOCÊ'],
        'repete': ['AHÃ', 'CLARO', 'PRÓXIMO', 'QUÊ?', 'CÊ É', 'C É', 'NÃO SEI', 'BORA', 'REPETE', 'VOCÊ', 'SENSO',
                   'CENSO', 'VOCÊ É', 'OCÊ'],
        'aha': ['AHÃ', 'OCÊ', 'VOCÊ É', 'VOCÊ', 'BORA', 'CENSO', 'NÃO SEI', 'PRÓXIMO', 'CLARO', 'SENSO', 'CÊ É', 'C É',
                'REPETE', 'QUÊ?'],
        'naosei': ['C É', 'REPETE', 'VOCÊ É', 'CÊ É', 'PRÓXIMO', 'NÃO SEI', 'BORA', 'VOCÊ', 'AHÃ', 'SENSO', 'OCÊ',
                   'CLARO', 'CENSO', 'QUÊ?'],
        'que?': ['VOCÊ', 'CENSO', 'CÊ É', 'OCÊ', 'REPETE', 'BORA', 'NÃO SEI', 'SENSO', 'VOCÊ É', 'AHÃ', 'C É',
                 'PRÓXIMO', 'QUÊ?', 'CLARO'],
        'bora': ['CLARO', 'AHÃ', 'PRÓXIMO', 'QUÊ?', 'OCÊ', 'C É', 'CÊ É', 'CENSO', 'SENSO', 'VOCÊ', 'REPETE', 'VOCÊ É',
                 'NÃO SEI', 'BORA'],
        'proximo': ['QUÊ?', 'AHÃ', 'NÃO SEI', 'OCÊ', 'CENSO', 'CLARO', 'PRÓXIMO', 'SENSO', 'BORA', 'VOCÊ É', 'C É',
                    'CÊ É', 'REPETE', 'VOCÊ'],
        'censo': ['VOCÊ É', 'REPETE', 'BORA', 'NÃO SEI', 'VOCÊ', 'C É', 'CLARO', 'QUÊ?', 'CÊ É', 'PRÓXIMO', 'CENSO',
                  'AHÃ', 'OCÊ', 'SENSO'],
        'claro': ['VOCÊ É', 'BORA', 'SENSO', 'CÊ É', 'VOCÊ', 'CENSO', 'AHÃ', 'C É', 'CLARO', 'REPETE', 'QUÊ?',
                  'PRÓXIMO', 'OCÊ', 'NÃO SEI'],
        'senso': ['CÊ É', 'PRÓXIMO', 'REPETE', 'C É', 'CENSO', 'BORA', 'NÃO SEI', 'QUÊ?', 'AHÃ', 'VOCÊ', 'SENSO',
                  'CLARO', 'VOCÊ É', 'OCÊ'], 'fim': 'uhuu'}

    while 1:
        disp = 'start'
        while disp not in tela.keys():
            disp = unidecode(input('\nPara voltar ao menu, digite "fim"'
                                   '\nDigite a palavra como está aparecendo na tela: ').lower().replace(" ", ""))

            if disp == 'fim':
                break

        if disp == 'fim':
            break

        tecla = ''
        while tecla not in pals.keys():
            tecla = unidecode(input(f'\n{tela[disp]["linha"]} linha, {tela[disp]["coluna"]} coluna'
                                    f'\nDigite a palavra da tecla: ').lower().replace(" ", ""))

            if tecla == 'fim':
                break

            if tecla in ['hmm', 'hmmm', 'hmmmm', 'hmmmmm', 'hmmmmmm', 'hmmmmmmm']:
                tecla = 'hm'

        if tecla == 'fim':
            break
        res = 'x'
        for i in pals[tecla]:
            rep = True

            while rep:
                res = input(f'\nTem essa palavra em uma das teclas? [S] Sim | [N] Não'
                            f'\n{i} ').lower()
                if res == 's' or res == 'sim' or res == 'n' or res == 'nao' or res == 'não':
                    rep = False

                if res == 'fim':
                    break

            if res == 's' or res == 'sim' or res == 'fim':
                break

        if res == 'fim':
            break
    return


if __name__ == '__main__':
    display()
