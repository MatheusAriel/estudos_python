carrinho = []
carrinho.append(('Produto 1', 30.90))
carrinho.append(('Produto 2', 16.50))
carrinho.append(('Produto 3', 19.00))
carrinho.append(('Produto 5', 580.00))

print(carrinho)

print()
print('Minha resolução:')
total = [y for x, y in carrinho]
print(sum(total))

print()
print('Resolução Curso:')
produto, preco = carrinho[0]
print(produto, preco)

print()
total2 = sum([float(y) for x, y in carrinho])
print(total2)


