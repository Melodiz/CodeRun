def maximum_area_histogram(heights):
    stack = []
    max_area = 0
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] >= height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    return max_area

if __name__ == "__main__":
    print(maximum_area_histogram(list(map(int, input().split()))[1:]))