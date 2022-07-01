n=int(input("n ni kiriting: \n"))
s=0
r=0
while n>0:
    r=n%10
    s+=r
    n=n//10
print("""kiritgan raqamlaringiz yig'indisi""",'    ',+s)