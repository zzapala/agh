# plan:
# merge sort, w trakcie którego będę porównywać, ile elementów jest mniejszych



smaller_numbs = 0

def merge_and_count(arr, left, mid, right):
    global smaller_numbs
    left_size = mid - left + 1
    right_size = right - mid

    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i, j, k = 0, 0, left

    while i < left_size and j < right_size:
        if left_part[i] >= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            smaller_numbs += left_size - i  # Poprawione liczenie inwersji
            j += 1
        k += 1

    while i < left_size:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < right_size:
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if right > left:
        mid = (right + left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge_and_count(arr, left, mid, right)

def count_smaller_numbs(arr):
    global smaller_numbs
    smaller_numbs = 0
    merge_sort(arr, 0, len(arr) - 1)
    return smaller_numbs


T = [8,5,1,12,7,6]
print(count_smaller_numbs(T))  # 7