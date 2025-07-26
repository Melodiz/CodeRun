def solution(n, a):
    result = [0] * (n + 1)
    if n == 1:
        result[0] = 1
        result[1] = a[0]
        return result
    
    dp_plus = [0] * n
    dp_minus = [0] * n
    dp_plus[0] = a[0]
    dp_minus[0] = -a[0]
    
    for i in range(1, n):
        current_plus = a[i]
        current_minus = -a[i]
        plus_ok = False
        minus_ok = False
        
        if dp_plus[i-1] <= current_plus:
            plus_ok = True
        if dp_minus[i-1] <= current_plus:
            plus_ok = True
        
        if dp_plus[i-1] <= current_minus:
            minus_ok = True
        if dp_minus[i-1] <= current_minus:
            minus_ok = True
        
        if not plus_ok and not minus_ok:
            return result
        
        if plus_ok and minus_ok:
            dp_plus[i] = current_plus
            dp_minus[i] = current_minus
        elif plus_ok:
            dp_plus[i] = current_plus
            dp_minus[i] = float('inf')
        else:
            dp_plus[i] = float('inf')
            dp_minus[i] = current_minus
    
    result[0] = 1
    current = float('inf')
    for i in range(n-1, -1, -1):
        if i == n-1:
            if dp_plus[i] != float('inf'):
                result[i+1] = dp_plus[i]
                current = dp_plus[i]
            else:
                result[i+1] = dp_minus[i]
                current = dp_minus[i]
        else:
            if dp_plus[i] <= current:
                result[i+1] = dp_plus[i]
                current = dp_plus[i]
            else:
                result[i+1] = dp_minus[i]
                current = dp_minus[i]
    
    return result