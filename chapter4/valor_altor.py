def valor_alto(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = valor_alto(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
 
print(valor_alto([0,1,2,4,5,9]))
