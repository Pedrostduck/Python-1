print ('duckzado\n')

print ('1. Cadastrar Restaurante')
print ('2. Listar Restaurante')
print ('3. Ativar Restaurante')
print ('4. Sair\n')

opcao_escolhida = int(input('Escolha uma Opção: '))
print(f'Você escolheu a opção {opcao_escolhida}')



if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurante')
elif opcao_escolhida == 3:
    print('Ativar Restaurante')
else:
    print('Encerrando o Programa')



