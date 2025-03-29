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

def write_add_to_file(counter, n_samples, filename='ML/Medium/553_points-in-cube/result.txt'):
    with open(filename, 'a') as file:
        file.write(f"{counter} {n_samples}\n")

def main():
    treshold_square = 0.5625 
    n_samples = 10**6
    counter = 2580547
    samples_counter = 208000000
    for _ in tqdm(range(1_000), desc="Generating random points"):
        samples_counter += n_samples
        for _ in range(n_samples):
            point = generate_random_point_in_UnitCube()
            if checkIfPointFarEnoughFromVertices(point, treshold_square):
                counter += 1
        write_add_to_file(counter, samples_counter)
    print(f"Total points: {counter}")
    print(f"Total samples: {samples_counter}")
    print(f"Probability: {counter / samples_counter:.6f}")
    return counter / samples_counter

if __name__ == "__main__":
    main()