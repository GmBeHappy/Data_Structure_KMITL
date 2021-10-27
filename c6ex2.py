def reverse(nums) :
    buff =[]
    if len(nums) == 1    :
        return nums
    else :
        if nums[0] > nums[1]: 
            buff = [nums[0]] + reverse(nums[2:] + [nums[1]])
        else: 
            buff = [nums[1]] + reverse(nums[2:] + [nums[0]])
    return reverse(buff[:-1]) + buff[-1:]     


num = list(map(int, input("Enter your List : ").split(",")))
print(f'List after Sorted : {reverse(num)}')