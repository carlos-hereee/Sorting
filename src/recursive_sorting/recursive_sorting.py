# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(small_array, larger_array):
    elements = len(small_array) + len(larger_array)
    merged_arr = [0] * elements
    # TO-DO

    # create index
    small_index, big_index = 0, 0

    # while the small index is less than the small array, and the big index is less than the larger array
    while small_index < len(small_array) and big_index < len(larger_array):
        # if the small's index is less than the larger array index
        if small_array[small_index] < larger_array[big_index]:
            # append the smaller arry in to the merged arr variable
            merged_arr.append(small_array[small_index])

            small_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i = i+1
            else:
                arr[k] = right_half[j]
                j = j+1
            k = k+1

        while i < len(left_half):
            arr[k] = left_half[i]
            i = i+1
            k = k+1

        while j < len(right_half):
            arr[k] = right_half[j]
            j = j+1
            k = k+1

    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
