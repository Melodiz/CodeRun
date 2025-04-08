import json

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
    date_maxes = {}
    
    for item in data:
        date, value = item['date'], item['count']
        date_maxes[date] = max(date_maxes.get(date, float('-inf')), value)
    
    if date_maxes:
        min_value = min(date_maxes.values())
        result = sorted([date for date, value in date_maxes.items() if value == min_value])
        print(*result, sep='\n')

if __name__ == "__main__":
    main()