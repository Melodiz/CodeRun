# Solution for https://coderun.yandex.ru/problem/rocks-and-jewels
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    jewels = set(input())
    stones = input()
    count = 0
    for char in stones:
        if char in jewels:
            count += 1
    print(count)
if __name__ == "__main__":
    main()
