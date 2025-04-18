# Уникальные запросы

Problem ID: unique-queries

URL: https://coderun.yandex.ru/problem/unique-queries/

Tags: standard library, data structures

Пользователи задают в Яндекс Поиске десятки тысяч запросов в секунду. Часть запросов
задают сотни раз в час, другая часть запросов повторяется несколько раз в день,
третью часть запросов пользователи спрашивают у Яндекса впервые.

Необходимо оценить количество уникальных запросов, при условии наличия 500 KB оперативной памяти.
Гарантируется, что правильный ответ не превосходит $100000$ и не меньше, чем $50000$.

Решение засчитывается, если ответ отличается от правильного не более, чем на $5\%$.


## Формат ввода

В первой строке указано число $n \le 500000$ — количество запросов, среди которых нужно
найти число уникальных. В каждой из $n$ последующих строк содержится по одному
запросу. Длина каждого запроса не превосходит $1000$ символов.


## Формат вывода

Необходимо вывести одно число — оценку количества уникальных запросов. Оценка не обязана быть целой.


## Примечание

Этот пример лишь иллюстрирует формат входных данных. Он намеренно нарушает обещание, что ответ не меньше, чем $50000$.

