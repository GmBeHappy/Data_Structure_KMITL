print("*** TorKham HanSaa ***")
arr = [x.split() for x in input("Enter Input : ").split(",")]
newArr= []
isfirst = True
i = 0
for ele in arr:
    if(ele[0]=="P"):
        myLastTwo = ele[1][-2] + ele[1][-1]
        if(arr[i+1][0]!="X" and arr[i+1][0]!="R"):
            nextTwoFirst = arr[i+1][1][0] + arr[i+1][1][1]
        if(isfirst):
            newArr.append(ele[1])
            isfirst = False
        print("'" + ele[1]+"' -> ", end = '')
        print(newArr)
        if(arr[i+1][0]!="X" and arr[i+1][0]!="R"):
            if(myLastTwo.lower()==nextTwoFirst.lower()):
                newArr.append(arr[i+1][1])
            else:
                print("'" + arr[i+1][1]+"' -> game over")
                break
    elif(ele[0]=="R"):
        print("game restarted")
        newArr= []
        isfirst = True
    elif(ele[0]=="X"):
        break
    else:
        print("'" + ele[0] + " " + ele[1]+"' is Invalid Input !!!")
        break
    i = i + 1
    myLastTwo = ""
    nextTwoFirst = ""