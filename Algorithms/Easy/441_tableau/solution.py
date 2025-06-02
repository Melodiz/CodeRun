# Solution for https://coderun.yandex.ru/problem/tableau
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    data = dict([input(), 0] for _ in range(int(input())))
    a_score, b_score = 0, 0
    for _ in range(int(input())):
        score, name = input().split()
        new_a, new_b = map(int, score.split(':'))
        diff = abs(a_score-new_a) + abs(b_score-new_b)
        data[name] += diff
        a_score, b_score = new_a, new_b
    data = sorted(data.items(), key=lambda x: (x[1], x[0]), reverse=True)
    print(data[0][0],data[0][1])

if __name__ == "__main__":
    main()
