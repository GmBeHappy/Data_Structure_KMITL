def power(n, p) :
    if p > 0    :
        return n * power(n, p - 1)
    elif p == 0 :
        return 1

a, b = map(int, input("Enter Input a b : ").split(" "))
print(power(a, b))