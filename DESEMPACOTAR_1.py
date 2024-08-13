import zlib
import os

def descomprimir_arquivos_em_container(container_path, output_file, last_part_file):
    with open(container_path, 'rb') as f:
        # Abrir o arquivo de saída para a maior parte dos dados
        with open(output_file, 'wb') as arquivo_saida:
            contador = 0
            while True:
                
                # Pular 4 bytes (se necessário entre cada arquivo), É SÓ O TAMANHO DO ARQUIVO DESCOMPRIMIDO
                f.seek(4, os.SEEK_CUR)
                
                # Ler os próximos 4 bytes para obter o tamanho da parte descomprimida
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

                    # Incrementar o contador para verificar se é a última parte
                    contador += 1

                    # Se for a última parte, salvar em um arquivo separado
                    if not f.peek(4):  # Verifica se há mais dados para ler
                        with open(last_part_file, 'wb') as arquivo_ultimo:
                            arquivo_ultimo.write(dados_descomprimidos)
                        print(f'Última parte descomprimida de {tamanho} bytes salva em {last_part_file}.')
                    else:
                        # Caso contrário, escrever os dados descomprimidos no arquivo principal
                        arquivo_saida.write(dados_descomprimidos)
                        print(f'Dados descomprimidos de {tamanho} bytes adicionados ao arquivo de saída.')

                except zlib.error as e:
                    # Se ocorrer um erro, imprimir a posição e os dados em hex
                    print(f"Erro ao descomprimir na posição {posicao_atual}: {e}")
                    break

# Caminho para o arquivo do container
caminho_do_container = 'en.sb'

# Nome do arquivo de saída para a maior parte dos dados
arquivo_de_saida = 'en/arquivo_descomprimido_total.chunk'

# Nome do arquivo para a última parte
arquivo_ultimo = 'en/ultima_parte_descomprimida.chunk'

descomprimir_arquivos_em_container(caminho_do_container, arquivo_de_saida, arquivo_ultimo)
