numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Use filter() to retain only numbers divisible by 3, then use map() to square each filtered number
result = list(map(lambda x: x**2, filter(lambda x: x % 3 == 0, numbers)))
print(result)
