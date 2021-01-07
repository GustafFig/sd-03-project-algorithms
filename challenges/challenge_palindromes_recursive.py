def is_palindrome_recursive(word, low, high):
    if len(word) > 0 and low >= high:
        return True
    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False
