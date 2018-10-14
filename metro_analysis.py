"""
需要使用的话, 参照这个文件即可.
请使用python3
"""


import random
import time

import matplotlib.pyplot as plt
import networkx as nx

import excel_util
from mapx import GraphMaster

g = GraphMaster('metro_graph/gz_metro_graph_v2.2_11.json').graph   # init a graph


def output(result_dict, name):
    print(result_dict)
    sorted_keys = sorted(result_dict, key=lambda k: result_dict[k], reverse=True)
    print('sorted', sorted_keys)
    d = {e: result_dict[e] for e in sorted_keys}
    excel_util.write_excel(r'{}{}.xls'.format(name, int(time.time()) + random.randint(-1000, 1000)), d)
    nx.draw(g, with_labels=True, font_weight='bold')
    # plt.subplot(121)
    plt.show()


def do_closeness():
    closeness_dict = nx.algorithms.centrality.closeness_centrality(g)
    output(closeness_dict, 'closeness')


def do_betweenness():
    btn_dict = nx.algorithms.centrality.betweenness_centrality(g)
    output(btn_dict, 'betweenness')


def do_degree():
    degree_dict = nx.algorithms.centrality.degree_centrality(g)
    output(degree_dict, 'degree')


if __name__ == '__main__':
    pass
    do_closeness()
    do_betweenness()
    do_degree()
