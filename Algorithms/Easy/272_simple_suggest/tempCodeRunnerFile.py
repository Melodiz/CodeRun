# Solution for https://coderun.yandex.ru/problem/simple-suggest
# Other solutions: https://github.com/Melodiz/CodeRun

from collections import Counter
def main():
    n = int(input())
    print(tuple(Counter([input()[0].lower() for _ in range(n)]))[0])

if __name__ == "__main__":
    main()
