from cep import Cep
import traceback

try:
    c1 = Cep('12352100')
    print(c1.buscar_cep())

except (ValueError, TypeError, Exception) as erro:
    print(f'Erro: {erro}')
    traceback.print_exc()
