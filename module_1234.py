def umdoistresquatro():
    """Deals with the '1234 stages' module of the bomb in the game."""
    def um(num, d, estagio):
        t = 'x'
        p = 'x'
        if num == '1':
            p = '2'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '2':
            p = '2'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '3':
            p = '3'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '4':
            p = '4'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        estagio['1']['n'] = num
        estagio['1']['p'] = p
        estagio['1']['t'] = t

        return estagio

    def dois(num, d, estagio):
        t = 'x'
        p = 'x'
        if num == '1':
            t = '4'
            print(f'\nPressione o botão de número {t}')
            while p not in '1234fim':
                p = input('\nPosição do botão: ')
            if p == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '2':
            p = estagio['1']['p']
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '3':
            p = '1'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '4':
            p = estagio['1']['p']
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        estagio['2']['n'] = num
        estagio['2']['p'] = p
        estagio['2']['t'] = t

        return estagio

    def tres(num, d, estagio):
        t = 'x'
        p = 'x'
        if num == '1':
            t = estagio['2']['t']
            print(f'\nPressione o botão de número {t}')
            while p not in '1234fim':
                p = input('\nPosição do botão: ')
            if p == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '2':
            t = estagio['1']['t']
            print(f'\nPressione o botão de número {t}')
            while p not in '1234fim':
                p = input('\nPosição do botão: ')
            if p == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '3':
            p = '3'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '4':
            t = '4'
            print(f'\nPressione o botão de número {t}')
            while p not in '1234fim':
                p = input('\nPosição do botão: ')
            if p == 'fim':
                cancel = 'cancel'
                return cancel

        estagio['3']['n'] = num
        estagio['3']['p'] = p
        estagio['3']['t'] = t

        return estagio

    def quatro(num, d, estagio):
        t = 'x'
        p = 'x'
        if num == '1':
            p = estagio['1']['p']
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '2':
            p = '1'
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '3':
            p = estagio['2']['p']
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        elif num == '4':
            p = estagio['2']['p']
            print(f'\nPressione o botão na {d[p]} posição')
            while t not in '1234fim':
                t = input('\nNúmero do botão: ')
            if t == 'fim':
                cancel = 'cancel'
                return cancel

        estagio['4']['n'] = num
        estagio['4']['p'] = p
        estagio['4']['t'] = t

        return estagio

    def cinco(num, d, estagio):
        t = 'x'
        p = 'x'
        if num == '1':
            t = estagio['1']['t']
            print(f'\nPressione o botão de número {t}')

        elif num == '2':
            t = estagio['2']['t']
            print(f'\nPressione o botão de número {t}')

        elif num == '3':
            t = estagio['3']['t']
            print(f'\nPressione o botão de número {t}')

        elif num == '4':
            t = estagio['4']['t']
            print(f'\nPressione o botão de número {t}')

        estagio['5']['n'] = num
        estagio['5']['p'] = p
        estagio['5']['t'] = t

        return estagio

    print('\n1 2 3 4')

    dici = {'1': 'PRIMEIRA', '2': 'SEGUNDA', '3': 'TERCEIRA', '4': 'QUARTA'}
    c = 1
    est = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}}
    while 1:
        n = '8'
        while n not in '1234fim':
            n = input('\nPara sair, digite "fim"'
                      '\nQual o número na tela? ')
            if n == 'fim':
                break

        if n == 'fim':
            break

        if c == 1:
            est = um(n, dici, est)
            if est == 'cancel':
                break

        elif c == 2:
            est = dois(n, dici, est)
            if est == 'cancel':
                break

        elif c == 3:
            est = tres(n, dici, est)
            if est == 'cancel':
                break

        elif c == 4:
            est = quatro(n, dici, est)
            if est == 'cancel':
                break

        elif c == 5:
            est = cinco(n, dici, est)
            break

        c += 1

    return


if __name__ == '__main__':
    umdoistresquatro()
