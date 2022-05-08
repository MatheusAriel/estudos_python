"""
Documentação:
https://pythonhosted.org/PyPDF2/

Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
"""
import PyPDF2
import os

"""COMO JUNTAR PDF"""
"""
caminho_dos_pdfs = 'pdfs'
novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_pdf.pdf', 'wb') as file:
    novo_pdf.write(file)
"""

"""COMO SEPARAR PDF"""

with open('pdfs/novo_pdf.pdf', 'rb') as pdf:
    reader = PyPDF2.PdfFileReader(pdf)
    num_pages = reader.getNumPages()
    for num_page in range(num_pages):
        writer = PyPDF2.PdfFileWriter()
        atual_page = reader.getPage(num_page)
        writer.addPage(atual_page)

        with open(f'novos_pdfs/{num_page}.pdf', 'wb') as new_pdf:
            writer.write(new_pdf)