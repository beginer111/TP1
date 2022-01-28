#!/usr/bin/env python3

import time
import heapq

from typing import List


def algo_force_brute_time(buildings):
    start = time.time()
    algo_force_brute(buildings)
    end = time.time()
    print("start time is " + str(start) + " and end time is " + str(end))
    print("Execution time for algo naif is: " + str((end - start)))


mylist = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]


def algo_force_brute(buildings: List[List[int]]):
    critical_points = []
    for building in buildings:
        # find critical points of each building and put them in the list
        critical_points.extend([[building[0], building[2]]])
        critical_points.extend([[building[1], 0]])
    # ascending sort of critical points
    critical_points.sort()
    result = []
    # Transform result list into a heap in linear time; source: https://docs.python.org/3/library/heapq.html
    heapq.heapify(result)

    for critical_point in critical_points:
        for building in buildings:
            # verify if each critical point is inside a building or not, and if so chang its height
            if building[0] < critical_point[0] < building[1] and critical_point[1] <= building[2]:
                critical_point[1] = building[2]

        # verify if each critical point is eligible to be added to the result heap
        if (len(result) == 0) or (result[-1][1] != critical_point[1]):
            heapq.heappush(result, critical_point)

    print(result)


algo_force_brute_time(mylist)
