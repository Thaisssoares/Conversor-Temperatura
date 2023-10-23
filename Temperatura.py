from Conversor import multiplicacao
from Conversor import sub

while True:
    #Apresentação
    print('\n\n\n\t ---Conversor de temperatura--\n')
    #Menu
    print('1.multiplicacao')
    print('2.subtraçao')
    print('3.Sair')
    #Ler a opção de escolha do usuário
    op=int(input('\n opção:'))
    if op == 1 :
        print('\nSoma\n')
        #Entrada
        n1=int(input('digite um numero:'))
        n2=int(input('digite segundo numero:'))
        n3=int(input('digite terceiro numero:'))
        n4=int(input('digite quarto valor:'))
        #Processamento
        total=multiplicacao(n1,n2,n3,n4)
        #Saída
        print(f'\n {n1}*{n2}/{n3}+{n4} = {total}\n')
    elif op == 2 :
        print('\nSubtração\n')
        #Entrada
        s1=int(input('escreva um numero:'))
        s2=int(input('escreva segundo numero:'))
        s3=int(input('escreva terceiro numero:'))
        s4=int(input('escreva quarto numero'))
        #Processamento
        total2= sub(s1,s2,s3,s4)
        #Saída
        print('f\n ({s1} - {s2)\ {s3} * {s4}')
    elif op == 3:
        #Sair do sistema
        print('Bom trabalho,sair do projeto')
    else:
        print(f'\n opção {op} incorreta\n')
