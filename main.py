import os
import shutil
import streamlit as st
from zipfile import ZipFile
from io import BytesIO

def main():
    st.title("Organizador de Arquivos por Cidade")

    # Componente de upload de arquivos
    uploaded_files = st.file_uploader("Selecione os arquivos que deseja organizar por cidade:", accept_multiple_files=True)

    if uploaded_files:
        # Criando um diretório temporário para armazenar os arquivos
        temp_dir = "./temp_upload"
        os.makedirs(temp_dir, exist_ok=True)

        # Salvando os arquivos no diretório temporário
        file_paths = []
        for file in uploaded_files:
            file_path = os.path.join(temp_dir, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            file_paths.append(file_path)

        # Lista de cidades e nomes das pastas
        cidades_destinos = {
            'adamantina': 'Prefeitura Adamantina',
            'alfredo marcondes': 'Prefeitura Alfredo Marcondes',
            # Lista completa de cidades aqui ...
            'valparaiso': 'Prefeitura Valparaiso'
        }

        # Organizando os arquivos por cidade
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in file_name.lower()), None)

            if cidade_encontrada:
                diretorio_destino_cidade = os.path.join("./arquivos_organizados", cidades_destinos[cidade_encontrada])
                os.makedirs(diretorio_destino_cidade, exist_ok=True)
                caminho_destino = os.path.join(diretorio_destino_cidade, file_name)
                shutil.move(file_path, caminho_destino)

        st.success("Arquivos organizados com sucesso.")

        # Opção para fazer download dos arquivos organizados
        if st.button("Baixar Arquivos Organizados"):
            zipf = BytesIO()
            with ZipFile(zipf, 'w') as zip_obj:
                for cidade in cidades_destinos.values():
                    cidade_path = os.path.join("./arquivos_organizados", cidade)
                    for root, _, files in os.walk(cidade_path):
                        for file in files:
                            zip_obj.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), cidade_path))

            zipf.seek(0)
            st.markdown(get_download_link(zipf), unsafe_allow_html=True)

        # Removendo diretório temporário após o processamento
        shutil.rmtree(temp_dir, ignore_errors=True)

def get_download_link(file):
    # Cria um link para download do arquivo zipado
    href = f'<a href="data:application/zip;base64,{file.read().encode("base64").decode()}">Clique aqui para baixar os arquivos organizados</a>'
    return href

if __name__ == "__main__":
    main()
