s = input()
numbers = sorted([int(x) for x in s.split('+')])
result = '+'.join(map(str, numbers))
print(result)
