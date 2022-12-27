import json
import numpy as np

def task(string):
    str = json.loads(string)
    # выставленные значения рангов переводятся в числовые значения попарных стравнений 
    rangs = count_rangs(str)
    n = len(str[0])
    # задаем матрицу X, содержащую математические ожидания  попарного сравнения объектов
    mat_X = np.zeros((n, n))
    for y in range(n):
        for z in range(n):
            for x in range(len(str)):
                mat_X[y,z] += rangs[x][y][z]
    mat_X = mat_X / n
    # транспонируем матрицу
    mat_X = np.transpose(mat_X)
    k_t = np.ones((len(str)))/len(str)
    e = 0.001
    # выполняем пока максимальная разница оценок объектов в двух соседних шагах больше eps
    while np.linalg.norm(kt(mat_X, k_t, len(str)) - k_t) >= e:
        k_t = kt(mat_X, k_t, len(str))

    return json.dumps(list(np.around(kt(mat_X, k_t, len(str)), 3)))

def yt(x, kt):
    return np.matmul(x, kt)

def kt(x, k_t, n):
    lambda_t = np.matmul(np.ones((n)), np.matmul(x, k_t))
    res = 1 / lambda_t * yt(x, k_t)
    return res

# выставленные значения рангов переводятся в числовые значения попарных стравнений 
def count_rangs(str):
    rangs = np.zeros((len(str), len(str[0]), len(str[0])))
    for x in range(len(str)):
        for y in range(len(str[0])):
            for z in range(len(str[0])):
                if str[x][y] < str[x][z]:
                    rangs[x][y][z] = 0
                elif str[x][y] == str[x][z]:
                    rangs[x][y][z] = 0.5
                else: 
                    rangs[x][y][z] = 1
    return rangs