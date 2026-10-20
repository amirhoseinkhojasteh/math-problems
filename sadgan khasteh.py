n=str(input())
x=str(input())
if (n[::-1])>(x[::-1]):
    print(x+" < "+n)
elif (x[::-1])>(n[::-1]):
    print(n+" < "+x)
else :
    print(n+" = "+x)
