# [Средний элемент](link)

## Description

Рассмотрим три числа $a$, $b$ и $c$. Упорядочим их по возрастанию.

Какое число будет стоять между двумя другими?

Решение этой задачи на С++ могло бы выглядеть так:

``` 
#include \u003ciostream\u003e
#include \u003calgorithm\u003e

using namespace std;

int main()
{
    int a[3];
    for (int i = 0; i \u003c 3; ++i) cin \u003e\u003e a[i];
    sort(a, a + 3);
    cout \u003c\u003c a[1] \u003c\u003c endl;
    return 0;
}
```
### Input Format:

В единственной строке записаны три целых числа $a$, $b$, $c$ ($-1000 \le a, b, c \le 1000$), числа разделены одиночными пробелами.


### Output Format:

Выведите число, которое будет стоять между двумя другими после упорядочивания.

## Example Test Cases

### Example 1

**Input:**
```
1 2 3

```

**Output:**
```
2

```

### Example 2

**Input:**
```
1000 -1000 0

```

**Output:**
```
0

```

### Example 3

**Input:**
```
3 1 3

```

**Output:**
```
3

```

