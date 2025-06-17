# Solution for https://coderun.yandex.ru/problem/lap-2
# Other solutions: https://github.com/Melodiz/CodeRun
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

def solve():
    n, t, s = map(int, input().split())
    v = list(map(int, input().split()))

    cars = sorted(v)

    total_overtakes = 0

    ft_counts = FenwickTree(s)
    ft_divs = FenwickTree(s)

    for current_v in cars:
        current_val = current_v * t
        current_laps = current_val // s
        current_rem = current_val % s

        count_smaller_v = ft_counts.query(s)
        total_laps_i_contribution = count_smaller_v * current_laps

        sum_prev_laps = ft_divs.query(s)

        count_rem_ge_cur_rem = ft_counts.query(s) - ft_counts.query(current_rem)

        current_car_overtakes = total_laps_i_contribution - sum_prev_laps - count_rem_ge_cur_rem
        total_overtakes += current_car_overtakes

        ft_counts.update(current_rem + 1, 1)
        ft_divs.update(current_rem + 1, current_laps)

    print(total_overtakes)

if __name__ == "__main__":
    solve()