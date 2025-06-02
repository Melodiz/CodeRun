# Solution for https://coderun.yandex.ru/problem/6-out-of-36-squared
# Other solutions: https://github.com/Melodiz/CodeRun

import math
import itertools

def read_data():
    data = []
    with open("data.txt", "r") as file:
        for line in file:
            pairs = []
            nums = list(map(float, line.split()))
            for i in range(0, len(nums), 2):
                pairs.append((nums[i], nums[i + 1]))
            data.append(pairs)
    return data

def calculate_min_radius(p1, p2, p3, p4, p5, p6):
    # p_i is (x_i, y_i), calculate the minimum side of the square that can contain all 4 points
    points = [p1, p2, p3, p4, p5, p6]
    
    # Find the bounding box of all points
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # The minimum square side length is the maximum of width and height of the bounding box
    width = max_x - min_x
    height = max_y - min_y
    
    return max(width, height)/2.0

def solve_one_dataset(case):
    # Read the line of 72 numbers for one dataset
    points = case
        
    min_overall_radius = float('inf')
    for point_subset in itertools.combinations(points, 6):
        min_radius = calculate_min_radius(*point_subset)
        if min_radius < min_overall_radius:
            min_overall_radius = min_radius
    print(f"{min_overall_radius:.10f}")

if __name__ == "__main__":
    data = read_data()
    for case in data:
        solve_one_dataset(case)
