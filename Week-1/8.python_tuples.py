if __name__ == '__main__':
    n = int(input())
    elements = map(int, input().split())
    t = tuple(elements)
    print(hash(t))
