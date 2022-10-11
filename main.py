def solution():
    pass


import sys

ipANDsubnet = sys.argv[1]
ip, subnet = ipANDsubnet.split("/")
wxyz = ip.split('.')

w = int (wxyz[0])
x = int (wxyz[1])
y = int (wxyz[2])
z = int (wxyz[3])


if (w > 0 and w < 255) and (x > 0 and x < 255) and (y > 0 and y < 255) and (z > 0 and z < 255):


#Check if Class A
    if (w >= 1 and w <= 127):
        IpClass = "class A"
        IpDesignation = "Public"
    #check class A private
        if (w == 10):
            IpDesignation = "Private"

#Check if Class B
    elif (w >= 128 and w <= 191):
        IpClass = "class B"
        IpDesignation = "Public"
    # check class B private
        if (w == 172):
            if (x >=16 and x <= 31):
                IpDesignation = "Private"

# Check if Class C
    elif (w >= 192 and w <= 223):
        IpClass = "class C"
        IpDesignation = "Public"
        # check class C private
        if (w == 192 and x == 168):
            IpDesignation = "Private"

# Check if Class D
    elif (w >= 224 and w <= 239):
        IpClass = "class D"
        IpDesignation = "Public"

# Check if Class E
    elif (w >= 240 and w <= 255):
        IpClass = "class D"
        IpDesignation = "Public"


    print ("Class: ", IpClass, ", Designation: ", IpDesignation)

else:
    print("The IP contain not valid value")



if __name__ == '__main__':
    pass



