def determine_squence_type(arr):
    if len(arr) == 1:
        return "CONSTANT"

    greater = False
    less = False
    eq = False

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            eq = True
        elif arr[i] > arr[i-1]:
            greater = True
        else:
            less = True

    if not greater and not less and eq:
        return "CONSTANT"
    if greater and eq and not less:
        return "WEAKLY ASCENDING"
    if greater and not eq and not less:
        return "ASCENDING"
    if less and eq and not greater:
        return "WEAKLY DESCENDING"
    if less and not eq and not greater:
        return "DESCENDING"
    return "RANDOM"


def main():
    data = []
    while True:
        el = int(input())
        if el != -2000000000:
            data.append(el)
        else:
            break
    print(determine_squence_type(data))


if __name__ == "__main__":
    main()
