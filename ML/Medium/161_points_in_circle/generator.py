import random
import math
import numpy as np

def generate1():
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))

def generate2():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            return (x, y)

def generate_points():
    points = []
    algorithm = random.choice([1, 2])
    for _ in range(1000):
        if algorithm == 1:
            points.append(generate1())
        else:
            points.append(generate2())
    return points, algorithm

def main():
    with open('input.txt', 'w') as f_input, open('answers.txt', 'w') as f_answers:
        for _ in range(100):
            points, algorithm = generate_points()
            line = ' '.join(f'{x} {y}' for x, y in points)
            f_input.write(line + '\n')
            f_answers.write(f'{algorithm}\n')

if __name__ == '__main__':
    main()