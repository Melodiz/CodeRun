# [Весы и гири](link)

## Description

Есть чашечные весы и набор гирь. Будем говорить, что с помощью набора гирь возможно взвесить массу $m$, если можно поставить гири на весы так (не обязательно все), чтобы разница в весе чаш равнялась $m$.  

Задается число $n$. Можно с помощью предложенного набора гирь взвесить все целые величины масс от $1$ до $n$?

Например: пусть набор $[1, 3, 4]$ и $n=5$. То разница весов $1$, $3$ и $4$ достигается соответствующими гирями, $2$ можно получить как $3$ на одной чаше и $1$ на другой, а $5$ как $4+1$.
### Input Format:

В первой строке вводится число $n$ ($1 \le n \le 10^8$).

Во второй строке вводится набор чисел $w_i$ через пробел ($1 \le w_i \le 10^8$). 
Количество чисел в наборе не превосходит 13.

### Output Format:

Вывести ```Yes```, если можно взвесить любую массу от $1$ до $n$, иначе выведите ```No```.


## Example Test Cases

### Example 1

**Input:**
```
5
1 3 4

```

**Output:**
```
Yes

```

### Example 2

**Input:**
```
9
1 3 4

```

**Output:**
```
No

```

### Example 3

**Input:**
```
94
34 7 4 25 30 27 39

```

**Output:**
```
Yes

```

