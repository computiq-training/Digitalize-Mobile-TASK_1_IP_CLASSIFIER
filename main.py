import sys
def solution():
    p_address=sys.argv[1]
    ip=ip_address.split('.')
    address=int(ip[0])

    if address in range(0,128):
        if ip[0]=='10':
            print("class: A Designation:private")
        else:
            print("class: A Designation:public")
    elif address in range(128,192):
        if ip[0]=='172' and ip[1] in range(16,32):
            print("class: B Designation:private")
        else:
            print("class: B Designation:public")
    elif address in range(192,224):
        if ip[1]=='168':
            print("class: C Designation:private")
        else:
            print("class: c Designation:public")
    elif address in range(224,240):
        print("class: D")
    elif address in range (240,256):
        print("class: E")
    else:
        print("wrong ip address")
    


if __name__ == '__main__':
    solution()
    
