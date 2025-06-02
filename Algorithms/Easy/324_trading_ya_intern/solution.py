# Solution for https://coderun.yandex.ru/problem/trading-ya-intern
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n,m = map(int, input().split())
    bid = sorted(list(map(int, input().split())), reverse=False)
    ask = sorted(list(map(int, input().split())), reverse=True)
    i = 0
    profit = 0
    while i < min(n,m):
        if bid[i] < ask[i]:
            profit += ask[i] - bid[i]
            i += 1
        else:
            break
    print(profit)

if __name__ == "__main__":
    main()
