# Solution for https://coderun.yandex.ru/problem/next-lucky-ticket
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    for k in range(int(n)+1, 1000000):
        if is_lucky(k):
            print(k)
            break
    return

def is_lucky(k):
    return sum(map(int, str(k)[:3])) == sum(map(int, str(k)[3:]))

if __name__ == "__main__":
    main()
