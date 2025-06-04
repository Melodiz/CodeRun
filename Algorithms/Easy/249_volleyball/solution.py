import math

def combinations(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def ways_for_set_score(s1, s2, is_fifth_set):
    # Determine the normal points to win the set
    P_norm = 15 if is_fifth_set else 25
    
    winner_score = max(s1, s2)
    loser_score = min(s1, s2)

    if winner_score == P_norm and loser_score < (P_norm - 1):
        return combinations(P_norm - 1 + loser_score, loser_score)
    
    elif winner_score > (P_norm - 1) and loser_score == winner_score - 2:
        base_deuce_score = P_norm - 1 # e.g., 24 or 14
        
        ways_to_reach_base_deuce = combinations(2 * base_deuce_score, base_deuce_score)
        
        num_intermediate_deuces_after_base = loser_score - base_deuce_score
        
        factor_for_deuces = 1
        if num_intermediate_deuces_after_base > 0:
            factor_for_deuces = 2**num_intermediate_deuces_after_base
            
        return ways_to_reach_base_deuce * factor_for_deuces
    
    else:
        return 0

# Read input line
line_parts = input().split()
N = int(line_parts[0])
set_scores_str_list = line_parts[1:]

grand_total_ways = 1

for i in range(N):
    s1_str, s2_str = set_scores_str_list[i].split(':')
    s1_val = int(s1_str)
    s2_val = int(s2_str)
    
    is_fifth_set_rules = False
    if N == 5 and i == 4:
        is_fifth_set_rules = True
        
    ways_for_this_set = ways_for_set_score(s1_val, s2_val, is_fifth_set_rules)
    
    grand_total_ways *= ways_for_this_set

print(grand_total_ways)