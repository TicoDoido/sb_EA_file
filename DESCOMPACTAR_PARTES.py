import zlib
import os

def descomprimir_arquivos_em_container(container_path, output_dir):
    with open(container_path, 'rb') as f:
        contador = 1
        while True:
            # Pular 4 bytes (se necessário entre cada arquivo)
            f.seek(4, os.SEEK_CUR)
            
            # Ler os próximos 4 bytes para obter o tamanho do arquivo comprimido
            tamanho_bytes = f.read(4)
            if not tamanho_bytes:
                break  # Se não há mais bytes, sair do loop

            # Converter os 4 bytes para um inteiro em big-endian
            tamanho = int.from_bytes(tamanho_bytes, byteorder='big')

            # Ler os dados comprimidos com base no tamanho
            dados_comprimidos = f.read(tamanho)
            posicao_atual = f.tell() - tamanho  # Calcula a posição inicial dos dados comprimidos

            try:
                # Tentar descomprimir os dados
                dados_descomprimidos = zlib.decompress(dados_comprimidos)

                # Gerar um nome de arquivo único para cada arquivo descomprimido
                nome_arquivo = f'{output_dir}/arquivo_descomprimido_{contador}.bin'
                
                # Salvar os dados descomprimidos em um novo arquivo
                with open(nome_arquivo, 'wb') as arquivo_saida:
                    arquivo_saida.write(dados_descomprimidos)

                print(f'Arquivo {nome_arquivo} salvo com sucesso.')

                # Incrementar o contador para o próximo arquivo
                contador += 1

            except zlib.error as e:
                # Se ocorrer um erro, imprimir a posição e os dados em hex
                print(f"Erro ao descomprimir na posição {posicao_atual}: {e}")
                print(f"Dados em hex: {dados_comprimidos.hex()}")
                break

# Caminho para o arquivo do container
caminho_do_container = 'en.sb'

# Diretório onde os arquivos descomprimidos serão salvos
diretorio_de_saida = 'en/'

descomprimir_arquivos_em_container(caminho_do_container, diretorio_de_saida)
