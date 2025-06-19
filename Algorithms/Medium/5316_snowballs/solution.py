# Solution for https://coderun.yandex.ru/problem/snowballs
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        a %= 3
        b %= 3
        c %= 3
        print(0 if a^b^c == 0 else 1)

if __name__ == "__main__":
    main()
