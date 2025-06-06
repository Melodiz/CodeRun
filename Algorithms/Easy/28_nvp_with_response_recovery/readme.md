# [28. НВП с восстановлением ответа](https://coderun.yandex.ru/problem/nvp-with-response-recovery)

## Description

Дана последовательность, требуется найти её наибольшую возрастающую подпоследовательность.

Напомним:

Последовательность x называется подпоследовательностью последовательности y, если x получается из y удалением нескольких (возможно, нуля или всех) элементов.

Наибольшая возрастающая подпоследовательность - строго возрастающая подпоследовательность наибольшей длины.

### Input Format:

В первой строке входных данных задано число N — длина последовательности (1 $\le$ N $\le$ 1000). Во второй строке задается сама последовательность (разделитель — пробел). Элементы последовательности — целые числа, не превосходящие 10000 по модулю.

### Output Format:

Требуется вывести наибольшую возрастающую подпоследовательность данной последовательности. Если таких подпоследовательностей несколько, необходимо вывести одну (любую) из них.



## Example Test Cases

### Example 1

**Input:**
```
6
3 29 5 5 28 6

```

**Output:**
```
3 5 28

```

### Example 2

**Input:**
```
10
4 8 2 6 2 10 6 29 58 9

```

**Output:**
```
4 8 10 29 58 

```

**Tags**: dynamic programming 1D

