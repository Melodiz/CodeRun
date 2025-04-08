# Solution for https://coderun.yandex.ru/problem/splitting-into-terms/

def generate_partitions(n):
    partitions = []
    
    def generate(remaining, partition, max_val):
        if remaining == 0:
            partitions.append(partition[:])
            return
        
        for i in range(min(max_val, remaining), 0, -1):
            generate(remaining - i, partition + [i], i)
    
    generate(n, [], n)
    
    return sorted(partitions, key=lambda x: [-i for i in x])[::-1]

def solution():
    n = int(input())
    partitions = generate_partitions(n)
    
    for partition in partitions:
        print(" + ".join(map(str, partition)))

if __name__ == "__main__":
    solution()