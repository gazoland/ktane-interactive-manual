import pandas as pd
import numpy as np


def labirinto():
    """Deals with the 'labyrinth' module of the bomb in the game."""
    df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F'], index=np.arange(6))
    df.index = np.arange(1, len(df) + 1)

    # Generating table board
    for c in df.columns:
        for i in df.index:
            df.at[i, c] = str(i) + str(c)

    # Labyrinth References:
    moves1 = {'1A': ['D', 'R'],
              '1B': ['L', 'R'],
              '1C': ['L', 'D'],
              '1D': ['D', 'R'],
              '1E': ['L', 'R'],
              '1F': ['L'],
              '2A': ['D', 'U'],
              '2B': ['D', 'R'],
              '2C': ['L', 'U'],
              '2D': ['U', 'R'],
              '2E': ['L', 'R'],
              '2F': ['L', 'D'],
              '3A': ['D', 'U'],
              '3B': ['U', 'R'],
              '3C': ['L', 'D'],
              '3D': ['D', 'R'],
              '3E': ['L', 'R'],
              '3F': ['L', 'U', 'D'],
              '4A': ['D', 'U'],
              '4B': ['R'],
              '4C': ['L', 'R', 'U'],
              '4D': ['L', 'U'],
              '4E': ['R'],
              '4F': ['U', 'D', 'L'],
              '5A': ['D', 'R', 'U'],
              '5B': ['L', 'R'],
              '5C': ['L', 'D'],
              '5D': ['D', 'R'],
              '5E': ['L'],
              '5F': ['U', 'D'],
              '6A': ['U', 'R'],
              '6B': ['L'],
              '6C': ['U', 'R'],
              '6D': ['U', 'L'],
              '6E': ['R'],
              '6F': ['L', 'U']}
    moves2 = {'1A': ['R'],
              '1B': ['L', 'R', 'D'],
              '1C': ['L'],
              '1D': ['D', 'R'],
              '1E': ['L', 'R', 'D'],
              '1F': ['L'],
              '2A': ['D', 'R'],
              '2B': ['U', 'L'],
              '2C': ['D', 'R'],
              '2D': ['U', 'L'],
              '2E': ['U', 'R'],
              '2F': ['L', 'D'],
              '3A': ['D', 'U'],
              '3B': ['D', 'R'],
              '3C': ['L', 'U'],
              '3D': ['D', 'R'],
              '3E': ['L', 'R'],
              '3F': ['L', 'U', 'D'],
              '4A': ['D', 'U', 'R'],
              '4B': ['L', 'U'],
              '4C': ['D', 'R'],
              '4D': ['L', 'U'],
              '4E': ['D'],
              '4F': ['U', 'D'],
              '5A': ['D', 'U'],
              '5B': ['D'],
              '5C': ['U', 'D'],
              '5D': ['D', 'R'],
              '5E': ['L', 'U'],
              '5F': ['U', 'D'],
              '6A': ['U'],
              '6B': ['U', 'R'],
              '6C': ['U', 'L'],
              '6D': ['U', 'R'],
              '6E': ['R', 'L'],
              '6F': ['L', 'U']}
    moves3 = {'1A': ['D', 'R'],
              '1B': ['L', 'R'],
              '1C': ['L', 'D'],
              '1D': ['D'],
              '1E': ['D', 'R'],
              '1F': ['L', 'D'],
              '2A': ['U'],
              '2B': ['D'],
              '2C': ['D', 'U'],
              '2D': ['U', 'R'],
              '2E': ['L', 'U'],
              '2F': ['U', 'D'],
              '3A': ['D', 'R'],
              '3B': ['U', 'D'],
              '3C': ['U', 'D'],
              '3D': ['D', 'R'],
              '3E': ['L', 'D'],
              '3F': ['U', 'D'],
              '4A': ['D', 'U'],
              '4B': ['D', 'U'],
              '4C': ['D', 'U'],
              '4D': ['D', 'U'],
              '4E': ['D', 'U'],
              '4F': ['D', 'U'],
              '5A': ['D', 'U'],
              '5B': ['U', 'R'],
              '5C': ['L', 'U'],
              '5D': ['D', 'U'],
              '5E': ['D', 'U'],
              '5F': ['U', 'D'],
              '6A': ['U', 'R'],
              '6B': ['L', 'R'],
              '6C': ['U', 'R'],
              '6D': ['U', 'L'],
              '6E': ['R', 'U'],
              '6F': ['L', 'U']}
    moves4 = {'1A': ['D', 'R'],
              '1B': ['L', 'D'],
              '1C': ['R'],
              '1D': ['L', 'R'],
              '1E': ['L', 'R'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U'],
              '2B': ['D', 'U'],
              '2C': ['R', 'D'],
              '2D': ['L', 'R'],
              '2E': ['L', 'R'],
              '2F': ['L', 'D', 'U'],
              '3A': ['D', 'U'],
              '3B': ['U', 'R'],
              '3C': ['L', 'U'],
              '3D': ['D', 'R'],
              '3E': ['L'],
              '3F': ['U', 'D'],
              '4A': ['D', 'U'],
              '4B': ['R'],
              '4C': ['L', 'R'],
              '4D': ['L', 'U', 'R'],
              '4E': ['R', 'L'],
              '4F': ['U', 'D', 'L'],
              '5A': ['D', 'R', 'U'],
              '5B': ['L', 'R'],
              '5C': ['L', 'R'],
              '5D': ['L', 'R'],
              '5E': ['L', 'D'],
              '5F': ['U', 'D'],
              '6A': ['U', 'R'],
              '6B': ['L', 'R'],
              '6C': ['L'],
              '6D': ['R'],
              '6E': ['L', 'U'],
              '6F': ['U']}
    moves5 = {'1A': ['R'],
              '1B': ['L', 'R'],
              '1C': ['L', 'R'],
              '1D': ['L', 'R'],
              '1E': ['L', 'R', 'D'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U'],
              '2B': ['D', 'R'],
              '2C': ['L', 'U'],
              '2D': ['U', 'R'],
              '2E': ['L', 'R'],
              '2F': ['L', 'D'],
              '3A': ['D', 'U'],
              '3B': ['U', 'R'],
              '3C': ['L', 'D'],
              '3D': ['D', 'R'],
              '3E': ['L', 'R'],
              '3F': ['L', 'U', 'D'],
              '4A': ['D', 'U'],
              '4B': ['R'],
              '4C': ['L', 'R', 'U'],
              '4D': ['L', 'U'],
              '4E': ['R'],
              '4F': ['U', 'D', 'L'],
              '5A': ['D', 'R', 'U'],
              '5B': ['L', 'R'],
              '5C': ['L', 'D'],
              '5D': ['D', 'R'],
              '5E': ['L'],
              '5F': ['U', 'D'],
              '6A': ['U', 'R'],
              '6B': ['L'],
              '6C': ['U', 'R'],
              '6D': ['U', 'L'],
              '6E': ['R'],
              '6F': ['L', 'U']}
    moves6 = {'1A': ['D'],
              '1B': ['D', 'R'],
              '1C': ['L', 'D'],
              '1D': ['R'],
              '1E': ['L', 'R', 'D'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U'],
              '2B': ['D', 'U'],
              '2C': ['D', 'U'],
              '2D': ['D', 'R'],
              '2E': ['L', 'U'],
              '2F': ['U', 'D'],
              '3A': ['D', 'U', 'R'],
              '3B': ['U', 'L'],
              '3C': ['U'],
              '3D': ['D', 'U'],
              '3E': ['D', 'R'],
              '3F': ['L', 'U'],
              '4A': ['R', 'U'],
              '4B': ['L', 'D'],
              '4C': ['R', 'D'],
              '4D': ['L', 'U', 'D'],
              '4E': ['U', 'D'],
              '4F': ['D'],
              '5A': ['D', 'R'],
              '5B': ['L', 'U'],
              '5C': ['U'],
              '5D': ['D', 'U'],
              '5E': ['R', 'U'],
              '5F': ['U', 'D', 'L'],
              '6A': ['U', 'R'],
              '6B': ['L', 'R'],
              '6C': ['L', 'R'],
              '6D': ['U', 'L'],
              '6E': ['R'],
              '6F': ['L', 'U']}
    moves7 = {'1A': ['D', 'R'],
              '1B': ['L', 'R'],
              '1C': ['L', 'R'],
              '1D': ['D', 'L'],
              '1E': ['D', 'R'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U'],
              '2B': ['D', 'R'],
              '2C': ['L'],
              '2D': ['U', 'R'],
              '2E': ['L', 'U'],
              '2F': ['U', 'D'],
              '3A': ['R', 'U'],
              '3B': ['U', 'L'],
              '3C': ['R', 'D'],
              '3D': ['L'],
              '3E': ['D', 'R'],
              '3F': ['L', 'U'],
              '4A': ['D', 'R'],
              '4B': ['L', 'D'],
              '4C': ['D', 'R', 'U'],
              '4D': ['L', 'R'],
              '4E': ['L', 'U'],
              '4F': ['D'],
              '5A': ['D', 'U'],
              '5B': ['U'],
              '5C': ['U', 'R'],
              '5D': ['L', 'R'],
              '5E': ['L', 'D'],
              '5F': ['U', 'D'],
              '6A': ['U', 'R'],
              '6B': ['L', 'R'],
              '6C': ['L', 'R'],
              '6D': ['R', 'L'],
              '6E': ['R', 'L', 'U'],
              '6F': ['L', 'U']}
    moves8 = {'1A': ['D'],
              '1B': ['D', 'R'],
              '1C': ['L', 'R'],
              '1D': ['D', 'L'],
              '1E': ['D', 'R'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U', 'R'],
              '2B': ['U', 'R', 'L'],
              '2C': ['L'],
              '2D': ['U', 'R'],
              '2E': ['L', 'U'],
              '2F': ['U', 'D'],
              '3A': ['D', 'U'],
              '3B': ['D', 'R'],
              '3C': ['L', 'R'],
              '3D': ['L', 'R'],
              '3E': ['L', 'D'],
              '3F': ['U', 'D'],
              '4A': ['D', 'U'],
              '4B': ['R', 'U'],
              '4C': ['L', 'D'],
              '4D': ['R'],
              '4E': ['R', 'L', 'U'],
              '4F': ['U', 'L'],
              '5A': ['D', 'U'],
              '5B': ['D'],
              '5C': ['U', 'R'],
              '5D': ['L', 'R'],
              '5E': ['L', 'R'],
              '5F': ['L'],
              '6A': ['U', 'R'],
              '6B': ['L', 'R', 'U'],
              '6C': ['L', 'R'],
              '6D': ['R', 'L'],
              '6E': ['R', 'L'],
              '6F': ['L']}
    moves9 = {'1A': ['D'],
              '1B': ['D', 'R'],
              '1C': ['L', 'R'],
              '1D': ['L', 'R'],
              '1E': ['L', 'R', 'D'],
              '1F': ['L', 'D'],
              '2A': ['D', 'U'],
              '2B': ['D', 'U'],
              '2C': ['R', 'D'],
              '2D': ['L'],
              '2E': ['U', 'D'],
              '2F': ['U', 'D'],
              '3A': ['D', 'U', 'R'],
              '3B': ['U', 'R', 'L'],
              '3C': ['L', 'U'],
              '3D': ['D', 'R'],
              '3E': ['L', 'U'],
              '3F': ['D', 'U'],
              '4A': ['D', 'U'],
              '4B': ['D'],
              '4C': ['D', 'R'],
              '4D': ['L', 'U'],
              '4E': ['R'],
              '4F': ['U', 'D', 'L'],
              '5A': ['D', 'U'],
              '5B': ['U', 'D'],
              '5C': ['U', 'D'],
              '5D': ['D', 'R'],
              '5E': ['L', 'D'],
              '5F': ['U'],
              '6A': ['U', 'R'],
              '6B': ['L', 'U'],
              '6C': ['U', 'R'],
              '6D': ['U', 'L'],
              '6E': ['R', 'U'],
              '6F': ['L']}

    cols = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
    cols_order = ['A', 'B', 'C', 'D', 'E', 'F']
    trad = {'U': 'Cima', 'D': 'Baixo', 'L': 'Esquerda', 'R': 'Direita'}
    lab_ref = {'2A3F': moves1,
               '3F2A': moves1,
               '4B2E': moves2,
               '2E4B': moves2,
               '4D4F': moves3,
               '4F4D': moves3,
               '1A4A': moves4,
               '4A1A': moves4,
               '6D3E': moves5,
               '3E6D': moves5,
               '5C1E': moves6,
               '1E5C': moves6,
               '1B6B': moves7,
               '6B1B': moves7,
               '4C1D': moves8,
               '1D4C': moves8,
               '5A2C': moves9,
               '2C5A': moves9}

    moves = None
    while True:
        c1_lin = 'a'
        c1_col = 'a'
        while c1_lin not in ['1', '2', '3', '4', '5', '6']:
            c1_lin = input('\nDigite a linha do primeiro círculo: ').strip()
        while c1_col not in ['1', '2', '3', '4', '5', '6']:
            c1_col = input('\nDigite a coluna da primeiro círculo: ').strip()

        c2_lin = 'a'
        c2_col = 'a'
        while c2_lin not in ['1', '2', '3', '4', '5', '6']:
            c2_lin = input('\nDigite a linha do segundo círculo: ').strip()
        while c2_col not in ['1', '2', '3', '4', '5', '6']:
            c2_col = input('\nDigite a coluna do segundo círculo: ').strip()

        c1 = c1_lin + cols[c1_col]
        c2 = c2_lin + cols[c2_col]

        lab = c1 + c2
        try:
            moves = lab_ref[lab]
            break
        except KeyError:
            continue

    idx = 'a'
    col = 'a'
    while idx not in ['1', '2', '3', '4', '5', '6']:
        idx = input('\nDigite a linha da posição inicial: ').strip()
    while col not in ['1', '2', '3', '4', '5', '6']:
        col = input('\nDigite a coluna da posição inicial: ').strip()
    start_pos = idx + cols[col]

    idxf = 'a'
    colf = 'a'
    while idxf not in ['1', '2', '3', '4', '5', '6']:
        idxf = input('\nDigite a linha do objetivo: ').strip()
    while colf not in ['1', '2', '3', '4', '5', '6']:
        colf = input('\nDigite a coluna do objetivo: ').strip()
    end_pos = idxf + cols[colf]

    def moving(origin, direction, columns):
        destiny_row = None
        destiny_column = None
        eliminate = None
        if direction == 'R':
            destiny_column = columns[columns.index(origin[1]) + 1]
            destiny_row = origin[0]
            eliminate = 'L'
        elif direction == 'L':
            destiny_column = columns[columns.index(origin[1]) - 1]
            destiny_row = origin[0]
            eliminate = 'R'
        elif direction == 'U':
            destiny_row = str(int(origin[0]) - 1)
            destiny_column = origin[1]
            eliminate = 'D'
        elif direction == 'D':
            destiny_row = str(int(origin[0]) + 1)
            destiny_column = origin[1]
            eliminate = 'U'

        destiny = destiny_row + destiny_column

        return destiny, eliminate

    m = moves[start_pos][0]
    current_pos = start_pos
    seq = [start_pos]
    possible_moves = []
    turn = 0
    possible_moves.append(moves[current_pos])
    while True:
        current_pos, forbid = moving(current_pos, m, cols_order)
        seq.append(current_pos)
        if current_pos == end_pos:
            break
        moves[current_pos].remove(forbid)
        possible_moves.append(moves[current_pos])
        turn += 1
        while True:
            if len(moves[current_pos]) > 0:
                m = moves[current_pos][0]
                break
            else:
                del possible_moves[turn]
                turn -= 1
                seq.remove(current_pos)
                current_pos = seq[turn]
                possible_moves[turn].remove(possible_moves[turn][0])
                if len(moves[current_pos]) > 0:
                    m = moves[current_pos][0]
                    break
                else:
                    continue

    movements = [trad[w[0]] for w in possible_moves]
    print(', '.join(movements))


if __name__ == '__main__':
    labirinto()
