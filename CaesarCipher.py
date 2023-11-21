def caesar_cipher(text: str, move: int) -> str:
    res = ""
    for char in text:
        char = ord(char)
        if 65 <= char <= 90:
            res += chr((char - ord("A") + move) % 26 + ord("A"))
        elif 97 <= char <= 122:
            res += chr((char - ord("a") + move) % 26 + ord("a"))
        else:
            res += char
    return res


print(caesar_cipher("AB", -2))
