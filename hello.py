# Area of circle using radius
x=input("Enter the radius of the circle :")
r=int(x)
a=3.14*r**2
print("Area of the circle",a)


# print file extension
filename=input("Enter a filename :")
index=0
for i in range(len(filename)):
    if filename[i]==".":
        index=i
        print("The extension of this file is:")
        print(filename[index+1: ])
