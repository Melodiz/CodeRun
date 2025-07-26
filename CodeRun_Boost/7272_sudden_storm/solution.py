def solution(n, t, a, b):
    total_initial = sum(a)
    
    if t == 0:
        return [total_initial]
        
    base_diff = [0] * (t + 3)
    adj = [0] * (t + 3)
    
    for i in range(n):
        a_i = a[i]
        b_i = b[i]
        if b_i == 0 or a_i == 0:
            continue
            
        k_i = (a_i + b_i - 1) // b_i
        end = min(k_i, t)
        base_diff[1] += b_i
        if end + 1 < len(base_diff):
            base_diff[end + 1] -= b_i
            
        if k_i <= t:
            remainder = a_i - b_i * (k_i - 1)
            adj[k_i] += (remainder - b_i)
            
    res = [0] * (t + 1)
    res[0] = total_initial
    current_base = 0
    cumulative_loss = 0
    
    for j in range(1, t + 1):
        current_base += base_diff[j]
        loss_this_minute = current_base + adj[j]
        cumulative_loss += loss_this_minute
        res[j] = total_initial - cumulative_loss
        
    return res