# https://ffmpeg.zeranoe.com/builds/
"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v LIBX264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:v0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

import os, fnmatch, sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
codec_audio = '-c:a aac'
crf = '-crf 23'
preset = '-preset ultrafast'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

caminho_origem = r'C:\Users\mathe\Downloads\videos'
caminho_destino = r'C:\Users\mathe\Downloads\videos_convertidos'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
