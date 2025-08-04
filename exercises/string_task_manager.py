# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
from os import system
import json


def validate_index(list):
    try:
        return list.pop()
    except IndexError:
        print('No values to pop\n')

def save_archive(list, archive_path):
    with open(archive_path, 'w', encoding='utf8') as archive:
        json.dump(list, archive, indent=2)

def read_archive(list, archive_path):
    try:
        with open(archive_path, 'r', encoding='utf8') as archive:
            return json.load(archive)
    except FileNotFoundError:
        print('Task list not found\nCreating task list json...\n')
        save_archive(list, archive_path)
        return []


archive_path = 'data\\task_list.json'
answer = ''
todo = read_archive([], archive_path)
redo = []


while answer != '5':
    answer = input(
        'Type a task or choose one action:\n1- list\n2 - undo\n3 - redo\n4 - clear terminal\n5 - exit\n\n')
    print()

    if answer not in ('1', '2', '3', '4', '5'):
        todo.append(answer)
    elif answer == '1':
        print(todo, '\n')
    elif answer == '2':
        redo.append(validate_index(todo))
        print(todo, '\n')
    elif answer == '3':
        todo.append(validate_index(redo))
        print(todo, '\n')
    elif answer == '4':
        system('cls')

    save_archive(todo, archive_path)
