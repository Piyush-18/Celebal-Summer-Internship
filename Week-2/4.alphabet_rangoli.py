import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    width = 4 * size - 3  # Max width of the rangoli

    for i in range(size):
        left = alphabet[size-1:i:-1]   # descending part
        right = alphabet[i:size]       # ascending part (including center)
        row = '-'.join(left + right)
        lines.append(row.center(width, '-'))

    # top half + bottom half (excluding center repeated)
    for line in lines[::-1] + lines[1:]:
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)