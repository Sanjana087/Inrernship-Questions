fn = float(input("Enter your first number:"))
sign = str(input("Enter the sign of arithmetic:"))
sn = float(input("Enter the second number:"))
if(sign=='+'):
    sum = fn + sn
    print("The summation of",fn,"and",sn,"is",sum)
elif(sign=='-'):
    sub= fn-sn
    print("the substruction of",fn,"and",sn,"is",sub)
elif(sign=='*'):
    mul= fn*sn
    print("the multiplication of",fn,"and",sn,"is",mul)
elif(sign=='/'):
    div= fn/sn
    print("the Division of",fn,"and",sn,"is",div)
else:
    print("Invalid Syntax!!!!!!!!!!!")        
