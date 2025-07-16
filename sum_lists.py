"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [10, 2, 3, 4]

list_sum = [x + y for x, y in zip(list_a, list_b)]
print(list_sum)

# list_sum = []
# for i in range(len(list_b)):
#     list_sum.append(list_a[i] + list_b[i])
# print(list_sum)

# list_sum = []
# for i, _ in enumerate(list_b):
#     list_sum.append(list_a[i] + list_b[i])
# print(list_sum)

# def zipper(list1, list2):
#     interval = min(len(list1), len(list2))
#     return [(list1[i] + list2[i]) for i in range(interval)]
# print(zipper(list_a, list_b))
