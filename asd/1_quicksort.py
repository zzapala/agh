#zaimplementować quicksorta, zuzywajac maksymalnie O(nlogn) pamieci

def partition(T,l,r):
    pivot = T[r]
    i = l-1
    for j in range(l,r):
        if T[j] <= pivot:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def quicksort(T,l,r):
    while l < r:
        pivot = partition(T,l,r)
        if pivot-l < r-pivot:
            quicksort(T,l,pivot-1)
            l = pivot+1
        else:
            quicksort(T,pivot+1,r)
            r = pivot-1
    return T


T = [7,5,3,1,6,3,234,734132,532,1,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]
print(quicksort(T,0,len(T)-1))
    