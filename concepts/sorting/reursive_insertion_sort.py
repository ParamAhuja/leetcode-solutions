def insertion(arr, n):
    if n <= 1:
        return
    insertion(arr, n - 1)
    
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

        
arr = [2,1,4,1,7,5]
insertion(arr, 6)
print(arr)