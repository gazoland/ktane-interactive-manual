def genius():
    """Deals with the 'genius' module of the bomb in the game."""
    def vermelho(vog, erros, seq):
        if erros == 0:
            seq.append('Azul')
        elif erros == 1:
            if vog:
                seq.append('Amarelo')
            else:
                seq.append('Vermelho')
        elif erros == 2:
            if vog:
                seq.append('Verde')
            else:
                seq.append('Amarelo')
        return seq

    def azul(vog, erros, seq):
        if erros == 0:
            if vog:
                seq.append('Vermelho')
            else:
                seq.append('Amarelo')
        elif erros == 1:
            if vog:
                seq.append('Verde')
            else:
                seq.append('Azul')
        elif erros == 2:
            if vog:
                seq.append('Vermelho')
            else:
                seq.append('Verde')
        return seq

    def verde(vog, erros, seq):
        if erros == 0:
            if vog:
                seq.append('Amarelo')
            else:
                seq.append('Verde')
        elif erros == 1:
            if vog:
                seq.append('Azul')
            else:
                seq.append('Amarelo')
        elif erros == 2:
            if vog:
                seq.append('Amarelo')
            else:
                seq.append('Azul')
        return seq

    def amarelo(vog, erros, seq):
        if erros == 0:
            if vog:
                seq.append('Verde')
            else:
                seq.append('Vermelho')
        elif erros == 1:
            if vog:
                seq.append('Vermelho')
            else:
                seq.append('Verde')
        elif erros == 2:
            if vog:
                seq.append('Azul')
            else:
                seq.append('Vermelho')
        return seq

    print('\nGenius')

    v = ''
    while v not in ['s', 'sim', 'n', 'nao', 'não']:
        v = input('\n[S] Sim   [N] Não'
                  '\nTem alguma vogal no número serial? ').lower()
    if v == 'sim' or v == 's':
        vogal = True
    else:
        vogal = False

    e = '5'
    while e not in '012':
        e = input('\nQuantos erros já cometidos? 0, 1 ou 2? ')
    err = int(e)
    print(f'\n{e} erros.')

    f = ''
    s = []
    while f != 'fim':
        while f not in ['vm', 'vd', 'az', 'am', 'erro', 'fim']:
            f = input('\n"vm" -> Vermelho'
                      '\n"vd" -> Verde'
                      '\n"az" -> Azul'
                      '\n"am" -> Amarelo'
                      '\n"erro" -> reportar um erro'
                      '\n"fim" -> terminar'
                      '\nQual a cor do flash? ').lower()

        if f == 'vm':
            s = vermelho(vogal, err, s)
        elif f == 'az':
            s = azul(vogal, err, s)
        elif f == 'vd':
            s = verde(vogal, err, s)
        elif f == 'am':
            s = amarelo(vogal, err, s)
        elif f == 'fim':
            break
        elif f == 'erro':
            err += 1
            s = []
            print(str(f'Erros: \n{err}'))
        f = ''
        print(', '.join(s))


if __name__ == '__main__':
    genius()
