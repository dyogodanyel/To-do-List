tarefa = [] #onde vai armazenar as informacoes

def nova_tarefa():
    adicionar_tarefa = input("Digite sua tarefa a ser feita: ") #variavel para armazenar a tarefa
    tarefa.append(adicionar_tarefa) #adicionar na variavel de lista para armazenar as informações
    print(f"A Tarefa '{adicionar_tarefa}' foi adicionada!") 
    
def deletar_tarefa():
    mostrar_tarefa() #mostrar as tarefas registradas
    try: # tente rodar esse codigo
        apagar_tarefa = int(input("Digite o número da tarefa que deseja deletar: "))
        if apagar_tarefa >= 0 and apagar_tarefa < len(tarefa): #se a posicao que quer deletar for menor que 0 ou nao estiver na lista
            tarefa.pop(apagar_tarefa) #apague da lista o parametro em parenteses
            print(f"A tarefa {apagar_tarefa} foi deletada com sucesso.")
        else:
            print(f"A tarefa {apagar_tarefa} não foi localizada.")
    except: #se nao rodar, mostre a seguinte mensagem
        print("Digite um número válido")
    
def mostrar_tarefa():
    if not tarefa: #se nao tiver nada em tarefas
        print("Sem tarefas registradas.")
    else: #se tiver
        print("Tarefas: ")
        for index, adicionar_tarefa in enumerate(tarefa): #numerar cada tarefa
            print(f"Tarefa #{index+1}. {adicionar_tarefa}") # +1 para ser a partir do numero 1

    

if __name__ == "__main__":
    print("To do list - App")
    while True:
        print("\n")
        print("Selecione uma das opções abaixo")
        print("------------------------------------------")
        print("1. Adicionar uma nova tarefa")
        print("2. Deletar uma tarefa")
        print("3. Mostrar todas tarefas")
        print("4. Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            nova_tarefa()
        elif opcao == 2:
            deletar_tarefa()
        elif opcao == 3:
            mostrar_tarefa()
        elif opcao == 4:
            break
        else:
            print("Número inválido. Selecione uma das opções disponíveis novamente.")
            
    print("Até uma próxima 😉")