import os
import shutil

# Inserir local de origem e destino do arquivo de backup
origem = "C:\\Users\\igorv\\OneDrive\\Área de Trabalho\\arquivos"
destino = "D:\\backup"

# Listar arquivos da pasta origem
arquivos_origem = os.listdir(origem)
arquivos_destino = os.listdir(destino)

# Colocar arquivos em ordem para deletar apenas os dois mais antigos
arquivos_origem.sort()
arquivos_destino.sort()

# Copiar arquivos da pasta origem para Backup
for arquivo in arquivos_origem:
    caminho_origem = os.path.join(origem, arquivo)
    caminho_destino = os.path.join(destino, arquivo)
    shutil.copy2(caminho_origem, caminho_destino)

print(f'Arquivo salvo em {destino}')

# Apagar apenas os dois primeiros arquivos da pasta destino, para que fiquem apenas dois na pasta backup
if len(arquivos_destino) >= 4:
    for arquivo in arquivos_destino[:-2]:

        caminho_arquivo_antigo = os.path.join(destino, arquivo)
        os.remove(caminho_arquivo_antigo)
    print(f'Pasta {destino} atualizada com sucesso!')

# Deletar os dois arquivos mais antigos da pasta origem
if len(arquivos_origem) >= 4:
    for arquivo in arquivos_origem[:-2]:
        caminho_arquivo_antigo = os.path.join(origem, arquivo)
        os.remove(caminho_arquivo_antigo)
    print(f'Pasta {origem} atualizada com sucesso! ')
