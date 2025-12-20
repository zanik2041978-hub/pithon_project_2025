import os
from file_utils import get_files_in_folder, read_text_file
from text_utils import word_count, count_unique_words, calculate_ttr, count_lines, average_word_length
from file_utils import write_csv_file, read_csv_file



def analyze_single_text(filepath, filename):
    """
    Анализирует один текстовый файл и возвращает словарь с результатами.
    
    Args:
        filepath (str): Полный путь к файлу
        filename (str): Имя файла
    
    Returns:
        dict: Словарь с результатами анализа
    """
        
    text = read_text_file(filepath)
          
    word_count_value = word_count(text)
    unique_words_value = count_unique_words(text)
    ttr_value = calculate_ttr(text)
    lines_count = count_lines(text)
    avg_word_len = average_word_length(text)
        
    result = {
        'filename': filename,
        'word_count': word_count_value,
        'unique_words': unique_words_value,
        'ttr': ttr_value,
        'lines': lines_count,
        'avg_word_length': avg_word_len,      
    }
    
    return result




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

    print("-" * 80)
    print("-" * 80) 
    print("ОТЧЕТ ПО АНАЛИЗУ КОРПУСА А. ГАЛИЧА")
    print("-" * 80)
    print("-" * 80)


    print("ОБЩАЯ СТАТИСТИКА:")
    loaded_data = read_csv_file(csv_path) 
    print(f"Всего текстов: {len(loaded_data)}")
    
    total_words = sum(int(row['word_count']) for row in loaded_data)
    print(f"Всего слов: {total_words}")

    total_unique_words = sum(int(row['unique_words']) for row in loaded_data)
    print(f"Уникальных слов: {total_unique_words}")

    average_ttr = sum(float(row['ttr']) for row in loaded_data) / len(loaded_data)
    print(f"Средний TTR: {average_ttr:.3f}")
    

    print("ДЕТАЛЬНАЯ СТАТИСТИКА ПО ФАЙЛАМ:") 
    print("-" * 80)
    for row in loaded_data:
        print(f"Файл: {row['filename']}")
        print(f"Строк: {row['lines']}")
        print(f"Слов: {row['word_count']}")
        print(f"Уникальных слов: {row['unique_words']}")
        print(f"TTR: {row['ttr']}")
        print(f"Средняя длина слова: {row['avg_word_length']}")
    
             

