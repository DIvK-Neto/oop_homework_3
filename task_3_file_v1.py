from pprint import pprint
import os

# Функция создаёт новый файл на основе исходных
def file_generator():
    
    initial_path = 'initial'
    path_result = 'result'
    sorted_files = {}
    
    for file in os.scandir(initial_path):  # сканируем папку с файлами
        if file.is_file():
            with open(f"{initial_path}/{file.name}", encoding='utf-8') as f:
                data = f.readlines()
                sorted_files[file.name] = len(data)
                f.close
    sorted_files = sorted(sorted_files.items(), key=lambda i: i[1])  # сортируем файлы по кол-ву строк
    
    print(sorted_files)
    
    with open(f"result/result.txt", 'w+', encoding='utf-8') as f1:  # создаём новый файл для запси
        for file in sorted_files:
            with open(f"{initial_path}/{file[0]}", encoding='utf-8') as f2:  # в каждом файле считываем содержимое
                f1.write(file[0] + '\n')
                f1.write(str(file[1]) + '\n')
                f1.write(f2.read() + '\n')
        f1.seek(0)
        print(f1.read())
        f1.close

file_generator()