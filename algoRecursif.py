#!/usr/bin/env python3

# This code is inspired by :
# https://www.programcreek.com/python/?CodeExample=get+skyline
# https://www.learnbay.io/the-skyline-problem/


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


def algo_recursif(buildings):
    if not buildings:
        return []
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

    left = algo_recursif(buildings[:(len(buildings) // 2)])
    right = algo_recursif(buildings[(len(buildings) // 2):])
    return merge(left, right)

