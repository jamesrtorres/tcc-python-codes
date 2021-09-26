#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
info = {
    'nome': 'Lançamento Vertical com Resistência do Ar e Quiques',
    'autor': 'James R. Torres',
    'versão': (1, 0),
    'python': (3, 8, 0),
    'descrição': 'calcula o lançamento de projétil com'
                ' resistência do ar e ventos'
    'doc_url':
    'https://drive.google.com/drive/folders/1hmn0ImDw8OCX5bgsiax1v9DL6EzxdaEZ?usp=sharing',
}
'''

# importação de modulos
import matplotlib.pyplot as plt
import numpy as np
from rgbcores import blue, bred, bgreen, bblue

# Apresentação.

print('')
print(bgreen(
    'Bem-vindo ao programa:'))
print('')
print(bblue('Lançamento de Projétil com Resistência do Ar e Ventos'))
print('')
print(bred('Digite')
      + ' ' + bgreen('Ctrl + C ou Ctrl + D')
      + ' ' + bred('para sair do programa.'))
print('')
print('')

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
                x0 = float(input('Entre com a coordenada x em metros. x0 = '))
                print('')
                break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                y0 = float(input('Entre com a coordenada y em metros '
                                 '(Altura acima do solo). y0 = '))
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
                v0 = float(input('Entre com a velocidade'
                                 ' inicial em m/s. v0 = '))
                print('')
                if v0 < 0:
                    print(bred('Escolha um valor positivo para velocidade!'))
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                teta = float(input('Entre com o ângulo'
                                   ' inicial em graus. θ = '))
                vx0 = v0*np.cos(teta*np.pi/180.0)
                vy0 = v0*np.sin(teta*np.pi/180.0)
                print('')
                break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                w0 = float(input('Entre com a velocidade'
                                 ' inicial em m/s. w0 = '))
                print('')
                if w0 < 0:
                    print(bred('Escolha um valor positivo para velocidade!'))
                    qq = input('Pressione uma tecla para recomeçar...\n')
                    continue
                else:
                    break
            except (ValueError):
                print(bred('Digite um número válido.'))
        while True:
            try:
                delta = float(input('Entre com o ângulo'
                                    ' inicial em graus. δ = '))
                wx0 = w0*np.cos(delta*np.pi/180.0)
                wy0 = w0*np.sin(delta*np.pi/180.0)
                print('')
                break
            except (ValueError):
                print(bred('Digite um número válido.'))
        break
    except (KeyboardInterrupt, EOFError):
        break

# constantes, CI e variáveis.

# constantes.
g = 9.86

try:
    # CI do problema para o simulador.
    t = t0
    y = y0
    x = x0
    vx = vx0
    vy = vy0

    # variáveis tipo listas para o simulador.
    tempo = []
    posicao_x = []
    posicao_y = []
    velocidade_x = []
    velocidade_y = []

    # CI do problema para o usuário.
    ut = t0
    uy = y0
    ux = x0
    uvx = vx0
    uvy = vy0

    # variáveis tipo listas para o usuário.
    utempo = []
    uposicao_x = []
    uposicao_y = []
    uvelocidade_x = []
    uvelocidade_y = []

    # 4a interação com o usuário: calcular manualmente ou simular?
    while True:
        try:
            op = input('Escolha uma das opções:\n'
                       'a - quero simular passo-a-passo.\n'
                       'b - quero que o computador faça.\n')
            # calculaando manualmente e simulando.
            if op == 'a':
                for i in range(N + 1):
                    if i == 0:
                        print(blue('========================================'))
                        print('Condições iniciais!')
                        print(blue('========================================'))
                        print(bred(f't{i} = {t0 + i*h}'))
                        ut = t0
                        print(blue('----------------------------------------'))
                        print(bred(f'x{i} = {x0}.'))
                        ux = x0
                        print(bred(f'y{i} = {y0}.'))
                        uy = y0
                        print(blue('----------------------------------------'))
                        print(bred(f'vx{i} = {vx0}.'))
                        uvx = vx0
                        print(bred(f'vy{i} = {vy0}.'))
                        uvy = vy0
                        print(blue('========================================'))
                        print(bblue('Fórmula de recorrência para n+1 passos!'
                                    + ' ' + bred('(eq.0)')))
                        print(blue('========================================'))
                        print(bred('tn+1 = t0 + (n+1)*h.'))
                        print(blue('----------------------------------------'))
                        print(bred('xn+1 = (xn) + vx0*h.'))
                        print(bred('yn+1 = (yn) + (vyn)*h.'))
                        print(blue('----------------------------------------'))
                        print(bred('vxn+1 = (vxn).'))
                        print(bred('vyn+1 = (vyn) - g*h.'))
                        print(blue('========================================'))
                        print(bblue('O programa já calculou o')
                              + ' ' + bred(f'passo {i+1}')
                              + ' ' + bblue('ou')
                              + ' ' + bred(f'n = {i}.')
                              + ' ' + bred('(eq.1)'))
                        print(blue('========================================'))
                        print(bred(f't{i+1} = ({t0}) + ({i+1})(h) = {t0 + h}'))
                        print(blue('----------------------------------------'))
                        print(bred(f'x{i+1} = (x{i}) + (vx{i})*(h) ='
                                   f' {x + vx0*h}.')
                              )
                        print(blue('----------------------------------------'))
                        print(bred(f'y{i+1} = (y{i}) + (vy{i})*(h) ='
                                   f' {y + vy*h}.'))
                        print(blue('----------------------------------------'))
                        print(bred(f'vx{i+1} = (vx0) = {vx0}.'))
                        print(blue('----------------------------------------'))
                        print(bred(f'vy{i+1} = (vy{i}) - (g)*(h) ='
                                   f' {vy - g*h}.'))
                        print(blue('========================================'))

                        utempo.append(t0)
                        uposicao_x.append(x0)
                        uposicao_y.append(y0)
                        uvelocidade_x.append(vx0)
                        uvelocidade_y.append(vy0)

                        utempo.append(t0 + h)
                        uposicao_x.append(x + vy0*h)
                        uposicao_y.append(y + vy*h)
                        uvelocidade_x.append(vx0)
                        uvelocidade_y.append(vy - g*h)

                        tempo.append(t0)
                        posicao_x.append(x0)
                        posicao_y.append(y0)
                        velocidade_x.append(vx0)
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
                                print(bred(f'x{i+1} = (x{i}) + (vx0)*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em metros para '
                                      f' x{i+1}. ')
                                ux = float(input(f'x{i+1} =>  '))
                                print('')
                                print(blue('================================'))
                                print(bred(f'y{i+1} = (y{i}) + (vy{i})*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em metros para '
                                      f' y{i+1}. ')
                                uy = float(input(f'y{i+1} =>  '))
                                print('')
                                print(blue('================================'))
                                print(bred(f'vx{i+1} = (vx0) = ?'))
                                print('')
                                print(f'Escreva sua resposta em metros por '
                                      f'segundo para para vx{i+1}. ')
                                uvx = float(input(f'vx{i+1} =>'))
                                print('')
                                print(blue('================================'))
                                print(bred(f'vy{i+1} = (vy{i}) - ({g})*({h}) ='
                                           f' ?'))
                                print('')
                                print(f'Escreva sua resposta em metros por '
                                      f'segundo para para vy{i+1}. ')
                                uvy = float(input(f'vy{i+1} =>'))
                                print('')
                                print(blue('================================'))
                                print(bgreen('Você entrou com os seguintes '
                                             'resultados para o')
                                      + ' ' + bred(f'passo {i+1}.  (eq.{i+1})')
                                      )
                                print(blue('================================'))
                                print(bred(f't{i+1} = ({t0}) + ({i+1})*(h) ='
                                           f' {ut}')
                                      )
                                print(blue('--------------------------------'))
                                print(bred(f'x{i+1} = (x{i}) + (vx{i})*(h) ='
                                           f' {ux}.'))
                                print(blue('--------------------------------'))
                                print(bred(f'y{i+1} = (y{i}) + (vy{i})*(h) ='
                                           f' {uy}.'))
                                print(blue('--------------------------------'))
                                print(bred(f'vx{i+1} = (vx{i}) - (g)*(h) ='
                                           f' {uvx}.')
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
                            uposicao_x.append(ux)
                            uposicao_y.append(uy)
                            uvelocidade_x.append(uvx)
                            uvelocidade_y.append(uvy)

                    # cálulos do simulador pelo sistema de equações.
                    t = t0 + (i+1)*h
                    x = x + vx*h
                    y = y + vy*h
                    vx = vx
                    vy = vy - g*h
                    if y >= 0.0:
                        tempo.append(t)
                        posicao_x.append(x)
                        posicao_y.append(y)
                        velocidade_x.append(vx)
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
                    x = x + vx*h
                    y = y + vy*h
                    vx = vx - gamma*(vx - wx0)*h
                    vy = vy - g*h - gamma*(vy - wy0)*h
                    if y >= 0.0:
                        tempo.append(t)
                        posicao_x.append(x)
                        posicao_y.append(y)
                        velocidade_x.append(vx)
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
        print(bred('O projétil chegou ao solo! em')
              + ' ' + bblue(f'{round(tempo[-1], 2)} segundos.'))
        print(bred('O projétil obteve o alcance máximo de')
              + ' ' + bblue(f'{round(posicao_x[-1] - posicao_x[0], 2)}'
                            f' metros.'))
        print(bred('Atingiu uma altura máxima de')
              + ' ' + bblue(f'{round(max(posicao_y), 2)} metros')
              + bred(' em ')
              + bblue(f'{round(tempo[posicao_y.index(max(posicao_y))], 2)}'
                      f' segundos.'))
    else:
        print(bred('O projétil não chegou ao solo!!'))
        print(bred('Atingiu uma altura máxima de')
              + ' ' + bblue(f'{round(max(posicao_y), 2)} metros')
              + bred(' em ')
              + bblue(f'{round(tempo[posicao_y.index(max(posicao_y))],2)}'
                      f' segundos.'))
        print(bblue('Rode novamente e escolha um')
              + ' ' + bred('N')
              + ' ' + bblue('adequado para um')
              + ' ' + bred('tf')
              + ' ' + bblue('maior, para então ver o corpo chegar ao solo!!!'))

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

    def sx(t):
        """Função horária do espaço x."""
        return x0 + vx0*(t - t0)

    def sy(t):
        """Função horária do espaço y."""
        return y0 + vy0*(t - t0) - 0.5*g*(t - t0)**2

    def vy(t):
        """Função horária da velocidade y."""
        return vy0 - g*(t - t0)

    # solução analítica com resistencia do ar e ventos.
    gamma_gtz = round(gamma + 10e-5, 3)

    def exp_res(t):
        """Fator exponencial."""
        return ((1. - np.exp(- gamma_gtz*(t)))/gamma_gtz)

    def sx_res(t):
        """Função horária do espaço x."""
        # return x0 + vx0*exp_res(t)
        return x0 + wx0*(t - t0) + (vx0 - wx0)*exp_res(t - t0)

    def sy_res(t):
        """Função horária do espaço y."""
        # return y0 + (vy0 + g/gamma_gtz)*exp_res(t) - g/gamma_gtz*(t - t0)
        return y0 - (g - gamma*wy0)/gamma_gtz*(t - t0) \
            + ((g - gamma_gtz*wy0)/gamma_gtz + vy0)*exp_res(t - t0)

    def vx_res(t):
        """Função horária da velocidade y."""
        # return vx0*np.exp(-gamma_gtz*(t - t0))
        return wx0*(1.0 - np.exp(- gamma_gtz*(t - t0))) \
            + vx0*np.exp(- gamma_gtz*(t - t0))

    def vy_res(t):
        """Função horária da velocidade y."""
        # return (vy0 + g/gamma_gtz)*np.exp(-gamma_gtz*(t - t0)) - g/gamma_gtz
        return - ((g - gamma_gtz*wy0)/gamma_gtz) \
            + ((g - gamma_gtz*wy0)/gamma_gtz
               + vy0)*np.exp(- gamma_gtz*(t - t0))

    # grid do tempo para solução analítica.
    timeline = np.linspace(t0, tf, 20*N)

    # solução sy(timeline) > 0.
    tempo_analitica = []
    sx_analitica = []
    sy_analitica = []
    vx_analitica = []
    vy_analitica = []
    for time in timeline:
        if sy(time) >= 0:
            tempo_analitica.append(time)
            sx_analitica.append(sx(time))
            sy_analitica.append(sy(time))
            vx_analitica.append(vx0)
            vy_analitica.append(vy(time))
        else:
            break

    tempo_analitica_res = []
    sx_analitica_res = []
    sy_analitica_res = []
    vx_analitica_res = []
    vy_analitica_res = []
    for time in timeline:
        if sy_res(time) >= 0:
            tempo_analitica_res.append(time)
            sx_analitica_res.append(sx_res(time))
            sy_analitica_res.append(sy_res(time))
            vx_analitica_res.append(vx_res(time))
            vy_analitica_res.append(vy_res(time))
        else:
            break

    if op == 'a':
        # trajetória
        plt.plot(posicao_x, posicao_y, 'ro-', label='Sol. Simulador')
        plt.plot(uposicao_x, uposicao_y, 'go-', label='Sol. Usuário')
        plt.plot(sx_analitica, sy_analitica, 'b-', label='Sol. Analítica')
        plt.title(r'Trajetória $y(t)$ vs $x(t)$')
        plt.xlim()
        plt.ylim(0, )
        plt.xlabel(r'$x(m)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram posicao x vs tempo
        plt.plot(tempo, posicao_x, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uposicao_x, 'go-', label='Sol. Usuário')
        plt.plot(tempo_analitica, sx_analitica, 'b-', label='Sol. Analítica')
        plt.xlim(tempo_analitica[0],)
        plt.title(r'Diagrama $x(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$x(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram posicao y vs tempo
        plt.plot(tempo, posicao_y, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uposicao_y, 'go-', label='Sol. Usuário')
        plt.plot(tempo_analitica, sy_analitica, 'b-', label='Sol. Analítica')
        plt.xlim(tempo_analitica[0],)
        plt.title(r'Diagrama $y(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram velocidade x vs tempo
        plt.plot(tempo, velocidade_x, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uvelocidade_x, 'go-', label='Sol. Usuário')
        plt.plot(tempo_analitica, vx_analitica, 'b-', label='Sol. Analítica')
        plt.xlim(tempo_analitica[0],)
        plt.title(r'Diagrama $v_x(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$v_{x}(m/s)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram velocidade y vs tempo
        plt.plot(tempo, velocidade_y, 'ro-', label='Sol. Simulador')
        plt.plot(utempo, uvelocidade_y, 'go-', label='Sol. Usuário')
        plt.plot(tempo_analitica, vy_analitica, 'b-', label='Sol. Analítica')
        plt.xlim(tempo_analitica[0],)
        plt.title(r'Diagrama $v_{y}(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$v_{y}(m/s)$')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        # trajetória
        plt.plot(posicao_x, posicao_y, 'ro-', label=f'Sol. Simulador; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.plot(sx_analitica, sy_analitica, 'b-',
                 label=r'Sol. Analítica $\gamma$  = 0.0;  $w_{0}$ = 0.0')
        plt.plot(sx_analitica_res, sy_analitica_res, 'g-',
                 label=rf'Sol. Analítica; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.title(r'Trajetória $y(t)$ vs $x(t)$')
        plt.xlim()
        plt.ylim(0, )
        plt.xlabel(r'$x(m)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram posicao x vs tempo
        plt.plot(tempo, posicao_x, 'ro-', label=f'Sol. Simulador; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.plot(tempo_analitica, sx_analitica, 'b-',
                 label=r'Sol. Analítica $\gamma$  = 0.0')
        plt.plot(tempo_analitica_res, sx_analitica_res, 'g-',
                 label=rf'Sol. Analítica; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.xlim(tempo_analitica[0],)
        plt.title(r'Diagrama $x(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$x(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram posicao y vs tempo
        plt.plot(tempo, posicao_y, 'ro-', label=f'Sol. Simulador; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.plot(tempo_analitica, sy_analitica, 'b-',
                 label=r'Sol. Analítica $\gamma$  = 0.0')
        plt.plot(tempo_analitica_res, sy_analitica_res, 'g-',
                 label=rf'Sol. Analítica; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.xlim(tempo_analitica[0], )
        plt.title(r'Diagrama $y(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$y(m)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram velocidade x vs tempo
        plt.plot(tempo, velocidade_x, 'ro-', label=f'Sol. Simulador; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.plot(tempo_analitica, vx_analitica, 'b-',
                 label=r'Sol. Analítica $\gamma$  = 0.0')
        plt.plot(tempo_analitica_res, vx_analitica_res, 'g-',
                 label=rf'Sol. Analítica; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.xlim(tempo_analitica[0], )
        plt.ylim()
        plt.title(r'Diagrama $v_{x}(t)$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$v_{x}(m/s)$')
        plt.legend()
        plt.grid(True)
        plt.show()

        # diagram velocidade y vs tempo
        plt.plot(tempo, velocidade_y, 'ro-', label=f'Sol. Simulador; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.plot(tempo_analitica, vy_analitica, 'b-',
                 label=r'Sol. Analítica $\gamma$  = 0.0')
        plt.plot(tempo_analitica_res, vy_analitica_res, 'g-',
                 label=rf'Sol. Analítica; '
                 rf'$\gamma$  = {gamma}; '
                 rf' $w_{0}$ = {w0} m/s; '
                 rf'$\delta$ = {delta}$^\circ$')
        plt.xlim(tempo_analitica[0], )
        plt.title(r'Diagrama $v_y$ vs $t$')
        plt.xlabel(r'$t(s)$')
        plt.ylabel(r'$v_{y}(m/s)$')
        plt.legend()
        plt.grid(True)
        plt.show()
    print(bgreen('Programa Finalizado!'))

except (NameError, KeyboardInterrupt, EOFError):
    print(bred('\nPrograma interrompido!'))
    pass
