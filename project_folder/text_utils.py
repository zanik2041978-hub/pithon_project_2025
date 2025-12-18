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



def count_unique_words(text):
    """
    Возвращает количество уникальных слов.
    
    Args: 
        words (str): Слова, взятые из текста
        
    Returns:  
        int: Количество уникальных слов 
    """  
    if not text or text.isspace():
        return 0
    
    words = text.split()
    unique_words = set(words)
    return len(unique_words)



def calculate_ttr(text):
    """
    Рассчитывает ttr.

    Args:
        text (str): Текст для анализа
        
    Returns:
        float: Значение TTR от 0.0 до 1.0
    """
    total_words = word_count(text)
    if total_words == 0:
        return 0.0
    
    unique_words = count_unique_words(text)
    return unique_words / total_words


def get_most_common_words(text, n=10):
    """
    Возвращает n самых часто встречающихся в тексте слов.
    
    Args:
        text (str): Текст для анализа
        n (int): Количество возвращаемых слов (10)
        
    Returns:
        list: Список кортежей в формате (слово, количество_вхождений)
    """
    if not text or text.isspace():
        return []
    
    from collections import Counter
    
    words = text.split()
    word_counter = Counter(words)
    return word_counter.most_common(n)


def count_lines(text):
    """Подсчитывает строки в тексте
    Args: 
        text (str): Текст для анализа

    Returns: 
        int: Количество строк
    """
    lines = text.split('\n')
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