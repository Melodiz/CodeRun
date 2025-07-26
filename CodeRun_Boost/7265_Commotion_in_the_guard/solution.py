# Solution for https://coderun.yandex.ru/seasons/2025-summer/tracks/common/problem/commotion-in-the-guard/
# Other solutions: https://github.com/Melodiz/CodeRun

def solution(n, m, swap_values):
    
    positions = list(range(1, 2 * n + 1))

    methods_on_left_count = n

    results = []

    for i in range(m):
        p1_orig = swap_values[2 * i]
        p2_orig = swap_values[2 * i + 1]

        p1_idx = p1_orig - 1
        p2_idx = p2_orig - 1

        p1_is_left = (p1_idx < n)
        p2_is_left = (p2_idx < n)

        if p1_is_left != p2_is_left:
            guard1 = positions[p1_idx]
            guard2 = positions[p2_idx]
            
            guard1_is_method = (guard1 <= n)
            guard2_is_method = (guard2 <= n)

            if p1_is_left:
                if guard1_is_method:
                    methods_on_left_count -= 1  
                if guard2_is_method:
                    methods_on_left_count += 1
            else: # p2_is_left must be true
                if guard2_is_method:
                    methods_on_left_count -= 1
                if guard1_is_method:
                    methods_on_left_count += 1

        positions[p1_idx], positions[p2_idx] = positions[p2_idx], positions[p1_idx]

        results.append(methods_on_left_count)

    # print(*results)
    return results

