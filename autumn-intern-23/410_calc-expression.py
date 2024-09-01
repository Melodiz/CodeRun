import sys


def main():
    row = input()
    data = []
    num = ''
    for i in range(len(row)):
        if row[i] == '+':
            data.append(int(num))
            data.append('+')
            num = ''
        elif row[i] == '-':
            data.append(int(num))
            data.append('-')
            num = ''
        else:
            num += row[i]
    data.append(int(num))
    ans = data[0]
    for i in range(1, len(data), 2):
        if data[i] == '+':
            ans += data[i+1]
        else:
            ans -= data[i+1]

    print(ans)
    sys.exit(0)


if __name__ == '__main__':
    main()
