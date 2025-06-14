# Solution for https://coderun.yandex.ru/problem/maxim-triangle
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    data = [input().split() for _ in range(n)]
    left, right = 30, 4000
    for i in range(1, n):
        a, b = float(data[i][0]), float(data[i-1][0])
        mid = (a + b) / 2
        if a < b: 
            if data[i][1] == 'closer':
                right = min(right, mid)
            else:
                left = max(left, mid)
        else:
            if data[i][1] == 'closer':
                left = max(left, mid)
            else:
                right = min(right, mid)
    print(f"{left:.7f} {right:.7f}")
    

if __name__ == "__main__":
    main()