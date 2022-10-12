def solution(ip_address):
 ip_address=input('enter the ip-address')
 ip,sub_mask=ip_address.split('/')
 sepelat=[int(x) for x in ip.split('.')]
 
#class A

 if sepelat[0]>=1 and sepelat[0]<=127:
     ip_class= 'calss A'
     if (sepelat[0]==10 ):
        Desig='privet'
     else:
        Desig='public'
 #class B
 elif sepelat[0]>=128 and sepelat[0]<=191:
     ip_class= 'calss B'
     if (sepelat[0]==172 ):
         if(sepelat[1]>=16 and sepelat[1]<=31 ):
          Desig='privet'
     else:
        Desig='public' 
#class C
 elif sepelat[0]>=192 and sepelat[0]<=223:
     ip_class= 'calss C '
     if (sepelat[0]==192 ):
         if(sepelat[1]==168 ):
          Desig='privet'
     else:
        Desig='public'   
#class D
 elif sepelat[0]>=224 and sepelat[0]<=239:
     ip_class= 'calss C '
     Desig='public'   
#class E
 elif sepelat[0]>=239 and sepelat[0]<=255:
     ip_class= 'calss E '
     Desig='public'   
        
 print(ip_class,Desig )        
 return ip_class,Desig    
if __name__ == '__main__':
    pass
