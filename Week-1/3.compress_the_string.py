from itertools import groupby

s = input()

result = []
for key, group in groupby(s):
    count = len(list(group))
    result.append(f"({count}, {key})")

print(' '.join(result))