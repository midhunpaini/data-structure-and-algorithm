def linear_search(arr,num):
    for n in arr:
        if n == num:
            return True
    return False


def binary_search(arr,num):
    start = 0
    end = len(arr)-1

    while start<=end:
        middle = (start+end)//2
        if num == arr[middle]:
            return True
        elif num < arr[middle]:
            end = middle-1
        else:
            start = middle + 1
    return False


def _binary_search_recursion(arr,num,start,end):
    if start>end:
        return False
    
    middle = (start+end)//2

    if num == arr[middle]:
        return True
    elif num < arr[middle]:
       return _binary_search_recursion(arr,num,start,middle-1)
    else:
       return _binary_search_recursion(arr,num,middle+1,end)

def binary_search_recursion(arr,num):
    start = 0
    end = len(arr)-1
    return _binary_search_recursion(arr,num,start,end)


print(binary_search_recursion([1,6,3,9,7],1))
