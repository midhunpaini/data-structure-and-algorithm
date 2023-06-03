# find two numbers in array whose sum is 10

nums = [6,5,4,6,7,8,1,6,6]
def sum_is_ten(arr):
    s = set(arr)
    for num in arr:
        if 10 - num in s:
            return num,10-num
        else:
            s.remove(num)
    return 'No pair avilable'

# shifitin a perticular num to side of an array

def shif_to_right(arr, num):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[j] == num:
            j -= 1
            continue
        if arr[i] == num:
            arr[i],arr[j] = arr[j],arr[i]
        i += 1
    return arr 


print(shif_to_right(nums,6))
