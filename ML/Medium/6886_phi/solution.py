# Solution for https://coderun.yandex.ru/problem/phi/

def euler_totient_optimized(n):
    result = n
    p = 2
    while p * p <= n:
        # Check if p is a prime factor
        if n % p == 0:
            # If yes, then update n and result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    if n > 1:
        result -= result // n
    
    return result

if __name__ == "__main__":
    n = int(input())
    print(euler_totient_optimized(n))