#!/usr/bin/env python3

import algoBrute
import algoRecursif


def algo_seuil(buildings, seuil):
    number_of_buildings = len(buildings)
    if number_of_buildings <= seuil:
        return algoBrute.algo_brute(buildings)
    else:
        return algoRecursif.algo_recursif(buildings)
