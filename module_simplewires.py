import time


def fios_simples():
    """Deals with the 'simple wires' module of the bomb in the game."""
    def tres_fios(fio, col_b, col_p, col_v, col_z, col_m):
        if 'v' not in fio:
            print('\nCorte o segundo fio.')
        elif fio[:] == 'b':
            print('\nCorte o último fio.')
        elif col_z > 1:
            print('\nCorte o último fio azul.')
        else:
            print('\nCorte o último fio.')
        print('\nRetornando ao menu...')
        time.sleep(1)

    def quatro_fios(fio, col_b, col_p, col_v, col_z, col_m):
        ld = input('Último dígito do serial: ').lower()
        print(f'Último dígito do serial: {ld}')
        time.sleep(1)
        if col_v > 1 and int(ld) % 2 != 0:
            print('\nCorte o último fio vermelho.')
        elif fio[:] == 'm' and col_v == 0:
            print('\nCorte o primeiro fio.')
        elif col_z == 1:
            print('\nCorte o primeiro fio.')
        elif col_m > 1:
            print('\nCorte o último fio.')
        else:
            print('\nCorte o segundo fio.')
        print('\nRetornando ao menu...')
        time.sleep(1)

    def cinco_fios(fio, col_b, col_p, col_v, col_z, col_m):
        ld = input('Último dígito do serial: ').lower()
        print(f'Último dígito do serial: {ld}')
        time.sleep(1)
        if fio[:] == 'p' and int(ld) % 2 != 0:
            print('\nCorte o quarto fio.')
        elif col_v == 1 and col_m > 1:
            print('\nCorte o primeiro fio.')
        elif col_p == 0:
            print('\nCorte o segundo fio.')
        else:
            print('\nCorte o primeiro fio.')
        print('\nRetornando ao menu...')
        time.sleep(1)

    def seis_fios(fio, col_b, col_p, col_v, col_z, col_m):
        ld = input('Último dígito do serial: ').lower()
        print(f'Último dígito do serial: {ld}')
        time.sleep(1)
        if col_m == 0 and int(ld) % 2 != 0:
            print('\nCorte o terceiro fio.')
        elif col_m == 1 and col_b > 1:
            print('\nCorte o quarto fio.')
        elif col_v == 0:
            print('\nCorte o último fio.')
        else:
            print('\nCorte o quarto fio.')
        print('\nRetornando ao menu...')
        time.sleep(1)

    print('\nFios Simples')
    loop = True
    fios = []
    while loop:
        fios = input('\n[B] Branco   [P] Preto   [V] Vermelho   [Z] Azul   [M] Amarelo\n'
                     'Digite apenas as teclas que representam as cores dos fios, em sequência e sem espaços, '
                     'de acordo com as teclas acima:\n '
                     ).lower()
        for f in fios:
            if f not in 'pbzmv':
                loop = True
                break
            else:
                loop = False

    c_b, c_p, c_v, c_z, c_m = 0, 0, 0, 0, 0

    for f in fios:
        if f == 'b':
            c_b += 1
        elif f == 'p':
            c_p += 1
        elif f == 'v':
            c_v += 1
        elif f == 'z':
            c_z += 1
        elif f == 'm':
            c_m += 1
    if len(fios) == 3:
        tres_fios(fios, c_b, c_p, c_v, c_z, c_m)
    if len(fios) == 4:
        quatro_fios(fios, c_b, c_p, c_v, c_z, c_m)
    if len(fios) == 5:
        cinco_fios(fios, c_b, c_p, c_v, c_z, c_m)
    if len(fios) == 6:
        seis_fios(fios, c_b, c_p, c_v, c_z, c_m)


if __name__ == '__main__':
    fios_simples()
