import random
def name_ganerate(len: int) -> str:
    x = len - 1
    arr = []
    while x >= 0:
        sym = random.randint(49, 91)
        arr.append(chr(sym))

        x -= 1
    return ''.join(arr)