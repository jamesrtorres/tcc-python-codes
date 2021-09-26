#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
info = {
    "nome": "Lançamento Vertical com Resistência do Ar",
    "autor": "James R. Torres",
    "versão": (1, 0),
    "python": (3, 8, 0),
    "descrição": "calcula o lançamento vertical com resistência do ar",
    "doc_url":
    " https://drive.google.com/drive/folders/1hmn0ImDw8OCX5bgsiax1v9DL6EzxdaEZ?usp=sharing ",
}
'''
# importação de módulos
import matplotlib.pyplot as plt
import numpy as np
from rgbcores import blue, bred, bgreen, bblue

# Apresentação.
print('')
print(bgreen(
    'Bem-vindo ao programa:'))
print('')
print(bblue('Lançamento Vertical com Resistência do Ar'))
print('')
print(bred('Digite')
      + ' ' + bgreen('Ctrl + C ou Ctrl + D')
      + ' ' + bred('para sair do programa.'))
print('')
print('')
# 1 interação com o usuário e a definição de intervalo de tempo.
while True:
    try:
        while True:
            try:
                while True:
                    try:
                        t0 = float(input('Escolha o instante inicial '
                                         'em segundos. t0 = '))
                        if t0 < 0:
                            print(bred('Digite um número positivo!'))
                            qq = input('Pressione uma tecla para'
                                       ' recomeçar...\n')
                            continue
                        else:
                            break
                    except (ValueError):
                        print(bred('Digite um número válido.'))
                print('')
                while True:
                    try:
                        tf = float(input('Escolha o instante '
                                         'final em segundos. tf = '))
                        if tf < 0:
                            print(bred('Digite um número positivo!'))
                            qq = input('Pressione uma tecla para'
                                       ' recomeçar...\n')
                            continue
                        elif t0 == tf:
                            print(bred('Digite tf diferente de t0.'))
                            qq = input('Pressione uma tecla para'
                                       ' recomeçar...\n')
                            continue
                        else:
                            break
                    except (ValueError):
                        print(bred('Digite um número válido.'))
                if t0 > tf:
                    print(bred('Você esta voltando no tempo!'))
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                print('')
                print(blue(f'Você definiu um intervalo de tempo '
                           f'Δt = {tf-t0} s.'))
                print('')
                print(bblue(f'Em quantos passos você que ir de '
                            f't0 = {t0} s até tf = {tf} s?'))
                print('')
                N = int(input('N = '))
                print('')
                if N <= 0:
                    print(bred('Escolha um número positivo e inteiro!'))
                    print('')
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    print(blue(f'A duração de cada passo'
                               f' é h = {(tf-t0)/N} s.'))
                    print('')
                    h = (tf - t0)/N
                    zeros = [0 for i in range(N + 1)]
                    t = [t0 + i*h for i in range(N + 1)]
                    break
            except (ValueError, ZeroDivisionError, EOFError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                y0 = float(input('Entre com a coordenada y em metros '
                                 '(Altura acima do solo.). y0 = '))
                print('')
                if y0 < 0:
                    print(bred('A origem está definida no solo. '
                               'Escolha um valor positivo!'))
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                vy0 = float(input('Entre com a velocidade '
                                  'inicial em m/s. vy0 = '))
                if y0 == 0 and vy0 < 0:
                    print(bred('A altura inicial é o solo. '
                               'Não é possível fazer o lançamento! '
                               'Escolha um valor positivo para velocidade!'))
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    break
            except (ValueError):
                print(bred('Digite um número válido.'))
        break
    except (KeyboardInterrupt, EOFError):
        break


# constantes.
g = 9.86

try:
    # CI do problema para o simulador.
    t = t0
    y = y0
    vy = vy0

    # variáveis tipo listas para o simulador.
    tempo = []
    posicao_y = []
    velocidade_y = []

    # CI do problema para o usuário.
    ut = t0
    uy = y0
    uvy = vy0

    # variáveis tipo listas para o usuário.
    utempo = []
    uposicao_y = []
    uvelocidade_y = []

# 4 interação com o usuário. Calcular manualmente ou simular?
    while True:
        try:
            print('')
            op = input('Escolha uma das opções:\n'
                       'a - quero simular passo-a-passo.\n'
                       'b - quero que o computador faça.\n')
            # calculaando manualmente e simulando.
            if op == 'a':
                for i in range(N + 1):
                    # atribuindo CI.
                    if i == 0:
                        print(blue('========================================'))
                        print(bblue('Condições iniciais!'))
                        print(blue('========================================'))
                        print(bred(f't{i} = {t0 + i*h}'))
                        ut = t0
                        print(blue('----------------------------------------'))
                        print(bred(f'y{i} = {y0}.'))
                        uy = y0
                        print(blue('----------------------------------------'))
                        print(bred(f'vy{i} = {vy0}.'))
                        uvy = vy0
                        print(blue('========================================'))
                        print(bblue('Fórmula de recorrência para n+1 passos!'
                                    + ' ' + bred('(eq.0)')))
                        print(blue('========================================'))
                        print(bred('tn+1 = t0 + (n+1)*h.'))
                        print(blue('----------------------------------------'))
                        print(bred('yn+1 = (yn) + (vyn)*h.'))
                        print(blue('----------------------------------------'))
                        print(bred('vyn+1 = (vyn) - g*h.'))
                        print(blue('========================================'))
                        print(blue('========================================'))
                        print(bblue('O programa já calculou o')
                              + ' ' + bred(f'passo {i+1}')
                              + ' ' + bblue('ou')
                              + ' ' + bred(f'n = {i}.')
                              + ' ' + bred('(eq.1)'))
                        print(blue('========================================'))
                        print(bred(f't{i+1} = ({t0}) + ({i+1})(h) = {t0 + h}'))
                        print(blue('----------------------------------------'))
                        print(bred(f'y{i+1} = (y{i}) + (vy{i})*(h) ='
                                   f' {y + vy*h}.'))
                        print(blue('----------------------------------------'))
                        print(bred(f'vy{i+1} = (vy{i}) - (g)*(h) ='
                                   f' {vy - g*h}.'))
                        print(blue('========================================'))

                        utempo.append(t0)
                        uposicao_y.append(y0)
                        uvelocidade_y.append(vy0)

                        utempo.append(t0 + h)
                        uposicao_y.append(y + vy*h)
                        uvelocidade_y.append(vy - g*h)

                        tempo.append(t0)
                        posicao_y.append(y0)
                        velocidade_y.append(vy0)
                    else:
                        # 5a interação com o usuário: entrando com os cálculos.
                        while True:
                            try:
                                qq = input('Pressione "enter" para '
                                           'continuar...'
                                           'ou digite "sair"'
                                           ' para finalizar.\n')
                                if qq == 'sair':
                                    break
                                else:
                                    pass
                                print('')
                                print(bgreen('Agora é sua vez!!! Siga a '
                                             'fórmula')
                                      + ' ' + bred('(eq.0)')
                                      + ' ' + bgreen('e o resultado')
                                      + ' ' + bred(f'(eq.{i})')
                                      + ' ' + bgreen('acima. \nCalcule o ')
                                      + ' ' + bred(f'passo {i+1}')
                                      + ' ' + bgreen(', isto é, ')
                                      + ' ' + bred(f'n = {i}.'))
                                print(blue('================================'))
                                print(bred(f't{i+1} = (t0) + ({i+1})*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em segundos para'
                                      f' t{i+1}. ')
                                ut = float(input(f'T{i+1} =>  '))
                                print('')
                                print(blue('================================'))
                                print(bred(f'y{i+1} = (y{i}) + (vy{i})*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em metros '
                                      f'para para y{i+1}. ')
                                uy = float(input(f'y{i+1} =>  '))
                                print('')
                                print(blue('================================'))
                                print(bred(f'vy{i+1} = (vy{i}) - ({g})*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em metros por'
                                      f' segundo para para vy{i+1}. ')
                                uvy = float(input(f'vy{i+1} =>'))
                                print('')
                                print(blue('================================'))
                                print(bgreen('Você entrou com os seguintes '
                                             'resultados para o')
                                      + ' ' + bred(f'passo {i+1}.  '
                                                   f'(eq.{i+1})'))
                                print(blue('================================'))
                                print(bred(f't{i+1} = ({t0}) + ({i+1})*(h) ='
                                           f' {ut}')
                                      )
                                print(blue('--------------------------------'))
                                print(bred(f'y{i+1} = (y{i}) + (vy{i})*(h) ='
                                           f' {uy}.'
                                           )
                                      )
                                print(blue('--------------------------------'))
                                print(bred(f'vy{i+1} = (vy{i}) - (g)*(h) ='
                                           f' {uvy}.')
                                      )
                                print(blue('================================'))
                                break
                            except (ValueError, ZeroDivisionError):
                                print(bred('Digite um número válido.'))
                        if qq == 'sair':
                            print(bgreen('Programa Finalizado pelo usuário!'))
                            break
                        else:
                            utempo.append(ut)
                            uposicao_y.append(uy)
                            uvelocidade_y.append(uvy)

                    # cálulos do simulador pelo sistema de equações.
                    t = t0 + (i+1)*h
                    y = y + vy*h
                    vy = vy - g*h
                    if y >= 0.0:
                        tempo.append(t)
                        posicao_y.append(y)
                        velocidade_y.append(vy)
                    else:
                        print(bgreen(f'Simulação terminada para {N} passos!'))
                        break
                break
            # 4a interação com o usuário: somente os cálulos do simulador.
            elif op == 'b':
                while True:
                    try:
                        gamma = float(input('Sem atrito com o ar entre com'
                                            ' γ = 0.\nCom atrito entre com '
                                            'um valor (γ > 0). Digite γ = '))
                        if gamma < 0:
                            print(bred('Digite um número positivo.'))
                            continue
                        else:
                            break
                    except (ValueError, TypeError):
                        print(bred('Digite uma opção válida.'))
                for i in range(N + 1):
                    t = t0 + i*h
                    y = y + vy*h
                    vy = vy - g*h - gamma*vy*h
                    if y >= 0.0:
                        tempo.append(t)
                        posicao_y.append(y)
                        velocidade_y.append(vy)
                    else:
                        print(bgreen(f'Simulação terminada para {N} passos!'))
                        print(bgreen('Cálculo Finalizado!'))
                        break
                break
            else:
                print(bred('Digite uma opção válida.'))
        except (ValueError, TypeError):
            print(bred('Digite uma opção válida.'))

    # Fim dos cálculos!

    if abs(posicao_y[-1] - 0.0) <= max(posicao_y)*5./100.:
        print(bred('O corpo chegou ao solo! em')
              + ' ' + bblue(f'{round(tempo[-1], 2)} segundos.'))
        print(bred('Atingiu uma altura máxima de')
              + ' ' + bblue(f'{round(max(posicao_y), 2)} metros')
              + bred(' em ') +
              bblue(f'{round(tempo[posicao_y.index(max(posicao_y))], 2)}'
                    ' segundos.'))
    else:
        print(bred('De acordo com a simulação, o corpo não chegou ao solo!!'))
        if op == 'a':
            print(bgreen('Calcule mais passos da próxima vez!!!'))
        else:
            print(bblue('Rode novamente e escolha um')
                  + ' ' + bred('N')
                  + ' ' + bblue('adequado para um')
                  + ' ' + bred('tf')
                  + ' ' + bblue('maior, para então ver o corpo chegar'
                                ' ao solo.'))
        print(bblue('A curva azul mostra a solução analítica.'))
        print(bred('Na simulação, o corpo atingiu uma altura máxima de')
              + ' ' + bblue(f'{round(max(posicao_y), 2)} metros')
              + bred(' em ') +
              bblue(f'{round(tempo[posicao_y.index(max(posicao_y))],2)}'
                    ' segundos.'))

    # criando os gráficos.
    plt.rcParams.update({'axes.titlesize': 'x-large'})
    plt.rcParams.update({'axes.labelsize': 'x-large'})
    plt.rcParams.update({'axes.labelsize': 'x-large'})
    plt.rcParams.update({'xtick.labelsize': 'large'})
    plt.rcParams.update({'ytick.labelsize': 'large'})
    plt.rcParams.update({'mathtext.default': 'regular'})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams['lines.markersize'] = 4

    # solução analítica sem resistencia do ar.

    def sy(t):
        """Função horária do espaço y."""
        return y0 + vy0*(t - t0) - 0.5*g*(t - t0)**2

    def vy(t):
        """Função horária da velocidade y."""
        return vy0 - g*(t - t0)

    # solução analítica com resistencia do ar.

    if op == 'a':
        gamma = 0.0
    else:
        pass

    gamma_gtz = round(gamma + 10e-5, 3)

    def exp_res(t):
        """Fator exponencial."""
        return ((1. - np.exp(- gamma_gtz*(t - t0)))/gamma_gtz)

    def sy_res(t):
        """Função horária do espaço y."""
        return y0 - g/gamma_gtz*(t - t0) + (vy0 + g/gamma_gtz)\
            * ((1. - np.exp(- gamma_gtz*(t - t0)))/gamma_gtz)

    def vy_res(t):
        """Função horária da velocidade y."""
        return - g/gamma_gtz + (vy0 + g/gamma_gtz)*np.exp(- gamma_gtz*(t - t0))

    # grid do tempo para solução analítica.
    timeline = np.linspace(t0, tf, 20*N)

    # solução sy(timeline) > 0.
    tempo_analitica = []
    sy_analitica = []
    vy_analitica = []
    tempo_analitica_res = []
    sy_analitica_res = []
    vy_analitica_res = []
    for time in timeline:
        if sy(time) >= 0:
            tempo_analitica.append(time)
            sy_analitica.append(sy(time))
            vy_analitica.append(vy(time))
        else:
            break
    for time in timeline:
        if sy_res(time) >= 0:
            tempo_analitica_res.append(time)
            sy_analitica_res.append(sy_res(time))
            vy_analitica_res.append(vy_res(time))
        else:
            break

    if op == 'a':
        # posição y
        plt.plot(tempo_analitica, sy_analitica, 'b-', label='Sol. Analítica')
        plt.plot(tempo, posicao_y, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uposicao_y, 'go-', label='Sol. Usuário')
        plt.title(r'Diagrama $y(t)$ vs $t$')
        plt.xlim(0, )
        plt.ylim(0, )
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()
        # velocidade y
        plt.plot(tempo_analitica, vy_analitica, 'b-', label='Sol. Analítica')
        plt.plot(tempo, velocidade_y, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uvelocidade_y, 'go-', label='Sol. Usuário')
        plt.xlim(tempo_analitica[0], )
        plt.title(r'Diagrama $v_{y}(t)$ vs $t$')
        plt.xlabel('t(s)')
        plt.ylabel('v_{y}(m/s)')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        # posição y
        plt.plot(tempo, posicao_y, 'ro-', label=f'Sol. Simulador γ = {gamma}')
        plt.plot(tempo_analitica, sy_analitica, 'b-',
                 label='Sol. Analítica γ = 0.0')
        plt.plot(tempo_analitica_res, sy_analitica_res, 'g-',
                 label=f'Sol. Analítica γ = {gamma_gtz}')
        plt.title(r'Diagrama $y(t)$ vs $t$')
        plt.xlim(0, )
        plt.ylim(0, )
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()
        # velocidade y
        plt.plot(tempo, velocidade_y, 'ro-', label=f'Sol. Simulador '
                 f'γ = {gamma}')
        plt.plot(tempo_analitica, vy_analitica, 'b-',
                 label='Sol. Analítica γ = 0.0')
        plt.plot(tempo_analitica_res, vy_analitica_res, 'g-',
                 label=f'Sol. Analítica γ = {gamma_gtz}')
        plt.xlim(tempo_analitica[0], )
        plt.title(r'Diagrama $v_{y}(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$v_{y}(m/s)$')
        plt.legend()
        plt.grid(True)
        plt.show()
    print(bgreen('Programa Finalizado!'))

except (NameError, KeyboardInterrupt, EOFError):
    print(bred('\nPrograma interrompido!'))
    pass
