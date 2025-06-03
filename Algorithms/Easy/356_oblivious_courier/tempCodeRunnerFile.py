# Solution for https://coderun.yandex.ru/problem/oblivious-courier
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n, k = map(int, input().split())
    # Due to the rotational symmetry of the problem, each house
    # has exactly the same probability of being visited last, regardless of
    # the starting position or the specific house number.

    probability = 1.0 / n
    print(probability)

if __name__ == "__main__":
    main()
