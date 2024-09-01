import sys
import math

def countInnerPoints(points):
    # input format : x1 y1 x2 y2... xN yN
    # return the number of points in the first half of the unit circle
    count = 0
    for i in range(0, len(points), 2):
        x = points[i]
        y = points[i+1]
        if math.sqrt(x**2 + y**2) <= math.sqrt(0.5):
            count += 1
    return count

def solution(data):
    for points in data:
        if countInnerPoints(points) > 600:
            print(1)
        else:
            print(2)
    return

def main():
    data = [list(map(float, input().split())) for _ in range(100)]
    solution(data)

if __name__ == '__main__':
    main()