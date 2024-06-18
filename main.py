import streamlit as st
import os
import shutil
from pathlib import Path

# Função para mover arquivos baseado na cidade
def move_arquivos_por_cidade(arquivos_carregados, diretorio_base_destino, cidades_destinos):
    for arquivo in arquivos_carregados:
        nome_arquivo = arquivo.name
        cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in nome_arquivo.lower()), None)

        if cidade_encontrada:
            diretorio_destino_cidade = os.path.join(diretorio_base_destino, cidades_destinos[cidade_encontrada])
            os.makedirs(diretorio_destino_cidade, exist_ok=True)
            caminho_destino = os.path.join(diretorio_destino_cidade, nome_arquivo)
            with open(caminho_destino, "wb") as f:
                f.write(arquivo.getbuffer())

            st.write(f"Arquivo '{nome_arquivo}' movido para '{cidades_destinos[cidade_encontrada]}'.")

# Interface do Streamlit
st.title("File Mover by City")

# Diretório base para onde os arquivos vão
diretorio_base_destino = './uploads'  # Substitua pelo seu diretório de destino

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
    move_arquivos_por_cidade(uploaded_files, diretorio_base_destino, cidades_destinos)
