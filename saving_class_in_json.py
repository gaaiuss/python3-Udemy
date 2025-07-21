# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
import os

ARCHIVE_PATH = 'data\\people.json'


def save_data(*args):
    with open(ARCHIVE_PATH, 'w', encoding='utf8') as archive:
        json.dump(args, archive, indent=2, ensure_ascii=False)


class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age


people1 = People('Caio Guilherme', 25)
people2 = People('Paulo Guina', 50)
people3 = People('Marina', 22)
people4 = People('Jill', 18)

if __name__ == '__main__':
    save_data(vars(people1), vars(people2), vars(people3), vars(people4))
