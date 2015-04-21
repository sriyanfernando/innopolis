import networkx as nx
import numpy as np
from networkx.algorithms import isomorphism

f = open('data.txt', 'rb')

lines = f.readlines()

pares = []

i = 0

while i < len(lines):
    n = int(lines[i].strip())
    matrix = []
    matrix2 = []

    for j in range(i + 1, i + n + 1):
        matrix.append([])
        string = lines[j].strip()

        for e in string:
            matrix[-1].append(int(e))

    i = i + n + 1

    for j in range(i + 1, i + n + 1):
        matrix2.append([])
        string = lines[j].strip()

        for e in string:
            matrix2[-1].append(int(e))

    i = i + n + 2

    g1 = nx.DiGraph(np.array(matrix))
    g2 = nx.DiGraph(np.array(matrix2))

    GM = isomorphism.GraphMatcher(g1,g2)

    print (GM.is_isomorphic())