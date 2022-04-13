import json
from word.algorithms.anagram_sort import anagram_sort

def anagram_in_text(word: str) -> list[str]:
    with open('word/algorithms/words_en.json', 'r') as file:
        dict_words = json.load(file)

    anagrams: list[str] = []

    for dict_word in dict_words[f'{len(word)}']:
        if anagram_sort(word, dict_word):
            anagrams.append(dict_word)

    return anagrams
