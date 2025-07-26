import sys
from collections import deque

sys.setrecursionlimit(200000)

def _compare_paths(u_idx: int, v_idx: int, dp: list[tuple], memo: dict) -> int:
    if u_idx == v_idx:
        return 0

    if u_idx > v_idx:
        sign = -1
        u_idx, v_idx = v_idx, u_idx
    else:
        sign = 1

    if (u_idx, v_idx) in memo:
        return memo[(u_idx, v_idx)] * sign

    _u_jumps, u_parent, u_jump = dp[u_idx]
    _v_jumps, v_parent, v_jump = dp[v_idx]

    if u_parent == -1 and v_parent == -1:
        res = (u_jump > v_jump) - (u_jump < v_jump)
        memo[(u_idx, v_idx)] = res
        return res * sign

    res = _compare_paths(u_parent, v_parent, dp, memo)
    
    if res == 0:
        res = (u_jump > v_jump) - (u_jump < v_jump)
    
    memo[(u_idx, v_idx)] = res
    return res * sign

def solve(n: int, k: int, a: list[int]) -> list[int]:
    all_coords = sorted(list(set([0] + a + [n])))
    coord_to_idx = {coord: i for i, coord in enumerate(all_coords)}
    
    INF_JUMPS = float('inf')
    dp = [(INF_JUMPS, -1, 0) for _ in range(len(all_coords))]
    
    if 0 in coord_to_idx:
        dp[coord_to_idx[0]] = (0, -1, 0)

    comparison_memo = {}

    for i, curr_coord in enumerate(all_coords):
        curr_jumps, _parent, _jump = dp[i]

        if curr_jumps == INF_JUMPS:
            continue
            
        for jump in [1, 2]:
            next_coord = curr_coord + jump
            if next_coord in coord_to_idx:
                next_idx = coord_to_idx[next_coord]
                
                new_jumps = curr_jumps + 1
                
                old_jumps, old_parent_idx, old_jump = dp[next_idx]

                if new_jumps < old_jumps:
                    dp[next_idx] = (new_jumps, i, jump)
                elif new_jumps == old_jumps:
                    comparison_result = _compare_paths(i, old_parent_idx, dp, comparison_memo)
                    
                    if comparison_result < 0:
                        dp[next_idx] = (new_jumps, i, jump)
                    elif comparison_result == 0 and jump < old_jump:
                        dp[next_idx] = (new_jumps, i, jump)

    n_idx = coord_to_idx[n]
    min_jumps, parent_idx, last_jump = dp[n_idx]
    
    if min_jumps == INF_JUMPS:
        return [-1]
    
    path = deque()
    curr_idx = n_idx
    while parent_idx != -1:
        _jumps, p_idx, jump_val = dp[curr_idx]
        path.appendleft(jump_val)
        curr_idx = p_idx
        parent_idx = dp[curr_idx][1]
        
    return [min_jumps] + list(path)

