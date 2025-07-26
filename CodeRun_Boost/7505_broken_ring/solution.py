import sys

class FastInput:
    def __init__(self):
        self.stdin = sys.stdin

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_tokens(self):
        return self.read_line().split()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_tokens())


# ввод/вывод
# не изменяйте сигнатуру метода
def solution():
    input_reader = FastInput()
    num_test_cases = input_reader.read_int()

    results = []
    for _ in range(num_test_cases):
        n = input_reader.read_int()
        a = list(input_reader.read_ints())
        b = list(input_reader.read_ints())

        adj = [0] * (n + 1) 
        costs = [0] * (n + 1) 
        
        for i in range(n):
            adj[i + 1] = a[i] 
            costs[i + 1] = b[i] 

        visited = [0] * (n + 1) 
        
        all_cycle_min_b_values = [] 

        for i in range(1, n + 1):
            if visited[i] == 0: 
                current_node = i
                path_nodes = [] 
                
                while visited[current_node] == 0:
                    visited[current_node] = 1 # Mark as visiting
                    path_nodes.append(current_node)
                    current_node = adj[current_node] # Move to next node

                if visited[current_node] == 1:  
                    cycle_start_index = path_nodes.index(current_node)
                    cycle_nodes = path_nodes[cycle_start_index:]
                    
                    min_b_for_this_cycle = float('inf')
                    for node in cycle_nodes:
                        min_b_for_this_cycle = min(min_b_for_this_cycle, costs[node])
                    
                    all_cycle_min_b_values.append(min_b_for_this_cycle)
                
                for node in path_nodes: 
                    visited[node] = 2
        

        k = len(all_cycle_min_b_values)
        if k == 1:

            total_cost = 0
        else:

            total_cost = sum(all_cycle_min_b_values)
        
        results.append(total_cost)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")