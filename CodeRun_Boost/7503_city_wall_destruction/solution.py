def solve(n: int, a: list[int]) -> int:
    left_smaller, left_greater = [-1] * n, [-1] * n
    right_smaller, right_greater = [n] * n, [n] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            stack.pop()
        left_smaller[i] = stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] > a[i]:
            stack.pop()
        right_smaller[i] = stack[-1] if stack else n
        stack.append(i)
    stack.clear()
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        left_greater[i] = stack[-1] if stack else -1
        stack.append(i)
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        right_greater[i] = stack[-1] if stack else n
        stack.append(i)
    result = 0
    for i in range(n):
        max_count = (i - left_greater[i]) * (right_greater[i] - i)
        min_count = (i - left_smaller[i]) * (right_smaller[i] - i)
        result += a[i] * (max_count - min_count)
    return result
