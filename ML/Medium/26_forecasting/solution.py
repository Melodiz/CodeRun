import sys
import numpy as np

def main():
    n =  int(input())
    temperatures = []
    for _ in range(n):
        temperatures.append(float(input()))
    m = int(input())
    alpha, betta = 0.9, 0.95
    for i in range(m):
        prediction = alpha*temperatures[-1] + (1-alpha)*temperatures[-2]
        prediction*= betta
        prediction += (1-betta)*temperatures[i]
        print(prediction)
        temperatures.append(prediction)

if __name__ == "__main__":
    main()