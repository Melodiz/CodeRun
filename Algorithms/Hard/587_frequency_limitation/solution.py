# Solution for https://coderun.yandex.ru/problem/frequency-limitation
# Other solutions: https://github.com/Melodiz/CodeRun

def solve_for_Y(Y, queries):
    last_query_time = -float('inf')
    responses_time = []
    for query_time in queries:
        if query_time - last_query_time >= Y:
            responses_time.append(query_time)
            last_query_time = query_time
        else:
            responses_time.append(last_query_time + Y)
            last_query_time += Y
    return responses_time

def solve_for_X(X, queries):
    delay = 10**9 # 1 second in nanoseconds
    executed_queries = [float('-inf')] * X
    responses_time = []
    for i, query_time in enumerate(queries):
        # check if we can execute the query right now:
        if query_time - executed_queries[-X] >= delay:
            executed_queries.append(query_time)
            responses_time.append(query_time)
        else:
            # we need to execute the query in such time, when no more than X queries were executed in the last second
            new_exec_time = delay + executed_queries[-X]
            executed_queries.append(new_exec_time)
            responses_time.append(new_exec_time)
    return responses_time
        


def main():
    X, Y = map(int, input().split('/'))
    N = int(input())
    queries = list(map(int, input().split()))
    if X == 1: 
        print(*solve_for_Y(Y*10**9, queries))
    else:
        print(*solve_for_X(X, queries))

if __name__ == "__main__":
    main()
