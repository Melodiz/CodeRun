import sys
import random

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def calculate_answer(n: int, points: list[Point]) -> tuple[int, int]:

    def dist_sq(p1: Point, p2: Point) -> int:
        return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

    if n <= 1:
        return 0, 0
    # The problem statement guarantees n >= 2
    if n == 2:
        return 1, 2

    indices = list(range(n))
    random.shuffle(indices)

    num_attempts = min(n, 40)

    for i in range(num_attempts):
        anchor_idx = indices[i]
        anchor_point = points[anchor_idx]

        closest_dist_sq = -1
        neighbor_idx = -1

        for j in range(n):
            if j == anchor_idx:
                continue
            
            current_dist_sq = dist_sq(anchor_point, points[j])
            
            if neighbor_idx == -1 or current_dist_sq < closest_dist_sq:
                closest_dist_sq = current_dist_sq
                neighbor_idx = j

        neighbor_point = points[neighbor_idx]
        is_valid = True
        for k in range(n):
            if k == anchor_idx or k == neighbor_idx:
                continue
            
            p_k = points[k]
            if dist_sq(p_k, anchor_point) == dist_sq(p_k, neighbor_point):
                is_valid = False
                break
        
        if is_valid:
            return anchor_idx + 1, neighbor_idx + 1

    return 0, 0

# --- Provided I/O boilerplate ---
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

def solution():
    input = FastInput()
    n = input.read_int()
    coords = list(input.read_ints())
    points = [
        Point(coords[i * 2], coords[i * 2 + 1])
        for i in range(n)
    ]
    first, second = calculate_answer(n, points)
    print(first, second)