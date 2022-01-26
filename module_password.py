import itertools


def senha():
    """Deals with the 'password' module of the bomb in the game."""
    print('\nSenha')
    fst = ''
    while len(fst) != 6:
        fst = input('\nDigite as letras da primeira posição: ')
    pri = [x for x in fst]
    sec = ''
    while len(sec) != 6:
        sec = input('\nDigite as letras da segunda posição: ')
    seg = [x for x in sec]
    trd = ''
    while len(trd) != 6:
        trd = input('\nDigite as letras da terceira posição: ')
    ter = [x for x in trd]
    fth = ''
    while len(fth) != 6:
        fth = input('\nDigite as letras da quarta posição: ')
    qua = [x for x in fth]
    fth = ''
    while len(fth) != 6:
        fth = input('\nDigite as letras da quinta posição: ')
    qui = [x for x in fth]
    combs = list(itertools.product(pri, seg, ter, qua, qui))
    cbs = [''.join(list(y)) for y in combs]
    ref = ['acesa', 'ajuda', 'amigo', 'antes', 'arcos',
           'baile', 'balas', 'bispo', 'chefe', 'cheio',
           'cinto', 'cravo', 'etapa', 'etnia', 'flora',
           'lazer', 'legal', 'lugar', 'parte', 'parto',
           'perto', 'porta', 'regra', 'resto', 'salve',
           'sente', 'setor', 'sexta', 'tecla', 'tinta',
           'torta', 'touro', 'trato', 'valer', 'veado']

    if set(cbs) & set(ref):
        print(set(cbs) & set(ref))
    else:
        print('Não encontrado.')


if __name__ == '__main__':
    senha()
