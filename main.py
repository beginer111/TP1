#!/usr/bin/env python3

import argparse
import numpy as np
import time
import algoRecursif as recursif
import algoBrute as brute
import algoSeuil as seuil


def run(algorithm, model_path, algorithm_result, algorithm_time):
    buildings = np.loadtxt(model_path, dtype=int, skiprows=1)
    list_of_buildings = buildings.tolist()
    myseuil = 23

    if algorithm == 'brute':
        begin = time.time()
        final_result = brute.algo_brute(list_of_buildings)
        end = time.time()

    if algorithm == 'recursif':
        begin = time.time()
        final_result = recursif.algo_recursif(list_of_buildings)
        end = time.time()

    if algorithm == 'seuil':
        begin = time.time()
        final_result = seuil.algo_seuil(list_of_buildings, myseuil)
        end = time.time()

    if algorithm_result:
        for s in final_result:
            print(*s)

    if algorithm_time:
        print((end - begin) * 1000)


if __name__ == '__main__':
    # source: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", action='store', required=True, type=str)
    parser.add_argument("-e", "--path", action='store', required=True, type=str)
    parser.add_argument("-p", "--result", action='store_true')
    parser.add_argument("-t", "--time", action='store_true')

    args = parser.parse_args()
    run(args.algorithm, args.path, args.result, args.time)
