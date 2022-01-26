def botao():
    """Deals with the 'button' module of the bomb in the game."""
    class Botao:
        def __init__(self, cor, texto, car_signal, frk_signal):
            self.cor = cor
            self.texto = texto
            self.car = car_signal
            self.frk = frk_signal

    print('\nBotão')
    c = 'x'
    while c not in 'bvmz':
        c = input('[B] Branco   [V] Vermelho   [M] Amarelo   [Z] Azul\n'
                  'Qual a cor do botão? ').lower()

    t = 'x'
    while t not in '1234':
        t = input('[1] Segure   [2] Aperte   [3] Abortar   [4] Detonar\n'
                  'Qual o texto do botão? ').lower()

    n = input('\nQuantas pilhas na bomba? ').lower()
    print(f'{n} pilhas na bomba.')

    car = ''
    while car not in ['s', 'n', 'sim', 'nao', 'não']:
        car = input('\n[S] Sim   [N] Não'
                    '\nIndicador CAR aceso? ').lower()

    frk = ''
    while frk not in ['s', 'n', 'sim', 'nao', 'não']:
        frk = input('\n[S] Sim   [N] Não'
                    '\nIndicador FRK aceso? ').lower()

    if car == 's' or car == 'sim':
        car_sign = True
    else:
        car_sign = False

    if frk == 's' or frk == 'sim':
        frk_sign = True
    else:
        frk_sign = False

    bot = Botao(c, t, car_sign, frk_sign)

    # Resolvendo módulo do botão
    if bot.cor == 'z' and bot.texto == '3':
        print('\nPressione e segure:'
              '\nAzul -> 4'
              '\nBranco -> 1'
              '\nAmarelo -> 5'
              '\nOutra cor -> 1')
        input('\nPressione qualquer tecla para continuar: ')

    elif int(n) > 1 and bot.texto == '4':
        print('\nSó clique e solte imediatamente.')
        input('\nPressione qualquer tecla para continuar: ')

    elif bot.cor == 'b' and bot.car:
        print('\nPressione e segure:'
              '\nAzul -> 4'
              '\nBranco -> 1'
              '\nAmarelo -> 5'
              '\nOutra cor -> 1')
        input('\nPressione qualquer tecla para continuar: ')

    elif int(n) > 2 and bot.frk:
        print('\nSó clique e solte imediatamente.')
        input('\nPressione qualquer tecla para continuar: ')

    elif bot.cor == 'm':
        print('\nPressione e segure:'
              '\nAzul -> 4'
              '\nBranco -> 1'
              '\nAmarelo -> 5'
              '\nOutra cor -> 1')
        input('\nPressione qualquer tecla para continuar: ')

    elif bot.cor == 'v' and bot.texto == '1':
        print('\nSó clique e solte imediatamente.')
        input('\nPressione qualquer tecla para continuar: ')

    else:
        print('\nPressione e segure:'
              '\nAzul -> 4'
              '\nBranco -> 1'
              '\nAmarelo -> 5'
              '\nOutra cor -> 1')
        input('\nPressione qualquer tecla para continuar: ')


if __name__ == '__main__':
    botao()
