# Solution for https://coderun.yandex.ru/problem/calendar-formatting/

def solution():
    days, start_day = input().split()
    days = int(days)
    start_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                 'Friday', 'Saturday', 'Sunday'].index(start_day)
    # fill first week
    for i in range(7):
        if start_day > i:
            print('..', end=' ')
        else:
            print('.' + str(i-start_day+1), end=' ')
    print()
    for i in range(7-start_day+1, days+1):
        if (i + start_day) % 7 == 0 :
            if i < 10: print('.'+str(i))
            else: print(str(i))
        else:
            if i < 10: print('.'+str(i), end=' ')
            else: print(str(i), end=' ')


if __name__ == "__main__":
    solution()
