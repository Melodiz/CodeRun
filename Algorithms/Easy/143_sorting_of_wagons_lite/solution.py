# Solution for https://coderun.yandex.ru/problem/sorting-of-wagons-lite
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    wagons_on_path1 = list(map(int, input().split()))

    stack = []
    next_expected_wagon = 1

    for current_wagon in wagons_on_path1:
        stack.append(current_wagon)
        while stack and stack[-1] == next_expected_wagon:
            stack.pop()
            next_expected_wagon += 1
    
    # Try to empty the rest of the stack
    while stack and stack[-1] == next_expected_wagon:
        stack.pop()
        next_expected_wagon += 1

    if next_expected_wagon == n + 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
