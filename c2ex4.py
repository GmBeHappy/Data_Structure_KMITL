# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

arr = [int(x) for x in input("Enter Your List : ").split()]

def findThreeSum(nums):
        if len(nums) < 3:
            return []

        ansArr = []
        nums.sort()
        for currentIndex in range(0, len(nums)-2):
            if nums[currentIndex] > 0:
                continue
                
            if nums[currentIndex] == nums[currentIndex-1] and currentIndex > 0:
                continue
                
            first_ptr = currentIndex+1
            second_ptr = len(nums)-1
            
            while first_ptr < second_ptr:
                sum = nums[currentIndex] + nums[first_ptr] + nums[second_ptr]
                
                if sum == 5:
                    ansArr.append([nums[currentIndex], nums[first_ptr], nums[second_ptr]])        
                if sum <= 5:
                    first_ptr += 1
                    while nums[first_ptr] == nums[first_ptr-1] and first_ptr < second_ptr:
                        first_ptr += 1
                else:
                    second_ptr -= 1
                    
        return ansArr
if(len(findThreeSum(arr))==0):
    print("Array Input Length Must More Than " + str(len(arr)))
else:
    print(findThreeSum(arr))