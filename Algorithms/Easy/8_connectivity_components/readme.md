# [Компоненты связности](link)

## Description

Дан неориентированный невзвешенный граф, состоящий из $N$ вершин и $M$ ребер. Необходимо посчитать количество его компонент связности и вывести их.

Напомним:

**Компонента связности в неориентированном графе** - это подмножество вершин, таких что все вершины достижимы друг из друга.
### Input Format:

Во входном файле записано два числа N и M (0 $\lt$ N $\le$ 100000, 0 $\le$ M $\le$ 100000). В следующих M строках записаны по два числа i и j (1 $\le$ i, j $\le$ N), которые означают, что вершины i и j соединены ребром.

### Output Format:

В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.

## Example Test Cases

### Example 1

**Input:**
```
6 4
3 1
1 2
5 4
2 3

```

**Output:**
```
3
3
1 2 3 
2
4 5 
1
6 

```

### Example 2

**Input:**
```
6 4
4 2
1 4
6 4
3 6

```

**Output:**
```
2
5
1 2 3 4 6 
1
5 

```

