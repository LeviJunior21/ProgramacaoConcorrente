# Programação Concorrente - Threads

A estratégia é criar Threads iguais a quantidade de diretórios. Cada Thread ganha um sub-diretório para contar as palavras de todos os arquivos dentro do sub-diretório.

Após cada Thread contar as palavras do seu diretório, elas incrementam numa variável que é compartilhada globalmente, que por sua vez é uma região crítica e precisamos garantir exclusão mútua.

## No diretório wordcount_parte2:

### Dê permissão para os arquivos shell e crie os sub-diretórios e arquivos para o diretorio dataset:
- chmod +x ./make_dataset.sh
- chmod +x ./run_python.sh
- chmod +x ./run_java.sh
- ./make_dataset.sh

### Compare a execução de uma thread com várias Threads para Python.
- time python3 ./python/word_count.py dataset
- time ./run_python.sh dataset

### Compare a execução de uma thread com várias Threads para Java.
- time java ./java/WordCount.java dataset
- time ./run_java.sh dataset

### Links
- Escrita e execução do Programa em Asciinema: [Vídeos Asciinema](https://drive.google.com/drive/folders/1tq0v_ZYFCRJ50Z_ln7CiDel4hzc9vXA1?usp=sharing)
