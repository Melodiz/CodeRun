def reduce(s):
    result = ''
    i = 0
    while i < len(s):
        if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result += s[i]
        elif s[i] == '+':
            result += '8'
            i += 1
        i += 1
    if len(result) == 7: 
        return '8495'+result
    return result


def main():
    a, b, c, d = [input() for _ in range(4)]
    v1, v2, v3, v4 = reduce(a), reduce(b), reduce(c), reduce(d)
    print("YES") if v1 == v2 else print("NO")
    print("YES") if v1 == v3 else print("NO")
    print("YES") if v1 == v4 else print("NO")

if __name__ == "__main__":
    main()
