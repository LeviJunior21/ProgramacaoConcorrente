import os
import sys
from threading import Thread, Semaphore

wc_count = []

def wc(content):
    return len(content.split())

def wc_file(filename):
    try:
        with open(filename, 'r', encoding='latin-1') as f:
            file_content = f.read()
        return wc(file_content)
    except FileNotFoundError:
        return 0

def wc_subdir(dir_path, index):
    count = 0
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        count += wc_file(filepath)

    global wc_count
    wc_count[index] = count

def wc_dir(dir_path):
    global wc_count

    all_threads = []
    list_dir = os.listdir(dir_path)
    wc_count = [0] * len(list_dir)

    for i in range(len(list_dir)):
        filepath = os.path.join(dir_path, list_dir[i])
        thread = Thread(target=wc_subdir, args=[filepath, i])
        all_threads.append(thread)
        thread.start()

    for thread in all_threads:
        thread.join()

    print(sum(wc_count))

def main():
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "root_directory_path")
        return
    root_path = os.path.abspath(sys.argv[1])
    wc_dir(root_path)

if __name__ == "__main__":
    main()
