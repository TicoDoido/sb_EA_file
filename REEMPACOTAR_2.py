import zlib

def create_container(file1_path, file2_path, output_container):
    def write_compressed_part(part, container):
        # Comprimindo a parte usando zlib (melhor compressão)
        compressed_part = zlib.compress(part, zlib.Z_BEST_COMPRESSION)

        # Tamanho da parte descomprimida em big-endian
        part_size = len(part).to_bytes(4, byteorder='big')

        # Tamanho da parte comprimida em big-endian
        compressed_size = len(compressed_part).to_bytes(4, byteorder='big')

        # Escrevendo no container
        container.write(part_size)  # Tamanho da parte descomprimida
        container.write(compressed_size)  # Tamanho da parte comprimida
        container.write(compressed_part)

    with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2, open(output_container, 'wb') as container:
        # Processando o primeiro arquivo
        while True:
            part = f1.read(64 * 1024)  # Lê 64 KB
            if not part:
                break
            write_compressed_part(part, container)

        # Processando o segundo arquivo
        while True:
            part = f2.read(64 * 1024)  # Lê 64 KB
            if not part:
                break
            write_compressed_part(part, container)

# Exemplo de uso
create_container('en/primeira_parte_descomprimida.chunk', 'en/arquivo_descomprimido_total.chunk', 'en/en.sb')
