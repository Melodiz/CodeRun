# [Оптимальная константа 2.0](link)

## Description

Кеша решает задачу повышения счастья новых пользователей сервиса с помощью машинного обучения. Он уже сделал предварительную обработку данных и подготовил обучающую выборку. Решается задача регрессии, в которой целевая функция имеет вид $t_i = \frac{a_i}{b_i}$, где $a_i$ и $b_i$ - статистики, влияющие на счастье пользователя. Для обучения используется техника перевзвешивания: каждому объекту обучающей выборки приписывается вес, который отвечает за "важность" данного объекта. Для повышения устойчивости модели в качестве веса используется $w_i = b_i$. 
Таким образом, обучающая выборка - это набор из $n$ объектов, представляющих собой тройки $ (x_i, a_i, b_i) $, где $x_i$ - признаковое описание объекта, то есть вектор вещественных чисел длиной $k$ (важно помнить, что признаки **не будут** использоваться при применении в продакшене).

Пусть $p$ - прогноз модели, тогда используемые метрики можно записать следующим образом:

1. Mean squared error

$$
MSE = \frac{ \sum w_i \cdot (t_i - p)^2 }{\sum w_i}
$$

2. Mean squared logarithmic error

$$
MSLE = \frac{ \sum w_i (ln(1 + t_i) - ln(1 + p))^2 }{\sum w_i}
$$


3. Logistic loss

$$
LogLoss = - \frac{ \sum w_i [\frac{t_i}{C}  ln(\frac{p}{C}) + (1 - \frac{t_i}{C}) ln(1 - \frac{p}{C})]}{\sum w_i}
$$

Для использования данной метрики необходимо, чтобы $t_i \in (0, 1), p_i \in (0, 1)$, $i = 1, 2, ..., n$. Из-за возникновения довольно больших значений целевой функции и предсказаний, в формуле присутствует $C$ - некоторая «достаточно большая» константа, отвечающая за нормировку значений $t_i$ и $p_i$. 

Для каждой из представленных метрик вам необходимо найти оптимальный константный прогноз, максимизирующий счастье пользователей в соответствии с этой метрикой. То есть требуется найти три константы, при которых значения каждой из соответствующих метрик будут минимальны на обучающей выборке.
### Input Format:

В первой строке входных данных содержится два целых числа *n* (1 $\leq$ *n* $\leq$ $10^{3}$) и *k* (1 $\leq$ *k* $\leq$ $10^{2}$) - число объектов и размер вектора признаков.

В следующих *n* строках вводятся описания объектов. Каждое описание состоит из *k* вещественных чисел $x_{i}$ ($-10^{3} \leq x_{i} \leq 10^{3}$) - признакового описания объекта, а также $a_{i}, b_{i}$ ($-10^{3} \leq a_{i}, b_{i} \leq 10^{3}$) - статистик, влияющих на счастье пользователя.

### Output Format:

В единственной строке выведите три числа - константы, при которых значения каждой из соответствующих метрик будут минимальны на обучающей выборке.

## Example Test Cases

### Example 1

**Input:**
```
5 1
5.66192 6.322711 121.257938
3.049585 5.285749 46.892782
0.227632 4.771393 9.516171
145.759519 5.320249 28.646039
22.774692 13.604903 36.033962
```

**Output:**
```
0.14568 0.138623 0.14568
```

