def is_anagram(first_string, second_string):
    first_string = list(first_string.lower())
    second_string = list(second_string.lower())
    if len(first_string) != len(second_string):
        return (False)
    for i in first_string:
        if i not in second_string:
            return (False)
        second_string.remove(i)
    return (True)
