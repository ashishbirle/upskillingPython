def is_happy(n: int) -> bool:
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        #Replace n with the sum of the squares of its digits
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return True

print(is_happy(19))