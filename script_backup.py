import os
import shutil

# Inserir local de origem e destino do arquivo de backup
origem = "C:\\Users\\igorv\\OneDrive\\Área de Trabalho\\arquivos"
destino = "D:\\backup"

# Listar arquivos da pasta origem
arquivos_origem = os.listdir(origem)


# Copiar arquivos da pasta origem para Backup
for arquivo in arquivos_origem:
    caminho_origem = os.path.join(origem, arquivo)
    caminho_destino = os.path.join(destino, arquivo)
    shutil.copy2(caminho_origem, caminho_destino)
    # Usamos o copytree quando queremos copiar um diretorio inteiro

print(f'Arquivo salvo em {destino}')
