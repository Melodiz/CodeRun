# Solution for https://coderun.yandex.ru/problem/tiles
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    B, W = map(int, input().split())
    
    # For a room n x m (n >= m):
    # Black tiles (perimeter): 2n + 2m - 4 = B
    # White tiles (interior): (n-2) * (m-2) = W
    
    # From the first equation: n + m = (B + 4) / 2
    # Let's call this sum S = (B + 4) / 2
    S = (B + 4) // 2
    
    import math
    
    a = 1
    b = -S
    c = 2*S - 4 + W
    
    discriminant = b*b - 4*a*c
    n1 = (-b + math.sqrt(discriminant)) / (2*a)
    n2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    # We need integer solutions
    n1 = int(round(n1))
    n2 = int(round(n2))
    
    m1 = S - n1
    m2 = S - n2
    
    # Choose the solution where n >= m
    if n1 >= m1 and (n1-2) * (m1-2) == W:
        n, m = n1, m1
    else:
        n, m = n2, m2
    
    # Ensure n >= m
    if n < m:
        n, m = m, n
    
    print(n, m)

if __name__ == "__main__":
    main()
