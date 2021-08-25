# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที

# แล้วแสดงผลเป็น วินาที
# แสดงผลตามตัวอย่าง

print("*** Converting hh.mm.ss to seconds ***")
h ,m ,s = input("Enter hh mm ss : ").split()

if(int(h)<0):
    print("hh("+h+") is invalid!")
elif(int(m)<0 or int(m) >= 60):
    print("mm("+m+") is invalid!")
elif(int(s)<0 or int(s) >= 60):
    print("ss("+s+") is invalid!")
else:
    if(int(h)<10):
        hh = "0" + str(h)
    else:
        hh=h
    if(int(m)<10):
        mm = "0" + str(m)
    else:
        mm=m
    if(int(s)<10):
        ss = "0" + str(s) 
    else:
        ss=s
    sec = (int(h)*60*60) + (int(m)*60) + int(s)
    print('{}:{}:{} = {:,} seconds'.format(hh,mm,ss,sec))