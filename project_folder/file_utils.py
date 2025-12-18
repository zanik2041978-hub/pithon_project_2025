"""
Модуль для работы с файлами.

Содержит функции для чтения текстовых файлов, CSV-файлов
и записи результатов анализа.
"""

import os



def get_files_in_folder(folder_path, extension='.txt'):
    """
    Получает список файлов в указанной папке с заданным расширением.

    Args:
        folder_path (str): Путь к папке
        extension (str): Расширение файлов (по умолчанию '.txt')

    Returns:
        list: Список имен файлов с указанным расширением
    """
    import os
    files = [f for f in os.listdir(folder_path) if f.endswith(extension)] 
    return files
        # добавить в список
if __name__ == "__main__":
    files = get_files_in_folder('corpus', '.txt')
    for file in files:
        print(f" - {file}")




def read_text_file(filepath):
    """
    Читает содержимое текстового файла.

    Args:
        filepath (str): Путь к файлу

    Returns:
        str: Содержимое файла или сообщение об ошибке
    """
    try: 
        with open(filepath, 'r', encoding='utf-8') as f: 
            return f.read() 
    except FileNotFoundError: 
            return "Ошибка: Файл не найден" 
    except UnicodeDecodeError: 
        return "Ошибка: Неверная кодировка файла"
if __name__ == "__main__":
    # Тест функции get_files_in_folder
    files = get_files_in_folder('corpus', '.txt')
    print(f"Найдено файлов: {len(files)}")


def read_csv_file(filename):
    """
    Читает CSV-файл и возвращает список словарей.
    Args:
        filepath (str): Путь к CSV файлу

    Returns:
        list: Список словарей, где ключи — названия колонок
    """
    data = []
    try:
        with open(filename, "r", encoding='utf-8') as file:
            content = file.readlines()
            headers = content[0].strip().split(',')
            for line in content[1:]:
                data_dict_for_one_row = {}
                values = line.strip().split(',')
                
                for i in range(len(values)):
                   data_dict_for_one_row[headers[i]] = values[i]

                data.append( data_dict_for_one_row)      
        
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        return data
     
      
if __name__ == "__main__":
    metadata = read_csv_file('data/metadata.csv')

    print(f"Загружено записей: {len(metadata)}")

    if metadata:
        print("\nПервая запись:")
        print(metadata[0])

        print("\nВсе записи:")
        for row in metadata:
            print(f"  - {row['filename']}: {row['title']} ({row['author']}, {row['year']})")


def write_csv_file(filepath, data, headers):
    """
    Записывает данные в CSV файл.

    Args:
        filepath (str): Полный путь к файлу, включая папку и название файла
                       Например: 'results/statistics.csv'
        data (list): Список списков [[val1, val2], [val1, val2], ...]
        headers (list): Список заголовков ['col1', 'col2']

    Returns:
        bool: True если успешно
    """
    
    folder = os.path.dirname(filepath)  # Из 'results/statistics.csv' получаем 'results'
    os.makedirs(folder, exist_ok=True)  # Создаём папку results/
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(','.join(headers) + '\n')
        for row in data:
            f.write(','.join(str(v) for v in row) + '\n')
    return True



import os

data = [
    ['text_1.txt', 523],
    ['text_2.txt', 612],
    ['text_3.txt', 498]
]
headers = ['filename', 'word_count']
print(write_csv_file('results/statistics.csv', data, headers))


def write_text_file(filepath, content):
    pass



def count_words(text):
    """
    Подсчитывает количество слов в тексте.

    Args:
        text (str): Текст для анализа

    Returns:
        int: Количество слов
    """
    if not text or text.isspace():
        return 0
    
    words = text.split()
    return len(words)

