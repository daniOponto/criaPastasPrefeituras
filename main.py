import os
import shutil
import streamlit as st
import base64
from zipfile import ZipFile
from io import BytesIO

def main():
    # Configurando o tema da página
    st.set_page_config(
        page_title="Criar Pastas - Prefeituras",
        layout="centered",
        initial_sidebar_state="auto",
    )

    # Definindo o estilo do tema
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #f0f0f0;
        }
        .sidebar .sidebar-content {
            background: #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título principal
    st.title("Organizador de Arquivos por Cidade")

    # Componente de upload de arquivos
    uploaded_files = st.file_uploader("Insira os arquivos de prefeituras que deseja organizar em pastas:", accept_multiple_files=True)

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
            'arco-iris': 'Prefeitura Arco-Iris',
            'ariranha': 'Prefeitura Ariranha',
            'bastos': 'Prefeitura Bastos',
            'bilac': 'Prefeitura Bilac',
            'bora': 'Prefeitura Bora',
            'dracena': 'Prefeitura Dracena',
            'flora rica': 'Prefeitura Flora Rica',
            'florida paulista': 'Prefeitura Florida Paulista',
            'getulina': 'Prefeitura Getulina',
            'guaracai': 'Prefeitura Guaracai',
            'guararapes': 'Prefeitura Guararapes',
            'herculandia': 'Prefeitura Herculandia',
            'iacri': 'Prefeitura Iacri',
            'inubia paulista': 'Prefeitura Inubia Paulista',
            'junqueiropolis': 'Prefeitura Junqueiropolis',
            'lucelia': 'Prefeitura Lucelia',
            'luiziania': 'Prefeitura Luiziania',
            'mariapolis': 'Prefeitura Mariapolis',
            'mirandopolis': 'Prefeitura Mirandopolis',
            'osvaldo cruz': 'Prefeitura Osvaldo Cruz',
            'ouro verde': 'Prefeitura Ouro Verde',
            'pacaembu': 'Prefeitura Pacaembu',
            'palmares paulista': 'Prefeitura Palmares Paulista',
            'panorama': 'Prefeitura Panorama',
            'parapua': 'Prefeitura Parapua',
            'pauliceia': 'Prefeitura Pauliceia',
            'pereira barreto': 'Prefeitura Pereira Barreto',
            'piacatu': 'Prefeitura Piacatu',
            'pirangi': 'Prefeitura Pirangi',
            'presidente prudente': 'Prefeitura Presidente Prudente',
            'quintana': 'Prefeitura Quintana',
            'rinopolis': 'Prefeitura Rinopolis',
            'rubiacea': 'Prefeitura Rubiacea',
            'santa mercedes': 'Prefeitura Santa Mercedes',
            'santopolis do aguapei': 'Prefeitura Santopolis Do Aguapei',
            'tupa': 'Prefeitura Tupa',
            'tupi paulista': 'Prefeitura Tupi Paulista',
            'valparaiso': 'Prefeitura Valparaiso'
        }

        # Organizando os arquivos por cidade
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in file_name.lower()), None)

            if cidade_encontrada:
                diretorio_destino_cidade = os.path.join("./arquivos_organizados", cidades_destinos[cidade_encontrada])
                os.makedirs(diretorio_destino_cidade, exist_ok=True)  # Garante que o diretório seja criado se não existir
                caminho_destino = os.path.join(diretorio_destino_cidade, file_name)
                shutil.move(file_path, caminho_destino)

        st.success("Arquivos organizados com sucesso.")

        # Criando o arquivo zip
        zipf = BytesIO()
        with ZipFile(zipf, 'w') as zip_obj:
            for cidade, pasta in cidades_destinos.items():
                cidade_path = os.path.join("./arquivos_organizados", pasta)
                for root, _, files in os.walk(cidade_path):
                    for file in files:
                        zip_obj.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "./arquivos_organizados"))

        zipf.seek(0)
        b64 = base64.b64encode(zipf.read()).decode()
        href = f'<a href="data:application/zip;base64,{b64}" download="arquivos_organizados.zip"><button style="background-color:#008CBA;border:none;color:white;padding:15px 32px;text-align:center;display:inline-block;font-size:16px;margin-bottom:0;cursor:pointer;border-radius:4px;">Baixar Arquivos Organizados</button></a>'
        st.markdown(href, unsafe_allow_html=True)

        # Botão para limpar diretórios
        if st.button("Limpar Diretórios"):
            shutil.rmtree(temp_dir, ignore_errors=True)
            shutil.rmtree("./arquivos_organizados", ignore_errors=True)
            st.success("Diretórios limpos com sucesso.")

if __name__ == "__main__":
    main()
