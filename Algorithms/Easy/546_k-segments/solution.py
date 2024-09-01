def min_segment_length(k, points):
    points.sort()
    left, right = 0, points[-1] - points[0]

    def can_cover_with_length(length):
        count, last_covered = 1, points[0]
        for point in points:
            if point - last_covered > length:
                count += 1
                last_covered = point
                if count > k:
                    return False
        return True

    while left < right:
        mid = (left + right) // 2
        if can_cover_with_length(mid):
            right = mid
        else:
            left = mid + 1

    return left

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_segment_length(k, arr))

if __name__ == "__main__":
    main()