# Solution for https://coderun.yandex.ru/problem/couple-of-letters/

def solution():
    s = input()
    cnt = {}
    for i in range(len(s)-1):
        if not ' ' in s[i:i+2]:
            cnt[s[i:i+2]] = cnt.get(s[i:i+2], 0) + 1
    print(sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0])

if __name__ == "__main__":
    solution()
