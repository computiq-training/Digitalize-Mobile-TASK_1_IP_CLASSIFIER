# def solution():
#     pass



import sys
ip_subnet =sys.argv[1]
ip,subnet=ip_subnet.split("/")
part=ip.split(".")
A=int(part[0])
B=int(part[1])
C=int(part[2])
D=int(part[3])

# print(A,B,C,D)


 # Check Range Of Ip To Assign Class & Designation
#  --------------------------------------------------
# Check if Class is A
if A>0 and A<=127:
    print("class :","A")
 # Check Designation
    if (A==10):
        print("designation : private")
    else:
        print("designation : Public")
# Check if Class is B      
elif A>127 and A<=191:
    print("class :","B")
# Check Designation    
    if (A==172):
        if B>=16 and B<=31:
            print("designation : private")
        else:
            print("designation : Public")
    else:
        print("designation : Public")
# Check if Class is C        
elif A>191 and A<=223:
    print("class :","C")
# Check Designation
    if (A==192 and B==168):
        print("designation : private")
    else:
        print("designation : Public")
   
# Check if Class is D    
elif A>223 and A<=239:
    print("class :","D\ndesignation : Public")
# Check if Class is E
elif A>=240 and A<=255:
    print("class :","E\ndesignation : Public")























# if __name__ == '__main__':
#     pass
