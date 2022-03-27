from typing import List

# Dynamic Programming implementation
# of Box Stacking problem


def algo_dynamique(arr: List[List[int]], n):
    # Initialize msh values for all indexes
    # msh[i] --> Maximum possible Stack Height
    # with box i on top
    msh = [0] * n
    result = []

    for i in range(n):
        msh[i] = arr[i][0]

    # Compute optimized msh values
    # in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i][1] < arr[j][1] and
                    arr[i][2] < arr[j][2]):
                if msh[i] < msh[j] + arr[i][0]:
                    msh[i] = msh[j] + arr[i][0]
                    result.append(arr[i])

    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])

        print(result)
    return maxm
