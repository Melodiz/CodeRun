import sys
from collections import Counter


def main():
    letters = []
    for line in sys.stdin.readlines():
        line = line.strip().replace(' ', '').replace('\n', '')
        letters.extend(list(line))
    data = Counter(letters)
    symbols = sorted(set(data.keys()))
    m = max(data.values())
    while m > 0:
        line = ''
        for symbol in symbols:
            if data[symbol] >= m:
                line += '#'
            else:
                line += ' '
        print(line)
        m -= 1
    print(''.join(symbols))


if __name__ == "__main__":
    main()
