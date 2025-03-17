import json
import time
import os

###########################################################################################################################
# Função para adicionar um item à lista de compras
###########################################################################################################################
def add_item(shoppingList, item, qtd):
    shoppingList[item] = qtd  # Adiciona o item com a quantidade informada ao dicionário
    print('Item adicionado à lista.\n')
    input('Pressione "Enter" para sair')

###########################################################################################################################
# Função para remover um item da lista de compras
###########################################################################################################################
def remove_item(shoppingList, item):
    try:
        del shoppingList[item]  # Remove o item do dicionário
        print('Item removido!')
        input('Pressione "Enter" para sair')
    except:
        print(f'O item não existe na lista.')  # Trata o caso de item inexistente
        input('Pressione "Enter" para sair')

###########################################################################################################################
# Função para visualizar os itens da lista de compras
###########################################################################################################################
def see_shopping(shoppingList):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal (Windows/Linux)
    
    # Percorre a lista e exibe os itens formatados
    for i, (item, qtd) in enumerate(shoppingList.items()):
        var = f'Item: {item.title()} | Quantidade: {qtd}'
        i += 1
        
        # Formata a exibição para separar os itens corretamente
        if i < len(shoppingList):
            print(var + ';')
        else:
            print(var + '.\n')

    input('Pressione "Enter" para sair')

###########################################################################################################################
# Função para salvar a lista de compras em um arquivo JSON
###########################################################################################################################
def save_shopping(shoppingList, fileName):
    with open(fileName, 'w') as file:
        json.dump(shoppingList, file, ensure_ascii=False)  # Salva a lista no formato JSON

###########################################################################################################################
# Função para carregar uma lista de compras de um arquivo JSON
###########################################################################################################################
def load_shopping(fileName):
    with open(fileName, 'r') as file:
        return json.load(file)  # Retorna o dicionário carregado do arquivo

###########################################################################################################################
# Função principal para gerenciar a lista de compras
###########################################################################################################################
def manage_shopping(shoppingList, fileName=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal
        
        # Opções do menu
        options = [
            '1 Adicionar item',
            '2 Remover item',
            '3 Visualizar lista',
            '4 Salvar e sair',
            '5 Sair sem salvar'
        ]
        
        for option in options:
            print(option)
            
        selectedOption = input('\nEscolha uma opção: ')
        
        ###########################################
        # Opção para adicionar um item à lista
        ###########################################
        if selectedOption == '1':
            item = input('Digite o nome do item: ')
            qtd = None
            
            # Valida a entrada para garantir que a quantidade seja um número inteiro
            while qtd is None:
                try:
                    qtd = int(input('Digite a quantidade: '))
                except:
                    print('Informe uma quantidade válida!')
                    qtd = None
            
            add_item(shoppingList, item, qtd)
        
        ###########################################
        # Opção para remover um item da lista
        ###########################################
        elif selectedOption == '2':
            item = input('Digite o nome do item: ')
            remove_item(shoppingList, item)
        
        ###########################################
        # Opção para visualizar a lista de compras
        ###########################################
        elif selectedOption == '3':
            see_shopping(shoppingList)
        
        ###########################################
        # Opção para salvar a lista e sair
        ###########################################
        elif selectedOption == '4':
            try:
                if fileName is None:
                    fileName = input('Digite o nome do arquivo para salvar: ')
                
                if not fileName.endswith('.json'):  # Garante que o arquivo tenha a extensão .json
                    fileName += '.json'
                
                save_shopping(shoppingList, fileName)
                break  # Sai do loop após salvar
            except ValueError as e:
                input(e)
                break
            
        ###########################################
        # Opção para sair sem salvar
        ###########################################
        elif selectedOption == '5':
            break
        
        ###########################################
        # Mensagem para opção inválida
        ###########################################
        else:
            print('\nOpção inválida!')
            time.sleep(1)

###########################################################################################################################
# Função principal do programa
###########################################################################################################################
def main():
    options = [
        '1 Criar uma nova lista de compras',
        '2 Carregar uma lista existente',
        '3 Sair'
    ]
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal

        for option in options:
            print(option)
        
        selectedOption = input('\nEscolha uma opção: ')
        
        ###########################################
        # Opção para criar uma nova lista de compras
        ###########################################
        if selectedOption == '1':
            shoppingList = {}  # Cria uma nova lista vazia
            manage_shopping(shoppingList)
        
        ###########################################
        # Opção para carregar uma lista existente
        ###########################################
        elif selectedOption == '2':
            os.system('cls' if os.name == 'nt' else 'clear')

            print('\nListas disponíveis:\n')
            files = [file for file in os.listdir() if file.endswith('.json')]  # Lista arquivos JSON disponíveis
            
            if not files:
                print('Nenhuma lista encontrada')
                time.sleep(2)
                continue

            for i, file in enumerate(files):
                print(f'{i + 1} - {file}')
            
            try:
                selectedList = int(input('\nEscolha uma lista para carregar (0 se nenhuma): '))
                
                if selectedList < 0 or selectedList > len(files):
                    print('\nOpção inválida!')
                    time.sleep(1)
                    continue

                if selectedList == 0:
                    continue
            except:
                print('Opção inválida')
                continue
            
            selectedFile = files[selectedList - 1]  # Obtém o nome do arquivo selecionado
            manage_shopping(load_shopping(selectedFile), selectedFile)
        
        ###########################################
        # Opção para sair do programa
        ###########################################
        elif selectedOption == '3':
            break
        
        ###########################################
        # Mensagem para opção inválida
        ###########################################
        else:
            print('\nOpção inválida!')
            time.sleep(1)

# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == '__main__':
    main()
