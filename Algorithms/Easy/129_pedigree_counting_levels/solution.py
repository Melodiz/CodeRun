# Solution for https://coderun.yandex.ru/problem/pedigree-counting-levels/

def get_height(person, parent_map, heights):
    if person in heights:
        return heights[person]
    
    if person not in parent_map:
        heights[person] = 0
        return 0
    
    parent = parent_map[person]
    heights[person] = 1 + get_height(parent, parent_map, heights)
    return heights[person]

def main():
    n = int(input())
    
    parent_map = {}
    all_people = set()
    
    for _ in range(n-1):
        child, parent = input().split()
        parent_map[child] = parent
        all_people.add(child)
        all_people.add(parent)
    
    heights = {}
    for person in all_people:
        if person not in heights:
            get_height(person, parent_map, heights)
    
    for person in sorted(all_people):
        print(person, heights[person])

if __name__ == "__main__":
    main()