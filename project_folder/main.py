import os
from file_utils import get_files_in_folder, read_text_file
from project_folder.text_utils import word_count
from file_utils import write_csv_file, read_csv_file

def main():
    """Главная функция программы."""
    print("=" * 60)
    print("📂 Анализ текстовых файлов в корпусе")
    print("=" * 60)

    # 1. Получить список файлов
    corpus_folder = 'corpus'
    print(f"\n🔍 Поиск файлов в папке '{corpus_folder}'...")

    files = get_files_in_folder(corpus_folder, '.txt')  # ← ВАЖНО

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
    # Часть 1: Анализ и сохранение
    txt_files = get_files_in_folder(corpus_folder)
    data = []

    for filename in txt_files:
        if filename.endswith('.txt'):
            file_path = os.path.join(corpus_folder, filename)
            text = read_text_file(file_path)
            word_count_value = word_count(text)
            data.append([filename, word_count_value])

    csv_path = 'results/statistics.csv'
    headers = ['filename', 'word_count']
    write_csv_file(csv_path, data, headers)

    # Часть 2: Загрузка и вывод статистики
    loaded_data = read_csv_file(csv_path)  # возвращает список словарей

    print(f"Количество проанализированных файлов: {len(loaded_data)}")

    # Список файлов с количеством слов
    for row in loaded_data:
        print(f"{row['filename']}: {row['word_count']} слов")

    # Общее количество слов
    total_words = sum(int(row['word_count']) for row in loaded_data)
    print(f"Общее количество слов в корпусе: {total_words}")

    # Среднее количество слов на файл
    average_words = total_words / len(loaded_data) if loaded_data else 0
    print(f"Среднее количество слов на файл: {average_words:.2f}")


if __name__ == "__main__":
    analyze_corpus("corpus")
