# Средний элемент

Problem ID: median-out-of-three

URL: https://coderun.yandex.ru/problem/median-out-of-three/

Tags: sort

Рассмотрим три числа $a$, $b$ и $c$. Упорядочим их по возрастанию.

Какое число будет стоять между двумя другими?

Решение этой задачи на С++ могло бы выглядеть так:

```
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a[3];
    for (int i = 0; i < 3; ++i) cin >> a[i];
    sort(a, a + 3);
    cout << a[1] << endl;
    return 0;
}
```


## Формат ввода

В единственной строке записаны три целых числа $a$, $b$, $c$ ($-1000 \le a, b, c \le 1000$), числа разделены одиночными пробелами.


## Формат вывода

Выведите число, которое будет стоять между двумя другими после упорядочивания.

