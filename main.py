def solution():
    pass
import sys
list_IP = sys.argv[1:] # take value as list !!
convertToStr=''.join(list_IP) # convert the list 2 string to spilt the .
spaer_IP = convertToStr.split('.') # the split :) now each value as string so we can't compar with other num
x = int(spaer_IP[0])
x = int(spaer_IP[0])
y = int(spaer_IP[1])
z = int(spaer_IP[2])
w = int(spaer_IP[3].split('/')[0])
if x>=0 and x<=255 and y>=0 and y<=255 and z>=0 and z<=255 and w>=0 and w<=255 : # comper out the range 
    if x in range (1,128): # Determine the class of each one 
        print("It's class A ")
    elif x in range (128,192):
        print("It's class Bg ")
    elif x in range (192,224):
        print("It's class C ")
    elif x in range(224,240):
        print("It's class D ")
    else: 
        print("It's Class E")
    if x == 10:  # Determine the public or privet class of each one 
        print("and it's privat IP")
    elif x==196 and y==245:
        print("and it's privat IP")
    elif x==172 and y==16 and y ==31:
        print("and it's privat IP")
    elif x==192 and y==168 :
        print("and it's privat IP")   
    else:
        print("and It's Public IP")
else:
    print("you can't take number greater than 255 or less then zero ")


if __name__ == '__main__':
    pass
