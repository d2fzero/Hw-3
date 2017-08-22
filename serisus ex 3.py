#a
n=int(input("nhap n"))
for i in range (n):
    print("*",end='')
#b
print()
n=int(input("nhap n"))
for i in range (n):
    print("X",end='')
    print("*",end='')
#c
print()
#d
n=int(input("nhap n"))
m=int(input("nhap m"))
for j in range (m):
        if j%2==0:
            for i in range (n):
                print("X * ",end='')

        else:
            for i in range (n):
                print("* X ",end='')
        print()