# Solution for https://coderun.yandex.ru/problem/summ-of-the-various
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    print(sum(set(map(int, input().split()))))

if __name__ == "__main__":
    main()
