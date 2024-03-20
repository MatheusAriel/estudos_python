from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

# Lista de URLs para solicitar
urls = ["URL"] * 1000000000

# Use ThreadPoolExecutor para enviar solicitações em paralelo
with ThreadPoolExecutor(max_workers=1000) as executor:
    responses = list(executor.map(urlopen, urls))

# Impressão de confirmação
print("Solicitações concluídas:", len(responses))
