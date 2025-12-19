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
            lines = file.readlines()
                                                 
            headers = lines[0].strip().split(',')
            
            for line_num, line in enumerate(lines[1:], start=2):
                line = line.strip()
                if not line: 
                    continue
                
                values = line.split(',')
                                
                if len(values) != len(headers):
                    continue
                
                row_dict = {}
                for i in range(len(headers)):
                    row_dict[headers[i]] = values[i]
                
                data.append(row_dict)
        
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
        filepath (str): Полный путь к файлу
        data (list): Список списков [[val1, val2], [val1, val2], ...]
        headers (list): Список заголовков ['col1', 'col2']

    Returns:
        bool: True если успешно, False при ошибке
    """
    try:       
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
                
        if not headers:
            print(f"Ошибка: Не указаны заголовки для файла '{filepath}'")
            return False
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(','.join(str(h) for h in headers) + '\n')                      
                                         
        print(f"Файл создан: {filepath}")
        return True
        
    except Exception as e:
        print(f"Ошибка при записи файла '{filepath}': {e}")
        return False



def write_text_file(filepath, content, encoding='utf-8'):
    """
    Записывает текст в файл

    Args:
        filepath (str): Путь к файлу
        content (str): Текст для записи
        
    Returns:
        bool: True/False
    """
    try:       
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
              
               
        with open(filepath, 'w', encoding=encoding) as f:
            f.write(content)
        
        print(f"Файл создан: {filepath}")
        return True
        
    except Exception as e:
        print(f"Возникла ошибка при создании файла'{filepath}': {e}")
        return False