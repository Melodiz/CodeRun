# Гистограмма и прямоугольник

Problem ID: histogram-and-rectangle

URL: https://coderun.yandex.ru/problem/histogram-and-rectangle/

Tags: linear search, stack

Гистограмма является многоугольником, сформированным из последовательности прямоугольников, выровненных на общей базовой линии. Прямоугольники имеют равную ширину, но могут иметь различные высоты. Например, фигура слева показывает гистограмму, которая состоит из прямоугольников с высотами 2, 1, 4, 5, 1, 3, 3. Все прямоугольники на этом рисунке имеют ширину, равную 1.



Обычно гистограммы используются для представления дискретных распределений, например, частоты символов в текстах. Отметьте, что порядок прямоугольников очень важен. Вычислите область самого большого прямоугольника в гистограмме, который также находится на общей базовой линии. На рисунке справа заштрихованная фигура является самым большим выровненным прямоугольником на изображенной гистограмме.


## Формат ввода

В первой строке входного файла записано число $N$ ($0 \lt N \le 10^6$) — количество прямоугольников гистограммы. Далее в той же строке записано $N$ целых чисел $h_1, ..., h_n$, где $0 \le h_i \le 10^9$. Эти числа обозначают высоты прямоугольников гистограммы слева направо. Ширина каждого прямоугольника равна 1


## Формат вывода

Выведите площадь самого большого прямоугольника в гистограмме. Помните, что этот прямоугольник должен быть на общей базовой линии.

