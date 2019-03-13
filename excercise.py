
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):

    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix


print(ordinal(4))
print(ordinal(3))
print(ordinal(15))
