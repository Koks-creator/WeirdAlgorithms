def bad_char_haur(string, size):
    bad_char = [-1] * 256

    for i in range(size):
        bad_char[ord(string[i])] = i

    return bad_char


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    s = 0
    bad_chars = bad_char_haur(pat, m)
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            s += (m - bad_chars[ord(txt[s+m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_chars[ord(txt[s+j])])

    return s


print(search("koksziom", "ziom"))
