class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def listar_produtos(self):
        for i, p in enumerate(self.__produtos, 1):
            print(f'Produto {i}: {p.nome} - R${p.preco}')

    def somar_total(self):
        # print(self.__produtos)
        #total = [x for x['preco'] in self.__produtos]
        #print(total)
        total = 0
        for x in self.__produtos:
            total += x.preco
        return f'Total do carrinho R${total}'
