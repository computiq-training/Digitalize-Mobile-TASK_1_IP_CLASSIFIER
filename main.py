import sys
ip_address=sys.argv[1]
ip_address2= ip_address.split('.')
ip_address3= ip_address.split('/')
x=int(ip_address2[0])
y=(int(len(ip_address2)))
k=(int(len(ip_address3)))

if y==4 and k==2:
    print('the ip address is accept')
    if (x>=0 and x<=128):
        print('class A')
        designation="public"

        if (x== 10):
            designation="private"


    # Check if Class B
    elif (x >= 129 and x <= 191):
        print('class B')
        designation="public"
        if (x == 172):
            designation = "private"




# Check if Class C
    elif (x >= 192 and x <= 224):
        print ('class C')
        designation = "public"
        if(x == 192):
            designation = "private"



 # Check if Class D
    elif (x >= 225 and x<= 239):
        print('class D')
        designation = "public"
# Check if Class E
    elif (x >= 240 and x <= 255):
        print('class E')
        designation = "public"
    print(designation)
else:
    print('the ip address is not correct')