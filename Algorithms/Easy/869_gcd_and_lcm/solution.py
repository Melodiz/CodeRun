# Solution for https://coderun.yandex.ru/problem/gcd-and-lcm/

def gcd(a, b):
    while b!=0:
        return gcd(b, a % b)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b))


if __name__ == "__main__":
    main()
