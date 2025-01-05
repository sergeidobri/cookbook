"""Модуль для записи данных файл и чтения данных из файлов"""

def file_reader(files_dirs: list[str]) -> list[tuple]:
    """
    Функция, которая читает файлы и создает список кортежей. Кортеж состоит
    из пути к файлу и числа строк в нем.
    """
    result_list = []
    for file_directory in files_dirs:
        try:
            with open(file_directory, "r", encoding="utf-8") as file:
                cnt = 0
                for _ in file:
                    cnt += 1
                result_list.append((file_directory, cnt))
        except FileNotFoundError as exp:
            raise FileNotFoundError(
                "Файл с директорией {file_directory} не был найден") from exp
    return result_list


def file_writer(result_file_name: str, list_files: list[tuple]) -> None:
    """
    Функция, которая записывает все исходные файлы в конечный с именем
    result_file_name. Запись файлов в результирующий происходит по очереди:
    сначала list_files[0], затем list_files[1] и тд.
    """
    with open(result_file_name, "w", encoding="utf-8") as result:
        for file_directory, lines_count in list_files:
            result.write(f"{file_directory}\n{lines_count}\n")
            with open(file_directory, "r", encoding="utf-8") as source:
                for line in source:
                    result.write(line)
                result.write('\n')

def main():
    """Функция, тестирующая работу с файлами"""
    files = [  # данные, известные по условию
        "task3_files/1.txt",
        "task3_files/2.txt",
        "task3_files/3.txt",
        ]
    result_f_name = 'task3_files/res_file.txt'  # имя конечного файла
    files_list = file_reader(files)
    files_list.sort(key=lambda x: x[1])
    file_writer(result_f_name, files_list)

if __name__ == "__main__":
    main()
