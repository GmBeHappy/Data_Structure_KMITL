def insertion_sort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        for j in range(i, -1, -1):
            if value < lst[j-1] and j > 0:
                lst[j] = lst[j-1]
            else:
                lst[j] = value
                break
    return lst


def get_median(sorted_list):
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2])/2
    else:
        return sorted_list[length // 2]



lst = list(map(int, input("Enter Input : ").split()))
sorting = []
for item in lst:
    sorting.append(item)
    sott = sorting.copy()
    insertion_sort(sott)
    print(f"list = {sorting} : median = {get_median(sott):.1f}")