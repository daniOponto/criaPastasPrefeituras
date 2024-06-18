import os
import shutil

# Diretório onde os arquivos estão
diretorio_origem = ('C:/Users/Microsoft/Downloads/Pasta1')

# Diretório para onde os arquivos vão
diretorio_base_destino = ('C:/Users/Microsoft/Downloads/Pasta1')

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


arquivos = os.listdir(diretorio_origem)
for arquivo in arquivos:
    cidade_encontrada = next((cidade for cidade in cidades_destinos if cidade in arquivo.lower()), None)

    if cidade_encontrada:
        caminho_origem = os.path.join(diretorio_origem, arquivo)
        diretorio_destino_cidade = os.path.join(diretorio_base_destino, cidades_destinos[cidade_encontrada])
        os.makedirs(diretorio_destino_cidade, exist_ok=True)
        caminho_destino = os.path.join(diretorio_destino_cidade, arquivo)
        shutil.move(caminho_origem, caminho_destino)

print("Processo concluído.")
