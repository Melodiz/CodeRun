# Solution for https://coderun.yandex.ru/problem/svd-recommender
# Other solutions: https://github.com/Melodiz/CodeRun

import numpy as np

def main():
    f = open('input.txt','r')
    k,U,M,D,T = map(int,f.readline().split())
    u_data = []
    m_data = []
    r_data = []
    for i in range(D):
        u,m,r = map(int,f.readline().split())
        u_data.append(u)
        m_data.append(m)
        r_data.append(r)

    train = np.array(list(zip(u_data,m_data,r_data)))
    mu = train[:,2].mean()

    b_u = np.zeros(U)
    m_u = np.zeros(M)
    p_u = np.random.normal(0, 0.1, (U, 20))
    q_m = np.random.normal(0, 0.1, (M, 20))
    lr = 0.02
    reg = 0.03

    for _ in range(10):
        for u, m, r in train:
            err = r - (mu + b_u[u] + m_u[m] + q_m[m] @ p_u[u])

            b_u[u] += lr * (err - reg * b_u[u])
            m_u[m] += lr * (err - reg * m_u[m])
            p_u[u] += lr * (err * q_m[m] - reg * p_u[u])
            q_m[m] += lr * (err * p_u[u] - reg * q_m[m])

    for i in range(T):
        u,m = map(int,f.readline().split())
        r = mu + b_u[u] + m_u[m] + q_m[m] @ p_u[u]
        print(r)
if __name__ == "__main__":
    main()