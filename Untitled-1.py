class Tarefa:
    def __init__(self, descricao, concluida=False):
        self.descricao = descricao
        self.concluida = concluida

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def exibir_tarefas(self):
        for index, tarefa in enumerate(self.tarefas, 1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{index}. {tarefa.descricao} - {status}")

    def marcar_concluida(self, numero_tarefa):
        if 1 <= numero_tarefa <= len(self.tarefas):
            self.tarefas[numero_tarefa - 1].concluida = True
            print(f"Tarefa {numero_tarefa} marcada como concluída.")
        else:
            print("Número de tarefa inválido.")

# Criando uma lista de tarefas
lista_tarefas = ListaDeTarefas()

# Adicionando tarefas
lista_tarefas.adicionar_tarefa(Tarefa("Estudar Python"))
lista_tarefas.adicionar_tarefa(Tarefa("Fazer exercícios de matemática"))
lista_tarefas.adicionar_tarefa(Tarefa("Ler um livro"))

# Exibindo as tarefas
print("Tarefas antes da conclusão:")
lista_tarefas.exibir_tarefas()

# Marcando a primeira tarefa como concluída
lista_tarefas.marcar_concluida(1)

# Exibindo as tarefas novamente após a conclusão
print("\nTarefas após a conclusão:")
lista_tarefas.exibir_tarefas()
