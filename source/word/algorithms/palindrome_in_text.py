from word.algorithms import palindrome

def palindrome_in_text(text: str) -> list[str]:
    palindrome_idx: list[tuple[int, int]] = []

    for i in range(len(text) - 1):
        j: int = len(text)

        while  i != j - 1:
            if palindrome(text[i:j]):
                palindrome_idx.append((i, j))
            j -= 1

    return [text[i:j] for i, j in palindrome_idx]
