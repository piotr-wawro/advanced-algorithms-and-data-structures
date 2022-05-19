import random

def random_color() -> str:
    base = [
        random.randint(0, 83),
        random.randint(84, 166),
        random.randint(167, 255),
    ]
    random.shuffle(base)

    return f'#{base[0]:02x}{base[1]:02x}{base[2]:02x}'
