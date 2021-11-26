def  isSort(list) :
    for i in range(len(list) - 1) :
        if list[i] >= list[i+1] :
            return 'No'
    return 'Yes'


inp = list(map(int, input('Enter Input : ').split()))
print(isSort(inp))