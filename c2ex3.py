# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา

# Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 

def mod_position(arr, s):
    newArr = []
    for i in range(int(s),len(arr)+1,int(s)):
        newArr.append(arr[i-1])
    return newArr
print("*** Mod Position ***")
textStr ,i  = input("Enter Input : ").split(",")
print(mod_position(textStr,i))