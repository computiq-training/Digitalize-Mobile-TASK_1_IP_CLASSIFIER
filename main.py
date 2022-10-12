import check_ip as check
from sys import argv

class main:

    # argv to read ip as str
    IP = str(argv[1])

# instance class checkip
    Ip_Address = check.CheckIp(IP)

# call our check function classip
    Ip_Address.classip()

    print(f" Ip is in Class {Ip_Address.ip_class_name}")
    print(f" Ip Class is a {Ip_Address.ip_designation}")