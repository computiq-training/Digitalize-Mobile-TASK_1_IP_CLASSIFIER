import classifyIP as cip
from sys import argv


class Classify:
    # instance from sys library
    IP = str(argv[1])

    # instance class file classify ip
    IP_Address = cip.ClassifyIP(IP)  

    # call up function ip_class from class classify ip
    IP_Address.ip_class()
    
    print(f" IP is Class {IP_Address.class_type}")
    print(f" IP is Designation  {IP_Address.designation_type}")































# --------------------------------------------------------

# def findClass(ip):
#   if(ip[0] >= 0 and ip[0] <= 127):
#     return "This IP Class A"
   
#   elif(ip[0] >=128 and ip[0] <= 191):
#     return "This IP Class B"
   
#   elif(ip[0] >= 192 and ip[0] <= 223):
#     return "This IP Class C"
   
#   elif(ip[0] >= 224 and ip[0] <= 239):
#     return "This IP Class D"
   
#   else:
#     return "This IP Class E"



# --------------------------------------------------------


# def validate_ip(s):  
  
#     # initialize count variable  
#     count = 0  
  
#     # check if period is present  
#     for i in range(0, len(s)):  
#         if(s[i] == '.'):  
#             count = count+1  
#     if(count != 3):  
#         return 0  
  
#     # check the range of numbers between periods  
#     set_val= set()  
#     for i in range(0, 256):  
#         set_val.add(str(i))  
#     count = 0  
#     temp = ""  
#     for i in range(0, len(s)):  
#         if(s[i] != '.'):  
#             temp = temp+s[i]  
#         else:  
#             if(temp in set_val):  
#                 count = count+1  
#             temp = ""  
#     if(temp in set_val):  
#         count = count+1  
  
#     # verifying all conditions  
#     if(count == 4):  
#         return 'Valid Ip address'  
#     else:  
#         return 'Invalid Ip address'  
  
# print(validate_ip('110.234.52.124'))  