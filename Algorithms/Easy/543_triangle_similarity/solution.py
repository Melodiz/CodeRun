# Solution for https://coderun.yandex.ru/problem/triangle-similarity/

from functools import lru_cache
@lru_cache(maxsize=None)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def normalize_triangle(sides):
    # Sort sides to ensure consistent ordering
    sides = sorted(sides)
    
    # Find GCD of all three sides
    g = gcd(sides[0], gcd(sides[1], sides[2]))
    
    # Return normalized sides as a tuple (for hashing)
    return (sides[0] // g, sides[1] // g, sides[2] // g)

def main():
    n = int(input())
    unique_triangles = set()

    for _ in range(n):
        sides = list(map(int, input().split()))
        normalized = normalize_triangle(sides)
        unique_triangles.add(normalized)
    
    print(len(unique_triangles)) 

if __name__ == "__main__":
    main()
