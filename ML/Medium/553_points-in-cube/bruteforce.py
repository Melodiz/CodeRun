from random import uniform
from tqdm import tqdm
import math

def generate_random_point_in_UnitCube():
    x = uniform(0, 1)
    y = uniform(0, 1)
    z = uniform(0, 1)
    return (x, y, z)

def euclidean_distance_squared(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2

def checkIfPointFarEnoughFromVertices(point, treshold_square):
    vertices = [
        (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)
    ]
    for vertex in vertices:
        if euclidean_distance_squared(point, vertex) <= treshold_square:
            return False
    return True

def main():
    treshold_square = 0.5625 
    n_samples = int(1e8)
    counter = 0
    for _ in tqdm(range(n_samples), desc='Progress'):
        point = generate_random_point_in_UnitCube()
        if checkIfPointFarEnoughFromVertices(point, treshold_square): 
            counter += 1
    result = counter / n_samples
    print(round(result, 6))

if __name__ == "__main__":
    main()