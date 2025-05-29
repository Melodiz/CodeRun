# Solution for https://coderun.yandex.ru/problem/simple-suggest
# Other solutions: https://github.com/Melodiz/CodeRun

from collections import Counter
def main():
    n = int(input())
    cnt = Counter([input()[0] for _ in range(n)])
    print(cnt.most_common(1)[0][0])

if __name__ == "__main__":
    main()
