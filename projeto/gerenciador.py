import funcoes
tarefas = []
while True:
    print(""" Menu do Gerenciador de Listas de Tarefas: 
          1. Adicionar tarefa
          2. Ver Tarefas
          3. Atualizar Tarefa
          4. Completar Tarefa
          5. Deletar tarefas completadas
          6. Sair""")
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        funcoes.adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        funcoes.ver_tarefas(tarefas)
    elif escolha == "3":
        funcoes.ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        funcoes.atualizar_tarefa(tarefas,indice_tarefa,novo_nome_tarefa)
    elif escolha =="4":
        funcoes.ver_tarefas(tarefas)
        indice_tarefa= input("Digite o número da tarefa que deseja completar: ")
        funcoes.completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        funcoes.ver_tarefas(tarefas)
        funcoes.deletar_tarefas_completadas(tarefas)
    elif escolha =="6":
        break
print("Programa Finalizado")