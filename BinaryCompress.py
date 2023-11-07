def dec_to_base(num: int, base: int) -> str:
    res = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            dig = str(dig)
        else:
            dig = chr(ord("A") + dig - 10)

        num //= base
        res += dig
    return res[::-1]


def compress(text: str):
    res = ""
    for char in text:
        char = ord(char)
        res += dec_to_base(char, 2)

    return res


print(compress("AB"))