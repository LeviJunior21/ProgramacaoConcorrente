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

def wc_subdir(dir_path):
    count = 0
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        count += wc_file(filepath)

    semaphore.acquire()
    global wc_count
    wc_count += count
    semaphore.release()

def wc_dir(dir_path):
    all_threads = []
    
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        thread = Thread(target=wc_subdir, args=[filepath])
        all_threads.append(thread)
        thread.start()

    for thread in all_threads:
        thread.join()

    global wc_count
    print(wc_count)

def main():
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "root_directory_path")
        return
    root_path = os.path.abspath(sys.argv[1])
    count = wc_dir(root_path)

if __name__ == "__main__":
    main()
