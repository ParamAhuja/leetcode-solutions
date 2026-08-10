def bubble(arr, n):
    if n<=1:
        return 
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble(arr, n-1)
    
        
arr = [2,1,4,1,7,5]
bubble(arr, 6)
print(arr)