from io import StringIO
import csv
import math

def task(csv_string):
    input = serialize_csv(csv_string)
    nodes = unique_nodes(input)
    mat = matrix(nodes, input)
    return(count_enropy(mat))

def serialize_csv(csv_string):
    f = StringIO(csv_string)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    return out

def r1_nodes(graph):
    out = []
    for node in graph:
        out.append(node[0])
    return out

def r2_nodes(graph):
    out = []
    for node in graph:
        out.append(node[1])
    return out

def r3_nodes(graph):
    out = []
    for x in graph:
        for y in graph:
            if x[1] == y[0]:
                out.append(x[0])
    return out
        
def r4_nodes(graph):
    out = []
    for x in graph:
        for y in graph:
            if x[1] == y[0]:
                out.append(y[1])
    return out

def r5_nodes(graph):
    out = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j and graph[i][0] == graph[j][0]:
                out.append(str(graph[i][1]))
    return out

def unique_nodes(graph):
    res = []
    for x in graph:
        for i in x:
            if i not in res:
                res.append(i)
    res.sort()
    return res

def matrix(nodes,graph):
    res = []
    for node in nodes:
        res.append([])
    for node in nodes:
        res[int(node)-1].append(r1_nodes(graph).count(node))
        res[int(node)-1].append(r2_nodes(graph).count(node))
        res[int(node)-1].append(r3_nodes(graph).count(node))
        res[int(node)-1].append(r4_nodes(graph).count(node))
        res[int(node)-1].append(r5_nodes(graph).count(node))
    return res

def count_enropy(matrix):
    res = 0
    k = 5
    n = len(matrix)
    for i in range(n):
        for j in range(k):
            el = matrix[j][i]
            if el != 0:
                res += (el / (n - 1)) * math.log(el / (n - 1), 2)
    return -res

