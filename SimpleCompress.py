def simple_compress(text: str) -> str:
    res = ""
    count = 1
    c_char = text[0]

    for char in text[1:]:
        if char == c_char:
            count += 1
        else:
            res += f"{count}{c_char}"
            count = 1
            c_char = char
    res += f"{count}{c_char}"

    return res


print(simple_compress("AAAABBCC"))