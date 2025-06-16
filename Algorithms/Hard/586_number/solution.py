# Solution for https://coderun.yandex.ru/problem/number
# Other solutions: https://github.com/Melodiz/CodeRun

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    N = int(input())
    S = sum_of_digits(N)
    k = N/gcd(N, S)
    if k.is_integer():
        print("I got it")
        print(int(k)*str(N))
    else:
        print('Epic fail')

if __name__ == "__main__":
    main()
