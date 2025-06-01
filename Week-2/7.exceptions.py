# Input number of test cases
T = int(input())

for _ in range(T):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)

