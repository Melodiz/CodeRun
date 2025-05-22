# Solution for https://coderun.yandex.ru/problem/1984/

def solution():
    n, m = map(int, input().split())
    stop_words = set([input().lower().strip() for _ in range(n)])
    queries = [input().lower() for _ in range(m)]
    for query in queries:
        if any(stop in query for stop in stop_words):
            print("DELETE")
        else:
            print("KEEP")

if __name__ == "__main__":
    solution()
