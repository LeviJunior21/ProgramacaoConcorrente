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
- Escrita e execuçã do Programa em Asciinema: [Vídeos Asciinema (Drive)]([https://drive.google.com/file/d/1KK8SbFm6-tZSRdY-9Js-OQdFni-ofTCZ/view?usp=sharing](https://drive.google.com/drive/folders/1dyUa0IJ2kdiHjiO8QybB4rMJU94HgBTP?usp=sharing))
