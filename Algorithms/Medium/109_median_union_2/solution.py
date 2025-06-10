# Solution for https://coderun.yandex.ru/problem/median-union-2
# Other solutions: https://github.com/Melodiz/CodeRun

def get_median_optimized(seq1, seq2, l):
    low = 0
    high = l

    while low <= high:
        partition1 = (low + high) // 2
        
        partition2 = l - partition1

        max_left1 = seq1[partition1 - 1] if partition1 > 0 else float('-inf')
        min_right1 = seq1[partition1] if partition1 < l else float('inf')

        max_left2 = seq2[partition2 - 1] if partition2 > 0 else float('-inf')
        min_right2 = seq2[partition2] if partition2 < l else float('inf')

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            return int(max(max_left1, max_left2))
        elif max_left1 > min_right2:
            high = partition1 - 1
        else:
            low = partition1 + 1

def main():
    n, l = map(int, input().split())
    params = [list(map(int, input().split())) for _ in range(n)]

    seqs = []
    for x1, d1, a, c, m in params:
        seq = [x1]
        d_cur = d1
        for _ in range(1, l):
            seq.append(seq[-1] + d_cur)
            d_cur = (a * d_cur + c) % m
        seqs.append(seq)

    for i in range(n):
        for j in range(i + 1, n):
            median = get_median_optimized(seqs[i], seqs[j], l)
            print(median)

if __name__ == "__main__":
    main()