from collections import Counter

# Input: number of shoes
X = int(input())

# Input: list of shoe sizes
shoe_sizes = list(map(int, input().split()))

# Count available shoe sizes
inventory = Counter(shoe_sizes)

# Input: number of customers
N = int(input())


earnings = 0


for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1  # Sell the shoe (reduce count)


print(earnings)
