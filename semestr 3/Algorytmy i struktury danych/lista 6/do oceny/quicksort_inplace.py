from collections import deque
import random
 
def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
def partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex += 1
    swap(a, pIndex, end)
    return pIndex

def iterativeQuicksort(a):
    stack = deque()
    start = 0
    end = len(a) - 1
    stack.append((start, end))
    while stack:
        start, end = stack.pop()
        pivot = partition(a, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))

a = [random.randint(-30,30) for i in range(20)]
print(f"Input list: {a}")
iterativeQuicksort(a)
print(f"Sorted list: {a}")