# This code is inspired by :
# https://www.programcreek.com/python/?CodeExample=get+skyline
# https://www.learnbay.io/the-skyline-problem/
import time

from typing import List


def merge(left, right):
    h1, h2, current_height = 0, 0, 0
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        x0 = left[i][0]
        x1 = right[j][0]
        if x0 <= x1:
            h1 = left[i][1]
            i += 1
        if x1 <= x0:
            h2 = right[j][1]
            j += 1
        if max(h1, h2) != current_height:
            current_height = max(h1, h2)
            result.append([min(x0, x1), current_height])

    result.extend(right[j:])
    result.extend(left[i:])
    return result


def get_skyline(buildings):
    if not buildings:
        return []
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

    left = get_skyline(buildings[:(len(buildings) // 2)])
    right = get_skyline(buildings[(len(buildings) // 2):])
    return merge(left, right)


mylist = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]


def algo_force_brute_time(buildings):
    start = time.time()
    print(get_skyline(buildings))
    end = time.time()
    print("Execution time for algo DPR is: " + str((end - start)))


algo_force_brute_time(mylist)
