from zad2testy import runtests

inversions_count = 0

def merge_and_count(arr, left, mid, right):
    global inversions_count
    left_size = mid - left + 1
    right_size = right - mid

    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i, j, k = 0, 0, left

    while i < left_size and j < right_size:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            inversions_count += left_size - i  # Poprawione liczenie inwersji
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

def count_inversions(arr):
    global inversions_count
    inversions_count = 0
    merge_sort(arr, 0, len(arr) - 1)
    return inversions_count


# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
#runtests( count_inversions, all_tests=False )
