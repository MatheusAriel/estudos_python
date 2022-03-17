set1 = {1, 2, 3, 4, 5, 'Matheus'}
print(set1, type(set1))

for v in set1:
    print(v)

print('\n\n')
set2 = set()
set2.add(1)
set2.add('Matheus')
set2.add((1, 2, 3, 4, 5, 6, 7))
print(set2)

set2.discard('Matheus')
print(set2)

set2.update('Ariel', [1, 2, 3], {1, 2, 3, 8})
print(set2)

print('\n\n')
l1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 'Matheus', 'Matheus']
print(l1, type(l1))
l1 = set(l1)
print(l1, type(l1))
l1 = list(l1)
print(l1, type(l1))

print('\n\n')
s1 = {1, 2, 3, 4, 5, 10}
s2 = {1, 2, 3, 4, 5, 6, 7, 8}
s3 = s1 | s2  # ou s1.union(s2)
print(s3)

s4 = s1 & s2
print(s4)

s5 = s1 - s2
print(s5)
s5 = s2 - s1
print(s5)

s6 = s1 ^ s2
print(s6)

l1 = ['Luiz', 'Maria', 'Mario', 'Luigi', 'Luigi', 'Mario', 'Mario', 'Carlos']
l2 = ['Luiz', 'Luiz', 'Luiz', 'Luiz', 'Maria', 'Mario', 'Carlos', 'Luigi', 'Luigi']

if set(l1) == set(l2):
    print('São iguais')
else:
    print('São diferentes')

l1 = list(set(l1))
l2 = list(set(l2))

print(l1 != l2)
