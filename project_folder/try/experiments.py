import pymorphy3
morph = pymorphy3.MorphAnalyzer()
print("✅ pymorphy3 готов к работе!")


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
    files = get_files_in_folder('corpus', '.txt')

def read_file(filename):
 """Читает и возвращает содержимое файла"""
 with open(filename, "r", encoding='utf-8') as file:
    content = file.read()
    return content
    
if __name__ == "__main__" :
    text = read_file('corpus', 'text_1.txt')

#попытка передать функции для работы текстовый файлик: text = get_files_in_folder('corpus', 'text_1.txt')
#print(text_1.txt)

def get_words_by_pos(text, target_pos):
    """
    Позволяет извлекать слова определённой части речи.


    Args:
        text (str): Текст для анализа
        target_pos (str): Часть речи (NOUN, VERB, ADJF, ADVB...)


    Returns:
        list: Список слов указанной части речи (в начальной форме)
    """
    morph = pymorphy3.MorphAnalyzer()


    clean_text = text.lower()
    for char in '.,!?;:—–-"«»()[]\n':
        clean_text = clean_text.replace(char, ' ')


    words = clean_text.split()
    result = []


    for word in words:
        if word:
            parsed = morph.parse(word)[0]
            if parsed.tag.POS == target_pos:
                result.append(parsed.normal_form)


    return result


text = get_files_in_folder('corpus', 'text_1.txt')

nouns = get_words_by_pos(text, 'NOUN')

nouns_set = set(nouns)

print("🏠 Существительные:", set(nouns))

common_set = {'чай','сок','вода','молоко','кисель','лимонад','компот','квас','вино','коньяк','водка','портвейн'}
common_set_elements = common_set & nouns_set
print(f"Общие элементы: {common_set_elements}")



#vocab = {"магия", "волшебство", "заклинание"}

# Добавить элемент
#vocab.add("зелье")
#print("После .add():", vocab)
