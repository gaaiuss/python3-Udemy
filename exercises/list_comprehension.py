# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from data import products
from copy import deepcopy

new_products = [{**p, 'price': round(p['price'] * 1.1, 2)} for p in products]


print(*products, sep='\n')
print()
# print(*new_products, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# name_ordered_products = sorted(
#     deepcopy(products), key=lambda p: p['name'], reverse=True)
# print(*name_ordered_products, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

price_ordered_products = sorted(
    deepcopy(products), key=lambda p: p['price'])
print(*price_ordered_products, sep='\n')
