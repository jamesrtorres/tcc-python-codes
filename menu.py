#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
info = {
    "nome": "Lançamento de Projétil com Resistência do Ar",
    "autor": "James R. Torres",
    "versão": (1, 0),
    "python": (3, 0, 0),
    "descrição": "calcula lançamento de projétil com resistência do ar",
    "doc_url":
    " https://drive.google.com/drive/folders/1hmn0ImDw8OCX5bgsiax1v9DL6EzxdaEZ?usp=sharing ",
}
'''


from rgbcores import bblue, bred, bgreen,bred
while True:
    try:
        while True:
            print('')
            print(bred('Digite')
              + ' ' + bgreen('Ctrl + C ou Ctrl + D')
              + ' ' + bred('para sair do programa.'))
            print('') 
            print(bblue('a - Lançamento vertical.\n'
                        'b - Lançamento vertical com resistência do ar. \n'
                        'c - Lançamento vertical com resistência do ar '
                        'e quiques.\n'
                        'd - Lançamento de projétil.\n'
                        'e - Lançamento de projétil com resistência do ar.\n'
                        'f - Lançamento de projétil com resistência do ar '
                        'e ventos.\n'
                        'g - Lançamento de projétil com resistência do ar, '
                        'ventos e quiques.\n'))
            op = str(input('Escolha uma das opções!\n'))
            while True:
                try:
                    if op == 'a':
                        exec(open('lancamento_vertical.py').read())
                        break
                    elif op == 'b':
                        exec(open('lancamento_vertical'
                                  '_resistencia.py').read())
                        break
                    elif op == 'c':
                        exec(open('lancamento_vertical_resistencia'
                                  '_quique.py').read())
                        break
                    elif op == 'd':
                        exec(open('lancamento_projetil.py').read())
                        break
                    elif op == 'e':
                        exec(open('lancamento_projetil_resistencia.py').read())
                        break
                    elif op == 'f':
                        exec(open('lancamento_projetil_resistencia'
                                  '_ventos.py').read())
                        break
                    elif op == 'g':
                        exec(open('lancamento_projetil_resistencia'
                                  '_ventos_quique.py').read())
                        break
                    else:
                        break
                except (ValueError, TypeError):
                    print(bred('\nPrograma interrompido!'))
    except (ValueError, NameError, KeyboardInterrupt, EOFError):
        print(bred('\nPrograma interrompido!'))
        break
        if __name__ == "__main__":
            print('')

