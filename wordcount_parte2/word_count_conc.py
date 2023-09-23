import os
import sys
from threading import Thread, Semaphore

wc_count = 0
semaphore = Semaphore(1)

def wc(content):
    return len(content.split())

def wc_file(filename):
    try:
        with open(filename, 'r', encoding='latin-1') as f:
            file_content = f.read()
        return wc(file_content)
    except FileNotFoundError:
        return 0

# Função que cada Thread deve executar, e aqui ocorrerá região critica
def wc_subdir(dir_path):
    count = 0
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        count += wc_file(filepath)

    # Região crítica
    semaphore.acquire()
    global wc_count
    wc_count += count
    semaphore.release()

# Função que cria as Threads que executarão a sunção subdir
def wc_dir(dir_path):
    all_threads = []
    
    # Criando uma Thread para cada subdiretório
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        thread = Thread(target=wc_subdir, args=[filepath])
        all_threads.append(thread)
        thread.start()

    # Aguardando as threads terminarem
    for thread in all_threads:
        thread.join()

    # Imprimindo o resultado após todas as Threads terminarem
    global wc_count
    print(wc_count)

# Apenas inciando
def main():
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "root_directory_path")
        return
    root_path = os.path.abspath(sys.argv[1])
    count = wc_dir(root_path)

if __name__ == "__main__":
    main()
