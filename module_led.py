import time


def led():
    """Deals with the 'led' module of the bomb in the game."""
    print('\nLED')
    print('\n| .  .  X  .  X  X | [1]    | X  .  X  .  X  . | [2]'
          '\n| X  X  X  X  .  X |        | .  X  X  .  X  X | '
          '\n __________________          __________________'
          '\n| .  X  X  .  .  X | [3]    | X  .  X  .  X  . | [4]'
          '\n| X  X  X  X  .  X |        | .  X  .  .  .  X | '
          '\n __________________          __________________'
          '\n| .  .  .  .  X  . | [5]    | .  .  .  .  X  . | [6]'
          '\n| X  .  .  X  X  X |        | .  .  .  X  X  . | '
          '\n __________________          __________________'
          '\n| X  .  X  X  X  X | [7]    | X  .  X  X  .  . | [8]'
          '\n| X  X  X  .  X  . |        | X  X  X  .  X  . | ')

    c = {'1': 'para Cima', '2': 'para Cima',
         '3': 'para Baixo', '4': 'para Baixo',
         '5': 'para Esquerda', '6': 'para Esquerda',
         '7': 'para Direita', '8': 'para Direita'}

    n = 'y'
    while n not in '12345678':
        n = input('\nX para o LED aceso e . para o LED apagado.'
                  '\nDigite o número que representa a configuração de LEDs acesos: ')

    print(f'\nConsiderando a posição da legenda "CIMA" como a direção de Cima...'
          f'\n\n ---> Deixe o indicador virado {c[n]}')

    time.sleep(5.4)
    return


if __name__ == '__main__':
    led()
