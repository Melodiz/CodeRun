# Solution for https://coderun.yandex.ru/problem/lap
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n, t, s = map(int, input().split())
    v = list(map(int, input().split()))
    overtakes = 0
    for i in range(1, n):
        d_rel = (v[0] - v[i]) * t 
        if d_rel > 0:
            overtakes += d_rel // s -1 if d_rel%s == 0 else d_rel // s
    print(overtakes)

if __name__ == "__main__":
    main()
