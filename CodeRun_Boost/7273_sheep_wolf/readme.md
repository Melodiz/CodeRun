# 7273. Волк в овечьей шкуре

Пока вы разбирались с непогодой, Кодерун изучал журналы доступа в замок. Что-то в логах настораживало. Среди привычных ID гостей тут и там появлялись странные повторы. «Кто-то копирует чужие идентификаторы и проникает в замок под чужими идентификаторами...» — решил кот.

Теперь Кодерун просит вашей помощи. Нужно найти самый длинный непрерывный фрагмент в логов доступа, в котором встречаются ровно два разных ID.

### Формат ввода

В качестве аргументов вашей функции передаются 2 параметра:

* Натуральное число `n (1 ≤ n ≤ 10^6)` — количество чисел в последовательности ID гостей, совершавших запросы.
* Одномерный массив натуральных чисел `a` размера `n (1 ≤ aᵢ ≤ 10^9)` — последовательность ID гостей.

### Формат вывода

В качестве ответа ваша функция должна вернуть одно число — максимальную длину подотрезка, удовлетворяющего условию.

### Ограничения

* Ограничение времени: 2 с
* Ограничение памяти: 256 МБ

### Пример 1

Ввод:
```

6
3 3 1 2 2 1

```

Вывод:
```

4

```

### Пример 2

Ввод:
```

2
1 1

```

Вывод:
```

0

```

---

# 7273. Wolf in Sheep's Clothing

While you were dealing with the bad weather, Coderun was examining the access logs for the castle. Something in the logs was alarming. Among the usual guest IDs, strange repetitions appeared here and there. "Someone is copying other people's identifiers and entering the castle with fake IDs..." – decided the cat.

Now Coderun asks for your help. You need to find the longest continuous fragment in the access logs that contains exactly two distinct IDs.

### Input Format

Your function arguments will receive 2 parameters:

* A natural number `n (1 ≤ n ≤ 10^6)` — the number of integers in the sequence of guest IDs who made requests.
* A one-dimensional array of natural numbers `a` of size `n (1 ≤ aᵢ ≤ 10^9)` — the sequence of guest IDs.

### Output Format

Your function should return a single number — the maximum length of a subsegment that satisfies the condition.

### Constraints

* Time limit: 2 s
* Memory limit: 256 MB

### Example 1

Input:
```

6
3 3 1 2 2 1

```

Output:
```

4

```

### Example 2

Input:
```

2
1 1

```

Output:
```

0

```