def reverse_words(str):
    str = str.strip().split()
    reversed_words = list(reversed(str))
    result = ' '.join(reversed_words)
    return result

print(reverse_words("  Hello World  "))