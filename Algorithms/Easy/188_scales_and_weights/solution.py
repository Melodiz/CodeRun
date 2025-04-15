# Solution for https://coderun.yandex.ru/problem/scales-and-weights/

def solution():
    n = int(input())
    weights = list(map(int, input().split()))
    
    possible_weights = {0}
    
    for weight in weights:
        new_weights = set()
        for w in possible_weights:
            new_weights.add(w + weight)
            if w >= weight:
                new_weights.add(w - weight)
            else:
                new_weights.add(weight - w)
        possible_weights.update(new_weights)
    
    for i in range(1, n + 1):
        if i not in possible_weights:
            print("No")
            return
    
    print("Yes")

if __name__ == "__main__":
    solution()