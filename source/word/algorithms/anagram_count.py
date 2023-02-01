def anagram_count(text1: str, text2: str) -> True | False:
    text1 = text1.replace(' ', '').lower()
    text2 = text2.replace(' ', '').lower()

    alphabet = {}

    for char in text1:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

    for char in text2:
        if char in alphabet:
            alphabet[char] -= 1
        else:
            alphabet[char] = -1

    for val in alphabet.values():
        if val != 0:
            return False

    return True
