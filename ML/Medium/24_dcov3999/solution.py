def read_data():
    meetings = {}
    n = int(input())
    infeted = set()
    psr_result = list(map(int, input().split()))
    for i in range(n):
        if psr_result[i]:
            infeted.add(i)
    for i in range(n):
        line = list(map(int, input().split()))
        for meet in line[1:]:
            if meet not in meetings:
                meetings[meet] = set()
            meetings[meet].add(i)
    return n, infeted, meetings

def main():
    n, infected, meetings = read_data()
    for meet in sorted(meetings.keys()):
        if infected.intersection(meetings[meet]): 
            infected.update(meetings[meet])
    for i in range(n):
        print(1 if i in infected else 0, end=' ')

if __name__ == "__main__":
    main()
