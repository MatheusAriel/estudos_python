from itertools import zip_longest

list_a = list(range(1, 15))
list_b = list(range(1, 10))
print(list_a, '+', list_b)

print()
list_sum = [x + y for x, y in zip(list_a, list_b)]
print(f'Minha resolução somando até {int(list_sum[-1]- list_sum[-1]/2)}: {list_sum}')
print()


list_sum_total = [x+y for  x, y in zip_longest(list_a,list_b, fillvalue=0)]
print(f'Somando todos os valores das duas listas: {list_sum_total}')