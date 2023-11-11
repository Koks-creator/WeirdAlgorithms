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


def rle(text: str):
    res = ""
    for char in text:
        char = ord(char)
        binar = dec_to_base(char, 2)
        zeros_to_add = 8 - len(binar)
        binar = zeros_to_add * "0" + binar

        binar2 = ""
        count = 0
        for i in binar:
            if i == "0":
                count += 1
            else:
                binar2 += str(count)
                count = 0
                binar2 += "1"

        res += binar2

    return res


print(rle("!AB*"))