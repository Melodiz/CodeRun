# Solution for https://coderun.yandex.ru/problem/substring-graph
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    adjacency = {}
    n = int(input())
    
    for _ in range(n):
        s = input().strip()
        current_s_substrings = []
        if len(s) >= 3:
            for j in range(len(s) - 2):
                current_s_substrings.append(s[j:j+3])
        
        if not current_s_substrings:
            continue

        for sub in current_s_substrings:
            if sub not in adjacency:
                adjacency[sub] = {}

        for j in range(len(current_s_substrings) - 1):
            u = current_s_substrings[j]
            v = current_s_substrings[j+1]
            adjacency[u][v] = adjacency[u].get(v, 0) + 1
                
    print(len(adjacency)) 
    
    edge_count = 0
    for u_node in adjacency:
        edge_count += len(adjacency[u_node])
    print(edge_count)

    for u_node, neighbors in adjacency.items():
        for v_node, weight in neighbors.items():
            print(u_node, v_node, weight)

if __name__ == "__main__":
    main()
