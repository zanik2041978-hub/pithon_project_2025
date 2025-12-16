def analyze_multiple_files(file_paths):
    """
    Принимает список путей к файлам и анализирует их все
    """
    all_results = {}
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                analysis = your_analysis_function(text)  # Замените на вашу функцию
                all_results[file_path] = analysis
    
    return all_results


def get_words_by_pos(text, target_pos):
    """
    Извлекает слова определённой части речи.

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

text = """
Понимая, что нет в оправданиях смысла,
Что бесчестье кромешно и выхода нет,
Наши предки писали предсмертные письма,
А потом, помолившись: «Во веки и присно…» —
Запирались на ключ — и к виску пистолет.

А нам и честь, и чех, и черт —
Неведомые области!
А нам признание и почет
За верность общей подлости!
А мы баюкаем внучат
И ходим на собрания,
И голоса у нас звучат
Все чище и сопраннее!..
"""

nouns = get_words_by_pos(text, 'NOUN')
verbs = get_words_by_pos(text, 'VERB')

print("🏠 Существительные:", set(nouns))
print("🏃 Глаголы:", set(verbs))
