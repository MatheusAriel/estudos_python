def function(nome: str, idade: int, nacionalidade: str = None) -> None:
    print(f'Nome: {nome} \n'
          f'Idade: {idade} \n'
          f'Nacionalidade: {nacionalidade if nacionalidade else "br"}')


function(idade=28, nome='Matheus')
