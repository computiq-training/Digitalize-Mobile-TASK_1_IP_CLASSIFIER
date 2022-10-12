def solution():

 ip = str(input('Enter IP address: '))
 #print(ip.split('.'))
 divideIp = ip.split('.')
 octets = [int(x) for x in divideIp]

 #class A
 if octets[0] in range(0, 128):
  if octets[0] == 0:
     print('Clas A, designation: private')
  elif octets[0] == 10:
     print('class A , private')
  else: print('Class A, designation: Public')

 #class B
 elif octets[0] in range(128, 191):
   if  octets[0] == 172 and octets[1] in range(16,32):
        print('class B, designation: private')
   else: print('class B, designation: public')

 #class c
 elif octets[0] in range(192, 223):
     if octets[0] == 192 and octets[1] == 168:
          print('class C, designation: private')
     else:print('class C , designation :public')

 #class d
 elif octets[0] in range(224, 240):
      print('class D , designation: special')

 #class E
 elif octets[0] in range(240, 255):
      print('class E, designation: special')

 else: print('the ip address is not found')

# solved the task
if __name__ == '__main__':
    solution()

