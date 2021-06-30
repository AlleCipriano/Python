from time import sleep
from random import randint
from datetime import date
atual = date.today().year
print('Ola')
sleep(0.5)
print('Sou seu dispositivo!')
sleep(0.5)
nome = str(input('Qual seu nome? '))
sleep(0.5)
print('Ola {}, Prazer em conhece-lo.'.format(nome))
sleep(0.5)
print('Meu nome é One')
sleep(0.5)
print('Por enquanto posso te ajudar nas seguintes opções: ')
sleep(0.5)
opcao = 0
while opcao != 6:
    print('+=' * 42)
    print('''Escolha sua opção:
    [ 1 ] Gerador de PA
    [ 2 ] Sequencia Fibonacci
    [ 3 ] Jogar Jo-Ken-Pô
    [ 4 ] Par ou Impar
    [ 5 ] Maior / Menor
    [ 6 ] Finalizar o Dialogo''')
    opcao = int(input('Escolha o que deseja: '))
    if opcao == 1:
        print('Vou calcular uma PA para você.')
        print('-=' * 42)
        print('''PROGRESSÃO ARITMÉTICA
        Uma progressão aritmética é uma sequência numérica em que cada termo, 
        a partir do segundo, é igual à soma do termo anterior com uma constante r. 
        O número r é chamado de razão ou diferença comum da progressão aritmética.''')
        print('-=' * 42)
        print('Para finalizar o processo do gerador de PA basta digitar o numero zero e clicar enter.')
        print('-=' * 42)
        print('{:^80}'.format('GERADOR DE PA'))
        print('-=' * 42)
        primtermo = int(input("Digite o primeiro termo: "))
        razao = int(input('Digite a razão: '))
        mais = int(input('Digite o total de termos a serem exibidos: '))
        termo = primtermo
        cont = 1
        total = 0
        while mais != 0:
            total = total + mais
            while cont <= total:
                print('{} => '.format(termo), end='')
                termo += razao
                cont += 1
            print('PAUSA')
            mais = int(input('Quantos numeros você quer mostrar a mais? '))
        print('A PA foi encerrada com um total de {} termo(s).'.format(total))
        print('FIM DA EXECUÇÃO DO GERADOR DE P.A.')
    elif opcao == 2:
        print('Teste 2')
        print('=' * 80)
        print('{:^80}'.format('SEQUENCIA FIBONACCI'))
        print('=' * 80)
        n = int(input('Quantos termos vc quer mostrar: '))
        t1 = 0
        t2 = 1
        print('{} - {}'.format(t1, t2), end='')
        cont = 3
        while cont <= n:
            t3 = t1 + t2
            print(' => {}'.format(t3), end='')
            t1 = t2
            t2 = t3
            cont += 1
        print(' = Fim')
    elif opcao == 3:
        print('Teste 3')
        print('+=' * 42)
        print('{:^80}'.format(' \033[1:34mJÓ-KEN-PÔ\033[m '))
        print('+=' * 42)
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        print('''Escolha uma opção:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')
        print('+=' * 42)
        jogador = int(input('Qual é sua jogada? '))
        if jogador != 0 and jogador != 1 and jogador != 2:
            print('Jogada INVALIDA. Tente Novamente.')
        else:
            print('+=' * 42)
            sleep(1)
            print('{:^40}'.format(' \033[1:32mJÓ\033[m '))
            sleep(1)
            print('{:^40}'.format(' \033[1:33mKEN\033[m '))
            sleep(1)
            print('{:^40}'.format(' \033[1:34mPÔ\033[m '))
            print('+=' * 42)
            print('O computador escolheu \033[1:33m{}\033[m'.format(itens[computador]))
            print('O Jogador escolheu \033[1:34m{}\033[m'.format(itens[jogador]))
            print('+=' * 42)
            print('{:^42}'.format(' \033[1:35mPROCESSANDO\033[m '))
            sleep(2)
            if computador == 0:
                if jogador == 0:
                    print('EMPATE')
                elif jogador == 1:
                    print('\033[1:32mJOGADOR VENCE\033[m')
                elif jogador == 2:
                    print('\033[1:31mCOMPUTADOR VENCE\033[m')
            elif computador == 1:
                if jogador == 0:
                    print('\033[1:31mCOMPUTADOR VENCE\033[m')
                elif jogador == 1:
                    print('EMPATE')
                elif jogador == 2:
                    print('\033[1:32mJOGADOR VENCE\033[m')
            elif computador == 2:
                if jogador == 0:
                    print('\033[1:32mJOGADOR VENCE\033[m')
                elif jogador == 1:
                    print('\033[1:31mCOMPUTADOR VENCE\033[m')
                elif jogador == 2:
                    print('EMPATE')
        print('Fim do Jogo')
    elif opcao == 4:
        print('Boa Sorte')
        v = 0
        while True:
            jogador = int(input('Digite um numero de 1 a 10: '))
            comp = randint(0, 10)
            total = comp + jogador
            tipo = ' '
            while tipo not in 'PI':
                tipo = str(input('Par ou Impar: [P/I]: ')).strip().upper()[0]
            print(f'Voce jogou {jogador} e o computador jogou {comp}. Total {total}')
            print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
            if tipo == 'P':
                if total % 2 == 0:
                    print('Você Venceu!')
                    v += 1
                else:
                    print('Você Perdeu!')
                    break
            elif tipo == 'I':
                if total % 2 == 1:
                    print('Você Venceu!')
                    v += 1
                else:
                    print('Você perdeu')
                    break
            print('Vamos jogar novamente...')
        print(f'GAME OVER! Você ganhou {v} vezes')
    elif opcao == 5:
        print('Teste 5')
    elif opcao == 6:
        print('FINALIZANDO...')
        print('=' * 80)
        sleep(0.5)
        print('Obrigado.')
    else:
        print('Opção Invalida. Tente Novamente')
print('Foi bom falar com você, {}'.format(nome))
