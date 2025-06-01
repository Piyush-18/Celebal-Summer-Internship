def average(array):
    unique_elements = set(array)
    avg = sum(unique_elements) / len(unique_elements)
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)