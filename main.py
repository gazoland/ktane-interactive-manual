from PIL import Image
import os
from module_simplewires import fios_simples
from module_1234 import umdoistresquatro
from module_display import display
from module_button import botao
from module_seqwires import fios_sequencia
from module_password import senha
from module_labyrinth import labirinto
from module_compwires import fios_complicados
from module_genius import genius
from module_morse import morse
from module_led import led


def simbolos():
    direc = os.getcwd()
    symbs = direc + '\\symbols'
    symbols = os.listdir(symbs)
    for s in symbols:
        img = Image.open(symbs + '\\' + s)
        img.show()


if __name__ == '__main__':
    while 1:
        m = ''
        while m not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'fim']:
            print('\n[1] Fios   [2] Botão   [3] Símbolos\n'
                  '[4] Genius   [5] Display   [6] 1234\n'
                  '[7] Morse   [8] Fios Complicados   [9] Fios Sequência\n'
                  '[10] Labirinto   [11] Senha    [12] Led')
            m = input('Selecione o módulo de acordo com os números acima ou digite "fim" para encerrar: ').lower()

        if m == '1':
            fios_simples()

        if m == '2':
            botao()

        if m == '3':
            simbolos()

        if m == '4':
            genius()

        if m == '5':
            display()

        if m == '6':
            umdoistresquatro()

        if m == '7':
            morse()

        if m == '8':
            fios_complicados()

        if m == '9':
            fios_sequencia()

        if m == '10':
            labirinto()

        if m == '11':
            senha()

        if m == '12':
            led()

        if m == 'fim':
            print('\nO dia está salvo graças a mim.')
            break
