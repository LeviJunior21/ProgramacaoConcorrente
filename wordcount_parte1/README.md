# Programação Concorrente - Processos

A estratégia é criar processos igual a quantidade de diretórios, os processos criam arquivos que escrevem a quantidade de palavras encontradas num diretório.
Apesar de serem concorrentes, como cada um escreve um arquivo diferente, não há problemas de perda dos dados em região crítica.

A garantia que todas as palavras serão contadas é quando fazemos um wait para esperar todos os processos terminarem e em seguida contamos as palavras para cada arquivo criado pelos processos.


## No diretório wordcount_parte1:

### Crie os sub-diretórios e arquivos para o diretorio dataset:
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

Em sequência, onde Go e Java usam códigos similares aos do Python mas com algumas modificações no arquivo.
1 - Python: https://asciinema.org/a/kh6eKo7fZ4BCNRplc1AHQ7hdh
2 - Go: https://asciinema.org/a/dXCLnx5sFu5iA6j5S5P29Q8NP
3 - Java: https://asciinema.org/a/lY85JZ288T6TnrDU3nzvJezYl
