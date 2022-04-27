from carrinhodecompras import CarrinhoDeCompras
from produto import Produto

carrinho = CarrinhoDeCompras()

produto = Produto('TV', 2500.00)
produto2 = Produto('PC', 7500.00)
produto3 = Produto('Celular', 4500.00)

carrinho.listar_produtos()
carrinho.inserir_produto(produto)
carrinho.inserir_produto(produto3)
carrinho.inserir_produto(produto2)

carrinho.listar_produtos()
print()
print(f'Total Carrinho de compras: R$ {carrinho.somar_total()}')
