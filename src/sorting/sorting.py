# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(elements):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        elif len(arrA) > 0:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)

    return merged_arr


def merge_sort(arr):
    # Your code here
    # Length 1: sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
