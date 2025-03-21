#n-elementowa tablica, w której elementy są ze zbioru {0, 1, 2, ..., n^2-1}



#4. n-elementowa tablica z parami różnych elementów. znaleźć x i y, które są w tablicy, ze y-x jest największe
# i jednocześnie istnieje z takie, ze jest pomiędzy x a y.

def max_diff(T):
    n = len(T)
    if len(T) < 2:
        return 0
    
    buckets = [[] for _ in range(n)]
    high, low = max(T), min(T)
    ran = high - low
    index = 0

    for num in T:
        if num == high:
            index = n - 1
        else:
            index = (num - low) * (n - 1) // (ran)
        
        buckets[index].append(num)

    res_buckets = []

    for i in range(n):
        if buckets[i]:
            res_buckets.append(min(buckets[i], max(buckets[i])))

    maxi = 0
    result = ()
    
    for i in range(1, len(res_buckets)):
        temp = maxi
        maxi = max(maxi, res_buckets[i-1][1] - res_buckets[i][0])

        if temp != maxi:
            result = (res_buckets[i-1][1], res_buckets[i][0])
    return result

T = [1, 10, 5, 3, 4, 2, 9, 7, 8, 6]
print(max_diff(T)) # (1, 10)