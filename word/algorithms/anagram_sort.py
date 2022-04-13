def anagram_sort(text1: str, text2: str) -> True | False:
    text1 = text1.replace(' ', '').lower()
    text2 = text2.replace(' ', '').lower()
    text1 = sorted(text1)
    text2 = sorted(text2)

    if text1 == text2:
        return True
    else:
        return False