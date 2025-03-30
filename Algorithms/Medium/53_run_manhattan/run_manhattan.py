def solve(time_limit, distance_limit, navigator_data):
    def expand_rectangle(rect, expansion):
        max_sum, min_diff, min_sum, max_diff = rect
        return [max_sum + expansion, min_diff + expansion, min_sum - expansion, max_diff - expansion]

    def intersect_rectangles(rect1, rect2):
        max_sum1, min_diff1, min_sum1, max_diff1 = rect1
        max_sum2, min_diff2, min_sum2, max_diff2 = rect2
        return [min(max_sum1, max_sum2), min(min_diff1, min_diff2),
                max(min_sum1, min_sum2), max(max_diff1, max_diff2)]

    current_rect = [0, 0, 0, 0]

    for x, y in navigator_data:
        current_rect = expand_rectangle(rect=current_rect, expansion=time_limit)
        new_rect = expand_rectangle([x + y, x - y, x + y, x - y], distance_limit)
        current_rect = intersect_rectangles(current_rect, new_rect)

    max_sum, min_diff, min_sum, max_diff = current_rect

    possible_positions = set()

    sum_range_start, sum_range_end = min(min_sum, max_sum), max(min_sum, max_sum)
    diff_range_start, diff_range_end = min(min_diff, max_diff), max(min_diff, max_diff)
    
    for sum_xy in range(sum_range_start, sum_range_end + 1):
        for diff_xy in range(diff_range_start, diff_range_end + 1):
            x = sum_xy + diff_xy
            if x % 2 == 0:
                y = sum_xy - x // 2
                possible_positions.add((x // 2, y))

    return possible_positions


def main():
    time_limit, distance_limit, num_points = map(int, input().split())
    navigator_data = [tuple(map(int, input().split())) for _ in range(num_points)]
    final_positions = solve(time_limit, distance_limit, navigator_data)
    print(len(final_positions))
    for position in sorted(final_positions):
        print(*position)


if __name__ == "__main__":
    main()