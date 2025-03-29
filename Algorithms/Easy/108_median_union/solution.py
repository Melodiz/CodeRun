def union_of_two_sorted_arrays(arr1, arr2):
    n = len(arr1)
    i, j = 0, 0
    last_element = -1
    while (i+j) < n:
        if arr1[i] < arr2[j]:
            last_element = arr1[i]
            i += 1
        else:
            last_element = arr2[j]
            j += 1
    return last_element


def main():
    k, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]
    for i in range(k):
        for j in range(i+1, k):
            print(union_of_two_sorted_arrays(data[i], data[j]))


if __name__ == "__main__":
    main()
