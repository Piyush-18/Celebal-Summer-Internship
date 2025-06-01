n = int(input())
numbers = sorted(set(map(int, input().split())))

N = int(input())
for _ in range(N):
    cmd = input().split()
    operation = cmd[0]
    
    if operation == "pop":
        if numbers:
            numbers.pop(0)  
    elif operation == "remove":
        try:
            numbers.remove(int(cmd[1]))
        except ValueError:
            pass
    elif operation == "discard":
        if int(cmd[1]) in numbers:
            numbers.remove(int(cmd[1]))

print(sum(numbers))