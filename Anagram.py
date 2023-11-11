def bubble_sort(array: list) -> list:
    n = len(array)
    swapped = None

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

    if not swapped:
        return array
    return array


def anagram(str1: str, str2: str) -> bool:
    str2_int = [ord(char) for char in str2]

    # sort ascii letters and convert them back to char
    str2_int = bubble_sort(str2_int)
    str2 = "".join([chr(asc) for asc in str2_int])

    if str1 == str2:
        return True
    return False


print(anagram("abh", "ba"))