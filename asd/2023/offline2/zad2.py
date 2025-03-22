#ksumy
from zad2testy import runtests

# słabe time complexity

def merge(arr, left, right, mid, temp):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            j += 1
        else:
            temp[k] = arr[i]
            i += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

def merge_sort(arr, left, right, temp):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid, temp)
        merge_sort(arr, mid + 1, right, temp)
        merge(arr, left, right, mid, temp)

def use_merge_sort(arr):
    n = len(arr)
    temp = [0] * n
    merge_sort(arr, 0, n-1, temp)

def ksum(T, k, p):
    n = len(T)
    res_sum = 0

    for i in range(n - p + 1):
        part = T[i:i + p]
        use_merge_sort(part)
        res_sum += part[-k] #k-ty najwiekszy element
    
    return res_sum

T = [7, 9, 1, 5, 8, 6, 2, 12]
k = 4
p = 5
print(ksum(T, k, p))

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( ksum, all_tests=True )

