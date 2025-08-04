# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
from saving_class_in_json import ARCHIVE_PATH, People
import json

people_list = []

with open(ARCHIVE_PATH, 'r', encoding='utf8') as archive:
    people_data = json.load(archive)

for people in people_data:
    people_list.append(people)

print(people_list)