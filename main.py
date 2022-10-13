#def solution(ip_address):
ip_address=input('enter the ip-address')
ip=ip_address.split('/')
sepelat= [int( i.split('.')[0]) for i in ip]

 
#class A
if sepelat[0]>=1 and sepelat[0]<=127:
     ip_class= 'calss A'
     if (sepelat[0]==10 ):
        Designation='privet' 
     else:
        Designation='public'
     print(ip_class,Designation)
 #class B
elif sepelat[0]>=128 and sepelat[0]<=191:
     ip_class= 'calss B'
     if (sepelat[0]==172 ):
         if(sepelat[1]>=16 and sepelat[1]<=31 ):
          Designation='privet'
     else:
       Designation='public' 
     print(ip_class,Designation)
#class C
elif sepelat[0]>=192 and sepelat[0]<=223:
     ip_class= 'calss C '
     if (sepelat[0]==192 ):
         if(sepelat[1]==168 ):
          Designation='privet'
     else:
        Designation='public' 
     print(ip_class,Designation)  
#class D
elif sepelat[0]>=224 and sepelat[0]<=239:
     ip_class= 'calss D '
     Designation='public'   
     print(ip_class,Designation)
#class E
elif sepelat[0]>=239 and sepelat[0]<=255:
     ip_class= 'calss E '
     Designation='public'
     print(ip_class,Designation)   
     
#x={'class':ip_class,'Designation':Designation }  
#print (x) 
#return {'class':ip_class,'Designation':Designation } 
if __name__ == '__main__':
    pass
#/