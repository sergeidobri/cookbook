def file_reader(files_dirs: list[str]) -> list[dict]:
    """
    Функция, которая читает файлы и создает список словарей. 
    Каждый словарь включает в себя относительный путь к файлу, 
    количество строчек в файле и содержание файла.
    """
    result_list = []
    for file_directory in files_dirs:
        try:
            with open(file_directory) as f:
                lines = f.readlines()
                result_list.append({
                    "name": file_directory,
                    "lines_count": len(lines),
                    "content": "".join(lines),
                })
        except FileNotFoundError:
            print(f'Неправильное имя файла {file_directory}')
            return -1
    return result_list

def file_writer(result_file_name: str, list_files: list[dict]) -> None:
    """
    Функция, которая записывает все исходные файлы в конечный с именем
    result_file_name. Запись файлов в результирующий происходит по очереди:
    сначала list_files[0], затем list_files[1] и тд.
    """
    with open(result_file_name, "w") as result:
        for file_dict in list_files:
            result.write(f"{file_dict['name']}\n" + 
                           f"{file_dict['lines_count']}\n" + 
                           f"{file_dict['content']}\n")

def main():
    files = [  # данные, известные по условию
        'task3_files/test1.txt',
        'task3_files/test2.txt',
        ]
    result_f_name = 'res_file.txt'  # имя конечного файла
    files_list = file_reader(files)
    if files_list == -1:
        return 0
    files_list.sort(key=lambda x: x['lines_count'])
    file_writer(result_f_name, files_list)

if __name__ == "__main__":
    main()