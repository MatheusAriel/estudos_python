from glob import iglob

# Nos retorna todos os arquivos do diretório raiz
files = iglob('/users/Downloads/*', recursive=True)
for file in iglob:
    print(file)

# Nos retorna todos os arquivos do diretório raiz e de seus sub-diretórios
files = iglob('/root/Downloads/**', recursive=True)

# Nos retorna os sub-diretórios do diretório raiz
files = iglob('/root/Downloads/*/', recursive=True)

# Nos retorna o diretório raiz e seus sub-diretórios
files = iglob('/root/Downloads/**/', recursive=True)

# Nos retorna todos os arquivos do diretório raiz que contenham a extensão "mp3"
files = iglob('/root/Downloads/*.mp3', recursive=True)

# Nos retorna todos os arquivos dos sub-diretórios que contenham a extensão "mp3"
files = iglob('/root/Downloads/*/*.mp3', recursive=True)
