import sys

sys.setrecursionlimit(2 * 10**5 + 50)

def calculate_answer(n: int, a: list[int]):
    adj = [x - 1 for x in a]
    
    rev_adj = [[] for _ in range(n)]
    for i, target in enumerate(adj):
        if target != -2:
            rev_adj[target].append(i)

    state = [0] * n
    ans = [0] * n

    for i in range(n):
        if state[i] == 2:
            continue

        path = []
        curr = i
        while curr != -2 and state[curr] == 0:
            state[curr] = 1  # Mark as on the current path stack.
            path.append(curr)
            curr = adj[curr]

        is_cycle = False
        cycle_nodes = set()
        if curr != -2 and state[curr] == 1:
            is_cycle = True
            try:
                idx = path.index(curr)
                cycle_nodes = set(path[idx:])
            except ValueError:
                pass

        q = path[:]
        component_nodes = set(path)
        head = 0
        visited_in_comp = set(path)
        while head < len(q):
            u = q[head]
            head += 1
            for v_pred in rev_adj[u]:
                if v_pred not in visited_in_comp:
                    visited_in_comp.add(v_pred)
                    component_nodes.add(v_pred)
                    q.append(v_pred)
        
        for node in component_nodes:
            state[node] = 2

        if is_cycle:
            comp_size = len(component_nodes)
            memo = {}
            def get_tree_sz(u):
                if u in memo: return memo[u]
                if u in cycle_nodes: return 0
                
                size = 1
                for v_pred in rev_adj[u]:
                    size += get_tree_sz(v_pred)
                memo[u] = size
                return size

            for node in component_nodes:
                if node in cycle_nodes:
                    ans[node] = comp_size
                else:
                    ans[node] = get_tree_sz(node)
        else:  # DAG component
            memo = {}
            def get_dag_sz(u):
                if u in memo: return memo[u]
                
                size = 1
                for v_pred in rev_adj[u]:
                    if v_pred in component_nodes:
                        size += get_dag_sz(v_pred)
                memo[u] = size
                return size

            for node in component_nodes:
                get_dag_sz(node)
            
            for node in component_nodes:
                ans[node] = memo.get(node, 0)

    print(*ans)


class FastInput:
    """Helper class for faster input reading."""
    def __init__(self):
        self.stdin = sys.stdin

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_int(self):
        return int(self.read_line())

    def read_ints(self):
        return map(int, self.read_line().split())


def solution():
    fast_input = FastInput()
    try:
        t = fast_input.read_int()
        for _ in range(t):
            n = fast_input.read_int()
            a = list(fast_input.read_ints())
            calculate_answer(n, a)
    except (IOError, ValueError):
        pass

solution()