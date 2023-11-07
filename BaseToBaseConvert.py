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


def base_to_dec(num: str, base: int) -> int:
    num = num[::-1]
    res = 0
    for i in range(len(num)):
        dig = num[i]
        if dig.isdigit():
            dig = int(dig)
        else:
            dig = ord(dig) - ord("A") + 10

        res += dig * (base**i)

    return res


def base_to_base(num: str, source_base: int, target_base: int) -> str:
    positive = True
    if source_base == target_base:
        return num

    if num[0] == "-":
        num = num[1:]
        positive = False

    if source_base != 10:
        num = base_to_dec(num, source_base)
    res = dec_to_base(int(num), target_base)
    return res if positive else "-" + res


print(base_to_base("1001101", 2, 16))
print(base_to_base("-1001101", 2, 16))
print(base_to_base("23", 8, 12))
