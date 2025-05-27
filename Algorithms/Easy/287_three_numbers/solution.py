# Solution for https://coderun.yandex.ru/problem/three-numbers/
def process_query(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                digit_presence = [False]*10
                for num in [numbers[i], numbers[j], numbers[k]]:
                    for char in num:
                        digit_presence[int(char)] = True
                    if all(presence for presence in digit_presence):
                        return ' '.join([numbers[i], numbers[j], numbers[k]])
    return 'Not a proper case'
def main():
    t = int(input())
    for _ in range(t):
        _ = input()
        numbers = input().split()
        print(process_query(numbers))
    return 0

if __name__ == "__main__":
    main()
