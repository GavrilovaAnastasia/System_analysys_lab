from io import StringIO
import csv

def task(csv_string):
    input = serialize_csv(csv_string)
    result = []
    return [r1_nodes(input), r2_nodes(input), r3_nodes(input), r4_nodes(input), r5_nodes(input)]
    

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
    return list(dict.fromkeys(out))

def r2_nodes(graph):
    out = []
    for node in graph:
        out.append(node[1])
    return list(dict.fromkeys(out))

def r3_nodes(graph):
    out = []
    for x in graph:
        for y in graph:
            if x[1] == y[0]:
                out.append(x[0])
    return list(dict.fromkeys(out))
        
def r4_nodes(graph):
    out = []
    for x in graph:
        for y in graph:
            if x[1] == y[0]:
                out.append(y[1])
    return list(dict.fromkeys(out))

def r5_nodes(graph):
    out = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j and graph[i][0] == graph[j][0]:
                out.append(str(graph[i][1]))
    return list(dict.fromkeys(out)) 