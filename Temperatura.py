from Conversor import fah,cel

while True:
    #Apresentação
    print('\n\n\n\t ---Conversor de temperatura Fah e Cel--\n')
    #Menu
    print('1.Fahrenheit')
    print('2.Celsius')
    print('3.Sair')
    #Ler a opção de escolha do usuário
    op=int(input('\n opção:'))
    if op == 1 :
        print('\n Fahrenheit \n')
        #Entrada
        n1=int(input('digite um numero:'))

        #Processamento
        total=fah(n1)
        #Saída
        print(f'\n {n1} = {total}\n')
    elif op == 2 :
        print('\n Celsius \n')
        #Entrada
        s1=int(input('escreva um numero:'))
        #Processamento
        total2= cel(s1)
        #Saída
        print(f'f\n {s1} = {total2}\n')
    elif op == 3:
        #Sair do sistema
        print('Bom trabalho!')
    break

else:
        print(f'\n opção {op} incorreta\n')