def generate_report():
    """
    Создает файл report.txt с общей статистикой, статистикой для каждого текста и выводами
    """
    from file_utils import read_csv_file
    import os
        
    os.makedirs('results', exist_ok=True)
    
    data = read_csv_file('results/statistics.csv')
    
    if not data:
        print("Данные не найдены")
        return
    
    metadata = read_csv_file('data/metadata.csv')
        
    titles_dict = {}
    if metadata:
        for item in metadata:
            filename = item.get('filename', '')
            title = item.get('title', '')
            if filename and title:
                titles_dict[filename] = title
    else:
        print("Файл metadata.csv не найден или пуст")
    
    with open('results/report.txt', 'w', encoding='utf-8') as f:      
        f.write("-" * 80 + "\n")
        f.write("-" * 80 + "\n")
        f.write("ОТЧЕТ ПО АНАЛИЗУ КОРПУСА А. ГАЛИЧА\n")
        f.write("-" * 80 + "\n")
        f.write("-" * 80 + "\n\n")
               
        f.write("ОБЩАЯ СТАТИСТИКА:\n")
        
        total_files = len(data)
        f.write(f"Всего текстов: {total_files}\n")
        
        total_words = sum(int(r['word_count']) for r in data)
        f.write(f"Всего слов: {total_words}\n")
        
        total_unique = sum(int(r['unique_words']) for r in data)
        f.write(f"Уникальных слов: {total_unique}\n")
        
        avg_ttr = sum(float(r['ttr']) for r in data) / total_files
        f.write(f"Средний TTR: {avg_ttr:.3f}\n\n")
       
        f.write("ДЕТАЛЬНАЯ СТАТИСТИКА ПО ФАЙЛАМ:\n")
        f.write("-" * 80 + "\n")

    
        def file_key(filename):
            try:
                return int(filename.replace('text_', '').replace('.txt', ''))
            except:
                return 0
        
        sorted_data = sorted(data, key=lambda x: file_key(x['filename']))
        
        most_diverse_text = None
        most_diverse_ttr = 0
        most_diverse_title = ""
        
        longest_text = None
        longest_word_count = 0
        longest_title = ""
        
        shortest_text = None
        shortest_word_count = float('inf')
        shortest_title = ""
                
        for row in sorted_data:
            filename = row['filename']
            title = titles_dict.get(filename, filename)
            ttr = float(row['ttr'])
            word_count_val = int(row['word_count'])
                        
            if ttr > most_diverse_ttr:
                most_diverse_ttr = ttr
                most_diverse_text = filename
                most_diverse_title = title
            
            if word_count_val > longest_word_count:
                longest_word_count = word_count_val
                longest_text = filename
                longest_title = title
                        
            if word_count_val < shortest_word_count:
                shortest_word_count = word_count_val
                shortest_text = filename
                shortest_title = title
                        
            f.write(f"Текст: {title}\n")
            f.write(f"Файл: {filename}\n")
            f.write(f"Строк: {row['lines']}\n")
            f.write(f"Слов: {row['word_count']}\n")
            f.write(f"Уникальных слов: {row['unique_words']}\n")
            f.write(f"TTR: {row['ttr']}\n")
            f.write(f"Средняя длина слова: {row['avg_word_length']}\n")
            f.write("\n")
               
        f.write("ВЫВОДЫ:\n")
                           
        if most_diverse_title:
            f.write("1. Самый лексически разнообразный текст:\n")
            f.write(f"{most_diverse_title}\n")
            f.write(f"TTR: {most_diverse_ttr:.3f}\n")
            f.write(f"Уникальных слов: {next(r['unique_words'] for r in data if r['filename'] == most_diverse_text)}\n")
            f.write(f"Всего слов: {next(r['word_count'] for r in data if r['filename'] == most_diverse_text)}\n")
            f.write("\n")
                
        if longest_title:
            f.write("2. Самый длинный текст:\n")
            f.write(f"{longest_title}\n")
            f.write(f"Всего слов: {longest_word_count}\n")
            f.write(f"Строк: {next(r['lines'] for r in data if r['filename'] == longest_text)}\n")
            f.write("\n")
              
        if shortest_title:
            f.write("3. Самый короткий текст:\n")
            f.write(f"{shortest_title}\n")
            f.write(f"Всего слов: {shortest_word_count}\n")
            f.write(f"Строк: {next(r['lines'] for r in data if r['filename'] == shortest_text)}\n")
    
    print("Файл со статистикой создан: results/report.txt")


def main():
    """
    Главная функция программы. Является точкой входа, вызывает все остальные функции и сохраняет результаты".       
    """
    print("=" * 60)
    print("Анализ корпуса текстов Галича")
    print("=" * 60)
    
    corpus_folder = 'corpus'
        
    if not os.path.exists(corpus_folder):
        print(f"Папка '{corpus_folder}' не найдена")       
        return       
         
    print(f"Поиск файлов в папке '{corpus_folder}'")
    files = get_files_in_folder(corpus_folder, '.txt')  

    if not files:
        print("Файлы не найдены")
        return
    print(f"Найдено файлов: {len(files)}")
    print("Список файлов для анализа:")

    for i, filename in enumerate(files, start=1):
        print(f"{i}. {filename}")
        
    print("Анализ текстов и сохранение статистики")
    analyze_corpus(corpus_folder)
      
    print("Создание отчета")
    generate_report()
       
    print("Результаты сохранены в папке 'results/':")
    if os.path.exists('results'):
        for file in ['statistics.csv', 'report.txt']:
            filepath = os.path.join('results', file)
            if os.path.exists(filepath):
                size = os.path.getsize(filepath)
                print(f"{file} ({size})")
            else:
                print(f"{file} (не создан)")
 
if __name__ == "__main__":

    main()
