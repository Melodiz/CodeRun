# [Симметричная последовательность](link)

## Description

Последовательность чисел назовём симметричной, если она одинаково читается как слева направо, так и справа налево. Например, следующие последовательности являются симметричными:

1 2 3 4 5 4 3 2 1 

1 2 1 2 2 1 2 1

Вашей программе будет дана последовательность чисел. Требуется определить, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.
### Input Format:

Сначала вводится число $N$ — количество элементов исходной последовательности (1 $\le$ $N$ $\le$ 100). Далее идут $N$ чисел — элементы этой последовательности,  натуральные числа от 1 до 9.

### Output Format:

Выведите сначала число $M$ — минимальное количество элементов, которое надо дописать к последовательности, а потом $M$ чисел (каждое — от 1 до 9) — числа, которые надо дописать к последовательности.

## Example Test Cases

### Example 1

**Input:**
```
9
1 2 3 4 5 4 3 2 1

```

**Output:**
```
0

```

### Example 2

**Input:**
```
5
1 2 1 2 2

```

**Output:**
```
3
1 2 1

```

### Example 3

**Input:**
```
5
1 2 3 4 5

```

**Output:**
```
4
4 3 2 1

```

