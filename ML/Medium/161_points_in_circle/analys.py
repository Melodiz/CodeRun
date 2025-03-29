import plotly.express as px
import numpy as np
from random import uniform
from math import cos, sin, pi
import pandas as pd


def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return (a * cos(2 * pi * b), a * sin(2 * pi * b))

def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return (x, y)

# generate points from both functions and make a scatter plot
data1 = [generate1() for _ in range(1000)]
data2 = [generate2() for _ in range(1000)]
filepath = 'data.csv'

df1 = pd.DataFrame(data1, columns=['x', 'y'])
df2 = pd.DataFrame(data2, columns=['x', 'y'])

fig1 = px.scatter(df1, x='x', y='y', title='generated points from function 1',
                  height=1000, width=1000)
fig2 = px.scatter(df2, x='x', y='y', title='generated points from function 2',
                  height= 1000, width= 1000)

fig1.show()
fig2.show()