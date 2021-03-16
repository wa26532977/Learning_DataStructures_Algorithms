
# def anagram(s1, s2):
#     array_1 = [s for s in s1.replace(" ", '').lower]
#     array_2 = [s for s in s2.replace(" ", '').lower]
#
#     if len(array_1) != len(array_2):
#         print("string length is not equal")
#         return False
#     print(array_1)
#     print(array_2)
#     print(array_1)
#     for item in array_1:
#         try:
#             array_2.remove(item)
#         except:
#             print(f"{item} is not found in {s2}")
#             return False
#
#         return True

#
# def anagram(s1, s2):
#     a_1 = s1.replace(" ", '').lower()
#     a_2 = s2.replace(" ", '').lower()
#     print(a_1)
#     print(sorted(a_1))
#     return sorted(a_1) == sorted(a_2)


def count_letter(string):
    count = {}
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


def anagram(s1, s2):
    s1 = s1.replace(" ", '').lower()
    s2 = s2.replace(" ", '').lower()

    if len(s1) != len(s2):
        return False

    count_1 = count_letter(s1)
    count_2 = count_letter(s2)
    if count_1 == count_2:
        return True


print(anagram("dog", 'god'))
