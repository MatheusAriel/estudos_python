class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for i, p in enumerate(self.produtos, 1):
            #caso sobre nome n tivesse um getter
            #print(f'Produto {i}: {p._Produto__nome} - \tR${p.preco}')
            print(f'Produto {i}: {p.nome} - \tR${p.preco}')

    def somar_total(self):
        total = sum([x.preco for x in self.produtos])
        return total
