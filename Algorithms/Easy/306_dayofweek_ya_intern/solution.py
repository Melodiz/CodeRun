# Solution for https://coderun.yandex.ru/problem/dayofweek-ya-intern/
def day_of_week(day, month, year):
    # Days of the week in order: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Adjust month and year for Zeller's congruence algorithm
    if month < 3:
        month += 12
        year -= 1
    
    # Calculate day of week using Zeller's congruence for Gregorian calendar
    k = year % 100
    j = year // 100
    
    h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    
    return days[h]

def solution():
    month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    with open('input.txt', 'r') as file:
        for line in file:
            day, month, year = line.strip().split()
            print(day_of_week(int(day), month_map[month], int(year)))
    return 0

if __name__ == "__main__":
    solution()
