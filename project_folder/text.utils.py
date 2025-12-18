"""
Модуль для анализа текстов.

Содержит функции для подсчёта слов, уникальных слов,
вычисления метрик и частотного анализа.
"""

from collections import Counter


def word_count(text):
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

#def calculate_ttr(text):
    #pass


#def get_most_common_words(text, n=10):
    #pass

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
    """Возвращает среднюю длину слова в тексте (float).
    
    Args:
        text (str): Текст для анализа
        
    Returns:
        float: Средняя длина слова
    """
    if not text or not text.strip():
        return 0.0
    
    words = text.split()

    total_len = sum(len(word) for word in words)
    return total_len / len(words)
