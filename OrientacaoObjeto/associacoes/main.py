from escritor import Escritor
from caneta import Caneta
from maquinadeescrever import MaquinaDeEscrever

escritor1 = Escritor('joão gabriel')
caneta1 = Caneta('Bic', 'Azul')
maquina1 = MaquinaDeEscrever()

print()

print(escritor1.nome)
print(caneta1.marca)
print(maquina1.escrever())

print()
escritor1.ferramenta = caneta1
escritor1.ferramenta.escrever()

print()
del escritor1
print(caneta1.marca)