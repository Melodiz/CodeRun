# Solution for https://coderun.yandex.ru/problem/calculate-tags
# Other solutions: https://github.com/Melodiz/CodeRun


def main():
    n = int(input())
    fibo = [1, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    print(sum(fibo)) if n > 1 else print(1)

if __name__ == "__main__":
    main()
