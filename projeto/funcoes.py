def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa ={"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!!!")
    return
def ver_tarefas(tarefas):
    print("\n Lista de tarefas")
    for indice, tarefa in enumerate (tarefas, start=1):
        status = "✓" if tarefa ["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return
def atualizar_tarefa(tarefas, indice_tarefa,novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} autalizada para {novo_nome_tarefa}")
    else:
        print("Índice de tarefa inválido")
    return
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("tarefas completadas foram deletadas")