def solution(n: int) -> int:
    if n < 5:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime.
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    count1_mod4 = 0
    count3_mod4 = 0
    for p in range(3, n + 1):
        if is_prime[p]:
            if p % 4 == 1:
                count1_mod4 += 1
            elif p % 4 == 3:
                count3_mod4 += 1
    return count1_mod4 * count3_mod4