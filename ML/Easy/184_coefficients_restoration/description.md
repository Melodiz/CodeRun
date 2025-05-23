# Восстановление коэффициентов

Problem ID: coefficients-restoration

URL: https://coderun.yandex.ru/problem/coefficients-restoration/

Tags: math

Необходимо восстановить коэффициенты функции $f(x)$, зная её значения на некотором наборе точек.

При этом известно, что 
$$f(x) =  ((a + \varepsilon_a)\sin x + (b + \varepsilon_b)\ln x)^2 + (c + \varepsilon_c)x^2,$$
где $\varepsilon_i$ — случайные величины, которые принимают значения из отрезка $[–0.001, 0.001]$;
$a, b, c$ — неизвестные положительные константы, которые требуется найти (абсолютная ошибка не должна превышать $10^{-2}$).


## Формат ввода

В архиве находится файл data.csv, в каждой строке которого записаны два числа $x$ и $f(x)$, разделённые запятой.


## Формат вывода

Выведите через пробел $3$ вещественных числа с точностью $2$ значащих цифры после десятичной точки, которые соответствуют набору $a, b, c$.

