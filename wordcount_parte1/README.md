# Programacao Concorrente

## No diretório word_count:

### Crie os diretórios e arquivos dataset:
- ./make_dataset.sh

### Compare a execução uma thread com processos para Python.
- time python3 ./python/word_count.py dataset
- time ./run_python.sh dataset

### Compare a execução uma thread com processos para Go.
- time go run ./go/word_count.go dataset
- time ./run_go.sh dataset

### Compare a execução uma thread com processos para Java.
- time java ./java/src/main/java/WordCount.java dataset
- time ./run_java.sh dataset

### Links e avisos
- Escrita e execução do Programa: [Vídeos Asciinema (Drive)](https://drive.google.com/file/d/1KK8SbFm6-tZSRdY-9Js-OQdFni-ofTCZ/view?usp=sharing)
- Observação: Cada computador poderá ter um tempo de execução diferente.
