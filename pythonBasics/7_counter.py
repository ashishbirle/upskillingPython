#finding the most frequent element in a list

from collections import Counter

def most_frequent(lst):
    counts = Counter(lst)
    return counts.most_common(1)[0][0]


print(most_frequent([1, 2, 2, 3, 3, 3, 1]))