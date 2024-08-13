Descompressão de Arquivos em Container  
Este projeto é um script Python que descomprime arquivos armazenados em um container binário.  
O script lê um arquivo de container, descomprime os dados usando zlib e salva cada arquivo descomprimido em um diretório de saída especificado.  

Funcionalidade  
Lê um arquivo de container no formato binário.  
Ignora 4 bytes no início de cada seção de arquivo (esses 4 bytes representam o tamanho dos dados descomprimidos).  
Lê o tamanho dos dados comprimidos (4 bytes).  
Descomprime os dados usando zlib.  
Salva cada arquivo descomprimido em um diretório especificado.  
Manipula erros de descompressão e exibe informações úteis para depuração.  
Requisitos  
Python 3.x  
Biblioteca zlib (incluída no Python padrão)  
Uso  
Certifique-se de ter o Python 3.x instalado em seu sistema.  

Clone este repositório ou baixe o script DESCOMPACTAR_PARTES.py.  

Atualize as variáveis caminho_do_container e diretorio_de_saida no script com o    
caminho para o seu arquivo de container e o diretório onde os arquivos descomprimidos serão salvos, respectivamente.  

Execute o script usando o comando:  

bash  
Copiar código  
python DESCOMPACTAR_PARTES.py  
