def staircase(n):
    if n == 0: 
        return "Not Draw!"
    elif n > 0: 
        stairPos(n, 1)
    else : 
        stairNeg(abs(n), 0)
    return ""

def stairPos(n, k) :

    print('_' * (n - k) + '#' * k)
    if k + 1 <= n:  
        stairPos(n, k + 1)
    if k == n: 
        return
    return   

def stairNeg(n, k) :
    print('_' * k + '#' * (n - k))
    if k + 1 < n: 
        stairNeg(n, k + 1)
    if k == n: 
        return
    return 
    

print(staircase(int(input("Enter Input : "))))