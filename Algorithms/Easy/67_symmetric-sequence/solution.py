def is_symmetrical(a):
    if a == a[::-1]: return True
    return False

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    tail = []
    for i in range(n+1):
        if is_symmetrical(seq + tail[::-1]):
            break
        else:
            tail.append(seq[i])

    print(len(tail))
    print(*tail[::-1])

if __name__ == "__main__":
    main()

