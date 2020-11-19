print('Olá, Bem-Vindo ao Jokenpo')
nome_1 = input('Insira o nome do primeiro jogador:')
print('Muito prazer, {}'.format(nome_1.capitalize()))
nome_2 = input('Insira o nome do segundo jogador:')
print('Muito prazer, {}'.format(nome_2.capitalize()))
print('Agora, escolha qual será sua jogada')
def menu_jokenpo(): 
    print("""
			(1) = Pedra
			(2) = Papel
			(3) = Tesoura
		""")
menu_jokenpo()
partida=0
pontos_nome_1=0
pontos_nome_2=0
points=0
venc='ninguém'
while partida < 4:
    escolha_1 = input(print('Qual será a sua escolha, {} ?'.format(nome_1.capitalize())))
    escolha_2 = input(print('Qual será a sua escolha, {} ?'.format(nome_2.capitalize())))
    if escolha_1 == '1' and escolha_2 == '1':
        pontos_nome_2+=0
        pontos_nome_1+=0       
        partida += 1
    elif escolha_1 == '2' and escolha_2 == '2':
        pontos_nome_2+=0
        pontos_nome_1+=0       
        partida += 1
    elif escolha_1 == '3' and escolha_2 == '3':
        pontos_nome_2+=0
        pontos_nome_1+=0       
        partida += 1
    elif escolha_1 == '1' and escolha_2 == '2':
        pontos_nome_2+=1
        pontos_nome_1+=0       
        partida += 1
    elif escolha_1 == '1' and escolha_2 == '3':
        pontos_nome_2+=0
        pontos_nome_1+=1      
        partida += 1
    elif escolha_1 == '2' and escolha_2 == '1':
        pontos_nome_2+=0
        pontos_nome_1+=1       
        partida += 1
    elif escolha_1 == '2' and escolha_2 == '3':
        pontos_nome_2+=1
        pontos_nome_1+=0       
        partida += 1
    elif escolha_1 == '3' and escolha_2 == '1':
        pontos_nome_2+= 1
        pontos_nome_1+= 0       
        partida += 1
    elif escolha_1 == '3' and escolha_2 == '2':
        pontos_nome_2+=0
        pontos_nome_1+=1      
        partida += 1
    if partida == 4:
        break    
    if pontos_nome_2 == 3 and pontos_nome_1 == 0:
        points=pontos_nome_2
        venc = nome_2
        break
    elif pontos_nome_1 == 2 and pontos_nome_2 == 0:
        points=pontos_nome_1
        venc = nome_1
        break
    elif pontos_nome_2 == 2 and pontos_nome_1 == 1:
        points=pontos_nome_2
        venc = nome_2
        break
print('O vencedor é', venc, 'com', points, 'pontos, em ', partida, 'rodadas') 
