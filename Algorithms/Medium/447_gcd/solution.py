# Solution for https://coderun.yandex.ru/problem/gcd
# Other solutions: https://github.com/Melodiz/CodeRun
from collections import Counter

def factorize(n):
    factors = []
    for d in range(2, int(n**0.5) + 1):
        while n % d == 0:
            factors.append(d)
            n //= d
    if n > 1:
        factors.append(n)
    return factors

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    a_factors = []
    b_factors = []
    for i in range(n):
        a_factors.extend(factorize(a[i]))
    for i in range(m):
        b_factors.extend(factorize(b[i]))
    ans = 1
    a = Counter(a_factors)
    b = Counter(b_factors)
    flag = False
    for k, v in a.items():
        if k in b.keys():
            ans *= k ** min(v, b[k])
            if ans > 10**9:
                flag = True
                ans %= 10**9
    if flag:
        print('0'*(9-len(str(ans)))+str(ans))
    else:
        print(ans)

if __name__ == "__main__":
    main()
