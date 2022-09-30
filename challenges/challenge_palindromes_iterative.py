def is_palindrome_iterative(word):
    if not word:
        return False
    word_iterative = word[::-1]
    if word == word_iterative:
        return True
    else:
        return False