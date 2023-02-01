alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def numeric_to_alpha(number: int) -> str:
    number += 1
    string = ''

    while number > 0:
        number -= 1
        string += alphabet[number%len(alphabet)]
        number = number//len(alphabet)

    return string[::-1]

def alpha_to_numeric(string: str) -> int:
    string = string.upper()

    number = 0
    for c in string:
        number = len(alphabet)*number + (ord(c)-ord('A')) + 1
    number -= 1

    return number