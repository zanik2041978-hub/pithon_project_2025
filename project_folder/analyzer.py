def read_file(filename):
    """Читает и возвращает содержимое файла"""
    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()
        return content

def count_nonempty_lines(text):
    """Считает количество непустых строк"""  
    count = 0
    lines = text.split("\n")
    for line in lines:
        if line.strip():
            count += 1
    return count        

def count_words(text): 
    """Считает количество слов"""
    count_1 = len(text.split())
    return count_1

def display_results(lines_count, words_count): 
    """Печатает результаты в 2-3 аккуратных строках"""
    print(f"Количество непустых строк: {lines_count}") 
    print(f"Количество слов: {words_count}")
    print(f"Первые две строки исходного текста:")
    for line in two_lines:
        print(line)

if __name__ == "__main__" :
    text = read_file("project_folder/poem.txt")
    lines_count = count_nonempty_lines(text)
    words_count = count_words(text)
    lines = text.splitlines()
    two_lines = lines[:2]
    display_results(lines_count, words_count)