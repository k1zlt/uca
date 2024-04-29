import pandas as pd
import os
from collections import defaultdict
import time

logs = []


def log(message=''):
    logs.append(str(message))
    print(message)


def import_edge_list(benchmark):
    edge_list = []
    if benchmark.endswith('.txt'):
        with open('benchmarks/' + benchmark) as f:
            for line in f:
                edge = line.split()
                edge_list.append((int(edge[0]), int(edge[1])))
    elif benchmark.endswith('.xlsx'):
        df = pd.read_excel('benchmarks/' + benchmark)
        for index, row in df.iterrows():
            edge_list.append(list(map(int, row.tolist())))
    else:
        log('Invalid file format')
        return None
    return edge_list


def mdg_algorithm(edge_list):
    cover = set()
    degree_dict = defaultdict(int)
    max = [-1, -1]
    while len(edge_list) > 0:
        degree_dict.clear()
        for edge in edge_list:
            degree_dict[edge[0]] += 1
            degree_dict[edge[1]] += 1
            if degree_dict[edge[0]] > max[1]:
                max = [edge[0], degree_dict[edge[0]]]
            if degree_dict[edge[1]] > max[1]:
                max = [edge[1], degree_dict[edge[1]]]
        cover.add(max[0])
        edge_list = [edge for edge in edge_list if max[0] != edge[0] and max[0] != edge[1]]
        max = [-1, -1]
    return cover


if __name__ == '__main__':
    main = time.time()
    benchmarks_list = os.listdir('benchmarks')

    for benchmark in benchmarks_list:
        log("Benchmark " + benchmark + " is being processed.")
        edge_list = import_edge_list(benchmark)
        log("Number of edges: " + str(len(edge_list)))
        start = time.time()
        res = mdg_algorithm(edge_list)
        log(res)
        log("Number of vertices in the cover: " + str(len(res)))
        log("Time taken: " + str(time.time() - start))
        log()

    log("Total time taken: " + str(time.time() - main))
    with open('logs.txt', 'w') as f:
        for log_entry in logs:
            f.write(log_entry + '\n')
