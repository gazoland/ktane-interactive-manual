from unidecode import unidecode


def fios_complicados():
    """Deals with the 'complicated wires' module of the bomb in the game."""
    print('\nFios Complicados')

    resp = ['sim', 's', 'n', 'nao', 'fim']
    d = ''
    while d not in resp:
        d = unidecode(input('\nDigite [S] Sim | [N] Não'
                            '\nO último número do serial é par? ').lower())
    if d == 'sim' or d == 's':
        dig = True
    else:
        dig = False

    e = ''
    while e not in resp:
        e = unidecode(input('\nDigite [S] Sim | [N] Não'
                            '\nTem uma entrada paralela na bomba? ').lower())
    if e == 'sim' or e == 's':
        ent = True
    else:
        ent = False

    p = ''
    while p not in resp:
        p = unidecode(input('\nDigite [S] Sim | [N] Não'
                            '\nTem pelo menos 1 pilha na bomba? ').lower())
    if p == 'sim' or p == 's':
        pil = True
    else:
        pil = False

    r = ''
    while r != 'fim':
        vm = ''
        while vm not in resp:
            vm = unidecode(input('\nDigite [S] Sim | [N] Não'
                                 '\nTem VERMELHO no fio? ').lower())
        if vm == 'sim' or vm == 's':
            v = True
        elif vm == 'fim':
            break
        else:
            v = False

        az = ''
        while az not in resp:
            az = unidecode(input('\nDigite [S] Sim | [N] Não'
                                 '\nTem AZUL no fio? ').lower())
        if az == 'sim' or az == 's':
            a = True
        elif az == 'fim':
            break
        else:
            a = False

        es = ''
        while es not in resp:
            es = unidecode(input('\nDigite [S] Sim | [N] Não'
                                 '\nTem uma ESTRELA na base do fio? ').lower())
        if es == 'sim' or es == 's':
            e = True
        elif es == 'fim':
            break
        else:
            e = False

        le = ''
        while le not in resp:
            le = unidecode(input('\nDigite [S] Sim | [N] Não'
                                 '\nO LED está ACESO no topo do fio? ').lower())
        if le == 'sim' or le == 's':
            led = True
        elif le == 'fim':
            break
        else:
            led = False

        msg = ['Corte o fio', 'Não corte o fio']

        if v and a and e and led:
            print(f'\n{msg[1]}')
        elif v and a and e and not led:
            if ent:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif v and a and not e and led:
            if dig:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif v and a and not e and not led:
            if dig:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif v and not a and e and led:
            if pil:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif v and not a and e and not led:
            print(f'{msg[0]}')
        elif v and not a and not e and led:
            if pil:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif v and not a and not e and not led:
            if dig:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        #######
        if not v and a and e and led:
            if ent:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif not v and a and e and not led:
            print(f'\n{msg[1]}')
        elif not v and a and not e and led:
            if ent:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif not v and a and not e and not led:
            if dig:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif not v and not a and e and led:
            if pil:
                print(f'\n{msg[0]}')
            else:
                print(f'\n{msg[1]}')
        elif not v and not a and e and not led:
            print(f'{msg[0]}')
        elif not v and not a and not e and led:
            print(f'{msg[1]}')
        elif not v and not a and not e and not led:
            print(f'{msg[0]}')

        r = input('\nPara sair, digite "fim"'
                  '\nPara digitar o próximo fio, digite qualquer tecla.').lower()


if __name__ == '__main__':
    fios_complicados()
