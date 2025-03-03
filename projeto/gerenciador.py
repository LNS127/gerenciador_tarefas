def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa ={"tarefa": nome_tarefa, "Completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!!!")
    return
def ver_tarefas(tarefas):
    print("\n Lista de tarefas")
    for indice, tarefa in enumerate (tarefas, start=1):
        status = "✓" if tarefa ==["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return
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
        adicionar_tarefa(tarefas, nome_tarefa)
    if escolha == "2":
        ver_tarefas(tarefas)
    elif escolha =="6":
        break
print("Programa Finalizado")