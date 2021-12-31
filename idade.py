nome = input('Qual é o seu nome ? ')
idade = input('Qual é a sua idade ? ')
if int(idade) <= 20:
    print('{} você é novo !'.format(nome))
elif int(idade) <= 40:
    print('{} tá precisando ser reformada, em !!!'.format(nome))
else:
    print("Oxe, o que você está fazendo aqui neste mundo ?")
