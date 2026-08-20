# cook your dish here
a,b,c=map(int,input().split())
if a<b<c:
    print("increasing")
elif a>b>c:
    print("decreasing")
else:
    print("neither")
