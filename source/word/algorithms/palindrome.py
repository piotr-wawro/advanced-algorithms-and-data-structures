import math

def palindrome(word: str) -> True | False:
    k: int = 0
    l: int = len(word) - 1

    for _ in range(math.floor(len(word)/2)):
        if word[k] != word[l]:
            return False

        k += 1
        l -=1

    return True
