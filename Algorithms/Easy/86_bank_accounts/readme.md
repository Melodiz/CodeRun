# [Банковские счета](link)

## Description

Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую
следующие операции:

Пополнение счета клиента. 
Снятие денег со счёта.
Запрос остатка средств на счёте.
Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пополнения, снятия или перевода денег, ему заводится счёт с нулевым балансом. Все дальнейшие операции проводятся только с этим счётом. Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.
### Input Format:

Входной файл содержит последовательность операций. Возможны следующие операции:
DEPOSIT name sum - зачислить сумму sum на счет клиента name.
Если у клиента нет счета, то счет создается.
WITHDRAW name sum - снять сумму sum со счета клиента name.
Если у клиента нет счета, то счет создается.
BALANCE name - узнать остаток средств на счету клиента name.
TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1
на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается счет.
INCOME p - начислить всем клиентам, у которых открыты счета, p\%
от суммы счета. Проценты начисляются только клиентам с положительным остатком на счету,
если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов
сумма на счету остается целой, то есть начисляется только целое число денежных единиц.
Дробная часть начисленных процентов отбрасывается.

### Output Format:

Для каждого запроса BALANCE программа должна вывести остаток на счету данного
клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите
ERROR.

## Example Test Cases

### Example 1

**Input:**
```
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

```

**Output:**
```
105
-50
ERROR

```

### Example 2

**Input:**
```
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov

```

**Output:**
```
ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179

```

### Example 3

**Input:**
```
BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b

```

**Output:**
```
ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771

```

