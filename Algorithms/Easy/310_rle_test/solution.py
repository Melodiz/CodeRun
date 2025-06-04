# Solution for https://coderun.yandex.ru/problem/rle-test
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    s = input().strip()
    i = 0
    n = len(s)
    total = 0
    while i < n:
        if s[i].isalpha():
            j = i + 1
            num = 0
            while j < n and s[j].isdigit():
                num = num * 10 + int(s[j])
                j += 1
            if num == 0:
                num = 1
            total += num
            i = j
        else:
            i += 1
    print(total)

if __name__ == "__main__":
    main()
