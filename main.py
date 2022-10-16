import sys
ia = str(sys.argv)
ip = ia.split('.')
ip_address = [i.split('/')[0] for i in ip ]
print(ip_address)

a = int(ip_address[1])
b = int(ip_address[2])
c = int(ip_address[3])
d = int(ip_address[4])

if a in range(1,127) and b in range(0,256)and c in range(0,256) and d in range(0,255):
    print("The class is A ")
    if a == 10 and b in range(0,256)and c in range(0,256) and d in range(0,255):
        print("the designation is private")
    else: print("the designation is public")
elif a in range(128,192) and b in range(1,256)and c in range(0,256) and d in range(1,255):
    print("The class is B ")
    if a == 172 and b in range(16,32)and c in range(0,256) and d in range(0,255):
        print("the designation is private")
    else: print("the designation is public")
elif a in range(192,224) and b in range(0,256)and c in range(1,256) and d in range(1,255):
    print("The class is C ")
    if a == 192 and b == 168 and c in range(0,256) and d in range(0,255):
        print("the designation is private")
    else: print("the designation is public")
elif a in range(224,240) and b in range(0,256)and c in range(0,256) and d in range(0,256):
    print("The class is D ")
    print("the designation is private")
elif a in range(240,255) and b in range(0,256)and c in range(0,256) and d in range(0,255):
    print("The class is E ")
    print("the designation is private")