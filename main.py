import sys
ipaddre = sys.argv[1]
ip, subnet = ipaddre.split("/")
TheIP = ip.split(".")
a = int (TheIP[0])
b = int (TheIP[1])
c = int (TheIP[2])
d = int (TheIP[3])


if (a > 0 and a < 255) and (b > 0 and b < 255) and (c > 0 and c < 255) and (d > 0 and d < 255):


#Class A
    if (a >= 1 and a <= 127):
        The_IpClass_Is = "class A"
        Designation_Is = "Public"
    #private A
        if (a == 10):
            Designation_Is = "Private"

#Class B
    elif (a >= 128 and a <= 191):
        The_IpClass_Is = "class B"
        Designation_Is = "Public"
    #private B
        if (a == 172):
            if (b >=16 and b <= 31):
                Designation_Is = "Private"

#Class C 
    elif (a >= 192 and a <= 223):
        The_IpClass_Is = "class C"
        Designation_Is = "Public"
        # check class C private
        if (a == 192 and b == 168):
            Designation_Is = "Private"

#Class D
    elif (a >= 224 and a <= 239):
        The_IpClass_Is = "class D"
        Designation_Is = "Public"

#Class E
    elif (a >= 240 and a <= 255):
        The_IpClass_Is = "class D"
        Designation_Is = "Public"


    print ("Class: ", The_IpClass_Is, ", Designation: ", Designation_Is)

else:
    print("The IP contain not valid value")


<<<<<<< HEAD

if __name__ == '__main__':
    pass
=======
>>>>>>> dea8128ac19dcdeedbc39bbe4f088913ad058383
