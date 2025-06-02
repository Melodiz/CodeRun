# Solution for https://coderun.yandex.ru/problem/combo
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    a = list(map(int, input().split()))
    X = int(input())
    b_raw = list(map(int, input().split()))
    b = [item - 1 for item in b_raw]

    k = int(input())
    c_raw = list(map(int, input().split()))
    c = [item - 1 for item in c_raw]

    desired_item_counts = [0] * n
    for item_idx in c:
        desired_item_counts[item_idx] += 1

    min_total_cost = float('inf')

    for num_combos in range(k + 2):
        current_combo_cost = num_combos * X
        temp_needed_counts = list(desired_item_counts)

        for combo_item_idx in b:
            temp_needed_counts[combo_item_idx] = max(0, temp_needed_counts[combo_item_idx] - num_combos)

        remaining_cost = 0
        for i in range(n):
            remaining_cost += temp_needed_counts[i] * a[i]

        min_total_cost = min(min_total_cost, current_combo_cost + remaining_cost)

    print(min_total_cost)

if __name__ == "__main__":
    main()