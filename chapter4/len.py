def contar(arr):
    if arr == []:
        return 0
    return 1 + contar(arr[1:])

print(contar([0,1,2,3,4,5]))
