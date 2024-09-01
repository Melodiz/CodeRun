import numpy as np
import sys


def countInnerPoints(points):
    # input format : x1 y1 x2 y2... x999 y999
    # return the number of points in the first half of the unit circle
    count = 0
    for i in range(0, len(points), 2):
        x = points[i]
        y = points[i+1]
        if np.linalg.norm([x, y]) <= np.sqrt(0.5):
            count += 1
    return count


def soluton(data, answers):
    countTrue = 0
    for i in range(len(data)):
        points = data[i]
        if countInnerPoints(points) > 600 and answers[i] == 1:
            countTrue += 1
        elif countInnerPoints(points) <= 600 and answers[i] == 2:
            countTrue += 1
    print(countTrue/len(data))

def main():
    inputPath = 'input.txt'
    answersPath = 'answers.txt'
    with open(inputPath, 'r') as f_input, open(answersPath, 'r') as f_answers:
        data = []
        for line in f_input:
            points = list(map(float, line.strip().split()))
            data.append(points)
        answers = list(map(int, f_answers))
        assert len(data) == len(answers)
        soluton(data, answers)

if __name__ == '__main__':
    main()