#function to count how many vowels are present in a given string.abs

def count_vowels(s):
    s = s.lower()
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    
    return count


print(count_vowels("Hello World"))