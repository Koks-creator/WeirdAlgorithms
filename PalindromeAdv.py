def palindrome_adv(text: str) -> str:
    longest_pal = ""

    for i in range(len(text)-1):
        for j in range(len(text)-1, 0, -1):
            chunk = text[i:j]
            if chunk == chunk[::-1] and len(chunk) > 2 and len(chunk) > len(longest_pal):
                longest_pal = chunk
    return longest_pal


print(palindrome_adv("CABCBAB"))
