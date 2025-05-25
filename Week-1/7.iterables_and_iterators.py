from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total = list(combinations(letters, k))

# Count combinations with at least one 'a'
count = sum(1 for combo in total if 'a' in combo)

# Compute and print probability
probability = count / len(total)
print(f"{probability:.3f}")
