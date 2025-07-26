class Answer:
    _slots_ = [
        'sum', 
        'field',
    ]

    def __init__(self, sum, field):
        self.sum = sum
        self.field = field

def solution(n):
    total_sum = 3 * n**2 - 5 * n + 2 if n != 1 else 0
    field = ['-'* n if i% 2 == 0 else 'x' * n for i in range(n)]
    return Answer(
        sum=total_sum,
        field=field,
    )

if __name__ == "__main__":
    n = int(input())
    print(solution(n).sum)
    print('\n'.join(solution(n).field))