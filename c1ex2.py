# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง

print("*** multiplication or sum ***")
num1 ,num2 = [int(x) for x in input("Enter num1 num2 : ").split()]

if((num1*num2)>1000):
    res = num1 + num2
else:
    res = num1 * num2
print("The result is " + str(res))