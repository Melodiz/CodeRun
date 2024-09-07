import shapely
from shapely.geometry import Point
import math
from joblib import Parallel, delayed
from tqdm import tqdm

def save_results(results, filename='results.txt'):
    with open(filename, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

def read_circles(filename = 'data.txt'):
    data = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            x1, y1, r1, x2, y2, r2, x3, y3, r3 = map(int, row.split())
            data.append(((x1, y1, r1), (x2, y2, r2), (x3, y3, r3)))
    return data



def create_circle(center, radius, n_vertices=100_000):
    # create a right n-polygonal approximation of a circle
    return shapely.geometry.Polygon([Point(center[0] + radius * math.cos(2 * math.pi * i / n_vertices),
                                           center[1] + radius * math.sin(2 * math.pi * i / n_vertices))
                                     for i in range(n_vertices)])

def find_intersection_area(c1, c2, c3):
    fig_c1 = create_circle((c1[0], c1[1]), c1[2])
    fig_c2 = create_circle((c2[0], c2[1]), c2[2]).intersection(fig_c1)
    fig_c3 = create_circle((c3[0], c3[1]), c3[2]).intersection(fig_c2)

    return fig_c3.area

def main():
    data = read_circles()
    results = Parallel(n_jobs=-1)(delayed(find_intersection_area)(*bach) for bach in tqdm(data, desc="Calculating intersection areas"))
    save_results(results, filename='result.txt')

if __name__ == "__main__":
    main()