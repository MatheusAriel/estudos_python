"""
    animal ->respirar
        lobo (animal) ->respirar/ ruivar
            cachorro (lobo) -> respirar/ uivar/ latir
"""


class Biblioteca:
    def chama_meotodo_da_interface(self):
        self.metodo_da_interface()


class Interface(Biblioteca):
    def metodo_da_interface(self):
        print('Sou um meotodo da classe interface')
