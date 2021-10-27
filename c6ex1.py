def findMax(nums) :
    if len(nums) == 1 :
        return nums[0]
    else :
        numMax = findMax(nums[1:])
        return numMax if nums[0] < numMax else nums[0]
    

num = list(map(int, input('Enter Input : ').split()))
print(f'Max : {findMax(num)}')
    