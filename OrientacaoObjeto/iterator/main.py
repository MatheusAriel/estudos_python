class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def __getitem__(self, index):
        try:
            result = self.__items[index]
        except IndexError:
            raise StopIteration('Index não existente na lista')
        else:
            return result

    def __setitem__(self, key, value):
        if key >= len(self.__items):
            self.__items.append(value)
        else:
            self.__items[key] = value

    def add(self, value):
        self.__items.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration
        else:
            return item

    def __str__(self):
        return f'{self.__class__.__name__} ({self.__items})'

    def __delitem__(self, key):
        try:
            del self.__items[self.__index]
        except IndexError:
            raise StopIteration('Não foi possível apagar pois o Index não existente na lista')


if __name__ == '__main__':
    l1 = MinhaLista()
    l1.add('Arroz')
    l1.add('Feijão')
    l1.add('Farofa')

    print(type(l1))
    print(l1, end='\n\n')

    for value in l1:
        print(value)

    for value in l1:
        print(value)

    print('\n\n')
    print(l1[1])

    l1[11] = 'Maçã'

    print(l1)

    del l1[11]
    print(l1)

