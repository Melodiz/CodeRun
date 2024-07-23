import random
import time
from sklearn.metrics import rand_score
from solution import RandIndex 
def generate_test_case(n):
    p = [random.randint(0, n-1) for _ in range(n)]
    v = [random.randint(0, n-1) for _ in range(n)]
    return p, v

def test_rand_index():
    for epochs in range(10):
        n = random.randint(2, 100_000)
        p, v = generate_test_case(n)
        prediction = RandIndex(p, v)
        solution = rand_score(p, v)
        assert abs(prediction[0] / prediction[1] - solution) < 1e-5, f'Epoch {epochs+1}, RandIndex mismatch: {prediction[0]}/{prediction[1]} vs {solution}'
    print('All test cases passed.')

if __name__ == '__main__':
    test_rand_index()