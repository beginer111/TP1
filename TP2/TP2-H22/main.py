#!/usr/bin/env python3

import argparse
import numpy as np
import time
import algoGlouton as glouton
import algoDynamique as dynamique
import algoTabou as tabou


def run(algorithm, model_path, algorithm_result, algorithm_time):
    list_of_blocks = np.loadtxt(model_path, dtype=int).tolist()
    myseuil = 23

    if algorithm == 'dynamique':
        begin = time.time()
        final_result = dynamique.algo_dynamique(
            list_of_blocks, len(list_of_blocks))
        end = time.time()

    if algorithm == 'recursif':
        begin = time.time()
        final_result = recursif.algo_recursif(list_of_blocks)
        end = time.time()

    if algorithm == 'seuil':
        begin = time.time()
        final_result = seuil.algo_seuil(list_of_blocks, myseuil)
        end = time.time()

    if algorithm_result:
        print(final_result)

    if algorithm_time:
        print((end - begin) * 1000)


if __name__ == '__main__':
    # source: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", action='store',
                        required=True, type=str)
    parser.add_argument("-e", "--path", action='store',
                        required=True, type=str)
    parser.add_argument("-p", "--result", action='store_true', required=False)
    parser.add_argument("-t", "--total_height",
                        action='store_true', required=False)

    args = parser.parse_args()
    run(args.algorithm, args.path, args.result, args.total_height)
