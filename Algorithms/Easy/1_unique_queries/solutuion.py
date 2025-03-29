import hashlib
import math

def main():
    n = int(input())
    m = 2 ** 14
    M = [0] * m

    for i in range(n):
        x = hashlib.sha256(str.encode(input().strip())).digest()[:4]
        idx = int.from_bytes(x, byteorder='little') % m
        M[idx] = 1

    print(m * math.log(m / M.count(0)))

if __name__ == "__main__":
    main()