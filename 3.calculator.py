a=float(input("enter the first no ="))
b=float(input("enter the second no = "))
c=input("what you want to perform + - / * ")
if c=="+":
    print("the sum is",a+b)
elif c=="-":
    print("the difference is ",a-b)
elif c=="*":
    print("the product is ",a*b)
elif c=="/":
    print("the divison is ",a/b)
else:
    print("Invalid symbol")


