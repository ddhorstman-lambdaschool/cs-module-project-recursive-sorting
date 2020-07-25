# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lenA, lenB = len(arrA), len(arrB)
    merged_arr = [0] * (lenA+lenB)
    a = b = 0
    for i in range(lenA+lenB):
        if lenA > a and lenB > b:
            if arrA[a] < arrB[b]:
                merged_arr[i] = arrA[a]
                a += 1
            else:
                merged_arr[i] = arrB[b]
                b += 1
        elif lenA > a:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

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


def merge_sort_in_place(arr, l=0, r=None):
    if not r:
        r = len(arr) - 1
    if r <= l:
        return
    mid = (r+l+1)//2
    merge_sort_in_place(arr, l, mid-1)
    merge_sort_in_place(arr, mid, r)
    return merge_in_place(arr, l, mid, r)

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# merge_sort_in_place(arr1)
