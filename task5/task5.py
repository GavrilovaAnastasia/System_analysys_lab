import json
import numpy as np

def task(s1, s2):
    ranges_1 = json.loads(s1)
    ranges_2 = json.loads(s2)
    mat_1 = rel_matrix(ranges_1)
    mat_2 = rel_matrix(ranges_2)
    mul_mat = np.multiply(mat_1, mat_2)
    return(conflicts(mul_mat))

def rel_matrix(s):
    rows = len(all_objects(s))
    m = [[0 for _ in range(rows)] for _ in range(rows)]
    d = all_objects(s)
    for y in d:
        for x in d:
            if d[y] <= d[x]:
                m[int(y)-1][int(x)-1] = 1
            else:
                m[int(y)-1][int(x)-1] = 0
    return m

def conflicts(m):
    res = []
    for i in range (len(m)):
        for j in range(i, len(m)):
            if m[i][j] == 0:
                res.append([str(i + 1), str(j + 1)])
    return res

def all_objects(s):
    a = []
    index = []
    for id, elem in enumerate(s):
        if isinstance(elem, list):  
            for el in elem:
                a.append(el)
                index.append(id)
        else:
            a.append(elem)
            index.append(id)
    d = dict(zip(a,index))
    return d

if __name__ == '__main__':
    s1 = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    s2 = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'
    print(task(s1, s2))