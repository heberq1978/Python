n1 = int(input('Digite o número: '))
operacao = input('Digite a operação: ')
n2 = int(input('Digite outro número: '))
if operacao == str('+'):
    print(n1 + n2)
elif operacao == str('-'):
    print(n1-n2)
elif operacao == str('*'):
    print(n1*n2)
elif operacao == str('/'):
    print(n1/n2)
else:
    print('Algo deu errado.')
