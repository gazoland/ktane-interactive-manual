import time


def fios_sequencia():
    """Deals with the 'sequential wires' module of the bomb in the game."""
    print('\nFios Sequência')

    s = {'a': {1: 'B', 2: 'A|C', 3: 'B', 4: 'A', 5: 'B', 6: 'B|C', 7: 'C', 8: 'A|C', 9: 'A'},
         'v': {1: 'C', 2: 'B', 3: 'A', 4: 'A|C', 5: 'B', 6: 'A|C', 7: 'A|B|C', 8: 'A|B', 9: 'B'},
         'p': {1: 'A|B|C', 2: 'A|C', 3: 'B', 4: 'A|C', 5: 'B', 6: 'B|C', 7: 'A|B', 8: 'C', 9: 'C'}}

    a = 1
    v = 1
    p = 1
    err = {'p': p, 'v': v, 'a': a}
    go = 'start'
    u = 'x'
    while go != 'fim':
        c = ''
        while c not in ['v','a','p','fim']:
            c = input('\nDigite "fim" para sair, "erro" para desconsiderar a última cor ou:'
                      '\n[V] Vermelho | [A] Azul | [P] Preto'
                      '\nDigite a letra que corresponde à cor do fio: ').lower()
        if c == 'v':
            print(f'\nCorte se conectado a: {s["v"][v]}')
            v += 1
            u = 'v'
            time.sleep(1)

        elif c == 'a':
            print(f'\nCorte se conectado a: {s["a"][a]}')
            a += 1
            u = 'a'
            time.sleep(1)

        elif c == 'p':
            print(f'\nCorte se conectado a: {s["p"][p]}')
            p += 1
            u = 'p'
            time.sleep(1)

        elif c == 'erro':
            err[u] -= 1

        elif c == 'fim':
            go = 'fim'

        if a > 9 or v > 9 or p > 9:
            break


if __name__ == '__main__':
    fios_sequencia()