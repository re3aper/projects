a=[0,128,256]
agrmax=int(input("Entered Input \n"))
max1=a[0]
zero=0
length=0
for i in range (0,agrmax):
    newmember=int(input("Input member \n"))
    a.append(newmember)
    length=length+1
    if a[i]<max1:
        max1=zero
        break
    if newmember==agrmax:
        break

print(zero)
print(length)


    
    
    
