import os
from PyPDF2 import PdfMerger

def consolidar_pdfs(arquivo_saida):
    # Criar um objeto PdfMerger
    merger = PdfMerger()

    # Obter o diretório atual (onde o script está localizado)
    diretorio_atual = os.getcwd()

    # Obter todos os arquivos PDF no diretório atual
    arquivos_pdfs = [f for f in os.listdir(diretorio_atual) if f.endswith('.pdf')]

    # Ordenar os arquivos para garantir que eles sejam mesclados na ordem correta
    arquivos_pdfs.sort()

    # Adicionar cada arquivo PDF ao merger
    for pdf in arquivos_pdfs:
        caminho_pdf = os.path.join(diretorio_atual, pdf)
        with open(caminho_pdf, 'rb') as f:
            merger.append(f)

    # Escrever o arquivo consolidado
    with open(arquivo_saida, 'wb') as f_saida:
        merger.write(f_saida)

    # Fechar o objeto merger
    merger.close()

    print(f'Arquivo PDF consolidado criado: {arquivo_saida}')

# Exemplo de uso:
arquivo_saida = 'arquivo_consolidado.pdf'  # Nome do arquivo consolidado
consolidar_pdfs(arquivo_saida)
