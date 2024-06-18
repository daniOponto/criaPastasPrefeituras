import streamlit as st
import os
import shutil
from pathlib import Path
import tempfile
import zipfile

# Função para mover arquivos baseado na cidade
def move_arquivos_por_cidade(arquivos_carregados, cidades_destinos):
    temp_dir = tempfile.TemporaryDirectory()

    for arquivo in arquivos_carregados:
        nome_arquivo = arquivo.name
        cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in nome_arquivo.lower()), None)

        if cidade_encontrada:
            diretorio_destino_cidade = os.path.join(temp_dir.name, cidades_destinos[cidade_encontrada])
            os.makedirs(diretorio_destino_cidade, exist_ok=True)
            caminho_destino = os.path.join(diretorio_destino_cidade, nome_arquivo)
            with open(caminho_destino, "wb") as f:
                f.write(arquivo.getbuffer())

            st.write(f"Arquivo '{nome_arquivo}' movido para '{cidades_destinos[cidade_encontrada]}'.")

    return temp_dir

# Função para criar um arquivo ZIP temporário
def criar_arquivo_zip(temp_dir):
    zip_filename = 'arquivos_por_cidade.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(temp_dir.name):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_dir.name))

    return zip_filename

# Interface do Streamlit
st.title("File Mover by City")

# Lista de cidades e nomes das pastas
cidades_destinos = {
    'adamantina': 'Prefeitura Adamantina',
    'alfredo marcondes': 'Prefeitura Alfredo Marcondes',
    # Lista completa de cidades
}

# Upload dos arquivos
uploaded_files = st.file_uploader("Escolha os arquivos", type=["txt", "csv", "xlsx", "pdf"], accept_multiple_files=True)

# Verifica se arquivos foram carregados
if uploaded_files:
    # Executa a função para mover os arquivos por cidade
    temp_dir = move_arquivos_por_cidade(uploaded_files, cidades_destinos)

    # Cria um arquivo ZIP temporário
    zip_filename = criar_arquivo_zip(temp_dir)

    # Download do arquivo ZIP
    st.markdown(f"### Download dos arquivos por cidade")
    st.markdown(f"Download [**{zip_filename}**](./{zip_filename}) pronto!")
