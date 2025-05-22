# Solution for https://coderun.yandex.ru/problem/fuzzies/

def solution():
    n, t = map(int, input().split())
    tasks = list(map(int, input().split()))
    tasks.sort()
    for i in range(len(tasks)):
        if t - tasks[i] >= 0:
            t -= tasks[i]
        else:
            return i
    return len(tasks)

if __name__ == "__main__":
    print(solution())
