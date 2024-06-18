import os
import shutil
import streamlit as st
import base64  # Import base64 module for encoding

# Function to process uploaded files
def process_files(uploaded_files):
    # Temporary directory for storing uploaded files
    temp_dir = './temp_upload'
    os.makedirs(temp_dir, exist_ok=True)

    # Save uploaded files to temp directory
    for uploaded_file in uploaded_files:
        with open(os.path.join(temp_dir, uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())

    # Process uploaded files
    process_documents(temp_dir)

    # Create zip file of processed folders
    zip_filename = create_zip_of_folders()

    # Provide download link for zip file
    st.markdown(f"### Download Processed Files")
    st.markdown(get_binary_file_downloader_html(zip_filename, 'ProcessedFiles.zip', 'Click here to download'))

    # Cleanup temp directory
    shutil.rmtree(temp_dir)

# Function to process documents based on city
def process_documents(temp_dir):
    cidades_destinos = {  # Your dictionary of cities and folder names
        'adamantina': 'Prefeitura Adamantina',
        # Add other cities as needed
    }

    arquivos = os.listdir(temp_dir)
    for arquivo in arquivos:
        cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in arquivo.lower()), None)
        if cidade_encontrada:
            diretorio_destino_cidade = os.path.join(temp_dir, cidades_destinos[cidade_encontrada])
            os.makedirs(diretorio_destino_cidade, exist_ok=True)
            caminho_origem = os.path.join(temp_dir, arquivo)
            caminho_destino = os.path.join(diretorio_destino_cidade, arquivo)
            shutil.move(caminho_origem, caminho_destino)

# Function to create a zip file of processed folders
def create_zip_of_folders():
    processed_zip = 'ProcessedFiles.zip'
    shutil.make_archive(processed_zip.replace('.zip', ''), 'zip', './temp_upload')
    return processed_zip

# Function to download files
def get_binary_file_downloader_html(bin_file, file_label, button_label):
    with open(bin_file, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}">{button_label}</a>'

# Streamlit UI
st.title('Document Upload and Processing')

uploaded_files = st.file_uploader('Upload your documents', accept_multiple_files=True)
if st.button('Process Files') and uploaded_files:
    process_files(uploaded_files)
