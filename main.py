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
