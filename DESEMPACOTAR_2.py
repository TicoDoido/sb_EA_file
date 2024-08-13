import zlib
import os

def descomprimir_arquivos_em_container(container_path, output_file, first_part_file):
    with open(container_path, 'rb') as f:
        # Abrir o arquivo de saída para a maior parte dos dados
        with open(output_file, 'wb') as arquivo_saida:
            dados_acumulados = bytearray()  # Usar um buffer para acumular os dados descomprimidos
            primeira_parte_salva = False

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

                    # Se for a primeira parte, salvar em um arquivo separado
                    if not primeira_parte_salva:
                        with open(first_part_file, 'wb') as arquivo_primeira_parte:
                            arquivo_primeira_parte.write(dados_descomprimidos)
                        print(f'Primeira parte descomprimida de {tamanho} bytes salva em {first_part_file}.')
                        primeira_parte_salva = True
                    else:
                        # Caso contrário, acumular os dados descomprimidos no buffer
                        dados_acumulados.extend(dados_descomprimidos)
                        print(f'Dados descomprimidos de {tamanho} bytes acumulados.')

                except zlib.error as e:
                    # Se ocorrer um erro, imprimir a posição e os dados em hex
                    print(f"Erro ao descomprimir na posição {posicao_atual}: {e}")
                    break

            # Após o loop, salvar todos os dados acumulados em um único arquivo
            if dados_acumulados:
                arquivo_saida.write(dados_acumulados)
                print(f'Dados descomprimidos restantes salvos em {output_file}.')

# Caminho para o arquivo do container
caminho_do_container = 'en.sb'

# Nome do arquivo para a primeira parte
arquivo_primeira_parte = 'en/primeira_parte_descomprimida.chunk'

# Nome do arquivo de saída para os dados restantes
arquivo_de_saida = 'en/arquivo_descomprimido_total.chunk'

descomprimir_arquivos_em_container(caminho_do_container, arquivo_de_saida, arquivo_primeira_parte)
