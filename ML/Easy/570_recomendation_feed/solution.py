# Solution for https://coderun.yandex.ru/problem/recomendation-feed/

def solution():
    p, n, k = map(int, input().split())
    themes = [input() for _ in range(p)]
    ids = list(map(int, input().split()))
    ans = []
    themes_cnt = {}
    cnt_total = 0
    for i, theme in enumerate(themes):
        if themes_cnt.get(theme, 0) == k:
            continue
        themes_cnt[theme] = themes_cnt.get(theme, 0) + 1
        ans.append(f'{theme} #{ids[i]}')
        cnt_total += 1
        if cnt_total == n:
            break
    print('\n'.join(ans))


if __name__ == "__main__":
    solution()
