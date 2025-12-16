import os
from project_folder.file_utils import get_files_in_folder, read_text_file

def main():
    """Главная функция программы."""
    print("=" * 60)
    print("📂 Анализ текстовых файлов в корпусе")
    print("=" * 60)

    # 1. Получить список файлов
    corpus_folder = "corpus"
    print(f"\n🔍 Поиск файлов в папке '{corpus_folder}'...")
    files = get_files_in_folder(corpus_folder)
   
    if not files:
        print("❌ Файлы не найдены!")
    return

    for i, name in enumerate(files, start=1): 
        print(f" {i}. {name}")
           

    # 2. Прочитать и показать содержимое каждого файла
    print(f"\n{'=' * 60}")
    print("📄 Содержимое файлов:")
    print("=" * 60)

    for filename in files:
       path = os.path.join(corpus_folder, filename) 
       content = read_text_file(path) 
       print(f"Файл: {filename} {content}") 

    print("\n✅ Обработка завершена!")


def count_words(text): 
    """Считает количество слов"""
    count_1 = len(text.split())
    return count_1

import os
def analyze_corpus(corpus_folder):
    """
    Анализирует все тексты в папке, сохраняет результаты и выводит статистику.

    Args:
        corpus_folder (str): Путь к папке с текстами (например, 'corpus')
    """
    
    txt_files = get_files_in_folder(corpus_folder)
    data = []

    for filename in txt_files:
        if filename.endswith('.txt'):
            file_path = os.path.join(corpus_folder, filename)
            text = read_text_file(file_path)
            word_count_value = count_words(text)
            data.append([filename, word_count_value])

    csv_path = 'results/statistics.csv'
    headers = ['filename', 'word_count']
    write_csv_file(csv_path, data, headers)
    
    loaded_data = read_csv_file(csv_path)  

    print(f"Количество проанализированных файлов: {len(loaded_data)}")
    
    for row in loaded_data:
        print(f"{row['filename']}: {row['word_count']} слов")

    total_words = sum(int(row['word_count']) for row in loaded_data)
    print(f"Общее количество слов в корпусе: {total_words}")

    average_words = total_words / len(loaded_data) if loaded_data else 0
    print(f"Среднее количество слов на файл: {average_words:.2f}")


if __name__ == "__main__":
    analyze_corpus("corpus")