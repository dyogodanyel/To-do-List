# 📝 To-Do List em Python

Este é um projeto simples de **lista de tarefas** desenvolvido em Python e executado pelo terminal.  
O usuário pode **adicionar**, **visualizar** e **deletar** tarefas de forma prática e intuitiva.

---

## 🚀 Funcionalidades

### ✔️ Adicionar uma nova tarefa
- O programa solicita uma descrição.
- A tarefa é armazenada na lista `tarefa`.
- Uma mensagem confirma a adição.

### 🗑️ Deletar uma tarefa
- Exibe todas as tarefas numeradas.
- O usuário informa o número da tarefa que deseja remover.
- O programa valida e apaga a tarefa correspondente.

### 📋 Mostrar todas as tarefas
- Lista todas as tarefas registradas.
- Exibe cada tarefa com seu índice numérico.

### ❌ Sair
- Encerra a execução do programa.

---

## 🧠 Estrutura do Código

O código é dividido em funções para facilitar a leitura e manutenção:

- `nova_tarefa()`: adiciona tarefas.
- `deletar_tarefa()`: deleta tarefas usando o índice fornecido.
- `mostrar_tarefa()`: lista todas as tarefas.
- O menu principal fica dentro de um loop `while True` e usa condicionais para navegar entre as opções.

As tarefas são armazenadas em uma lista:
```python
tarefa = []
