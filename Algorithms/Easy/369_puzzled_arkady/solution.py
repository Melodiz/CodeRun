# Solution for https://coderun.yandex.ru/problem/puzzled-arkady
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    p = float(input())
    probability = (1-p) * p**2
    print(f"{1/probability:.4f}")
if __name__ == "__main__":
    main()
