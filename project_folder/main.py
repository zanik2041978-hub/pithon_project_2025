import os
from file_utils import get_files_in_folder, read_text_file
from text_utils import word_count, count_unique_words, calculate_ttr, count_lines, average_word_length
from file_utils import write_csv_file, read_csv_file

def main():
    """Главная функция программы."""
    print("=" * 60)
    print("📂 Анализ корпуса текстов Галича")
    print("=" * 60)

    
    corpus_folder = 'corpus'
    print(f"\n🔍 Поиск файлов в папке '{corpus_folder}'...")

    files = get_files_in_folder(corpus_folder, '.txt')  

    if not files:
        print("❌ Файлы не найдены!")
        return

    print(f"✅ Найдено файлов: {len(files)}")

    print("\nСписок файлов:")
    for i, filename in enumerate(files, start=1):
        print(f"  {i}. {filename}")

    print("\n✅ Обработка завершена!")

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
            word_count_value = word_count(text)
            unique_words_value = count_unique_words(text)
            ttr_value = calculate_ttr(text)
            lines_count = count_lines(text)       
            avg_word_len = average_word_length(text)   
                  
         
            data.append([filename, word_count_value, unique_words_value, f"{ttr_value:.3f}", lines_count, f"{avg_word_len:.2f}"])

    csv_path = 'results/statistics.csv'
    headers = ['filename', 'word_count', 'unique_words', 'ttr', "lines", 'avg_word_length']
    write_csv_file(csv_path, data, headers)

    loaded_data = read_csv_file(csv_path)

    print("ДЕТАЛЬНАЯ СТАТИСТИКА ПО ФАЙЛАМ:")
    print("-" * 80)
    for row in loaded_data:
        print(f"Файл: {row['filename']}")
        print(f" Строк: {row['lines']}")
        print(f"Слов: {row['word_count']}")
        print(f"Уникальных слов: {row['unique_words']}")
        print(f"TTR: {row['ttr']}")
        print(f"Средняя длина слова: {row['avg_word_length']}")
        

    loaded_data = read_csv_file(csv_path) 
    print(f"Всего текстов: {len(loaded_data)}")

   

if __name__ == "__main__":
    analyze_corpus("corpus")