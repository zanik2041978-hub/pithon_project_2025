"""
Модуль для анализа текстов.

Содержит функции для подсчёта слов, уникальных слов,
вычисления метрик и частотного анализа.
"""

from collections import Counter


def read_file(filename):
    """Читает содержимое файла и возвращает строку. Возвращает None при ошибке."""
    try:
        with open(filename, "r", encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return None        


def get_words(text):
    """Возвращает список слов из текста (можно привести к нижнему регистру)."""
    text = text.lower()
    words = text.split()
    return words


def count_words(text): 
    """Считает количество слов"""
    count_1 = len(text.split())
    return count_1

#почему-то у меня есть еще 1 функция "count_words", надо разобраться, какая подходит нам и оставить 1:

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



def count_unique_words(words):
    """Возвращает количество уникальных слов.
    
    Args: 
        words (str): Слова, взятые из текста
        
    Returns:  
        int: Количество уникальных слов 
    """  
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def calculate_ttr(text):
    pass


def get_most_common_words(text, n=10):
    pass

def count_lines(text):
    """Подсчитывает строки в тексте
    Args: 
        text (str): Текст для анализа

    Returns: 
        int: Количество строк
    """
    lines = t.split('\n')
    return len(lines)


def average_word_length(text):
     """Возвращает среднюю длину слова в тексте (float)."""
    if not text or not text.strip():
        return 0.0
    
    words = text.split()

    total_len = sum(len(word) for word in words)
    return total_len / len(words)
