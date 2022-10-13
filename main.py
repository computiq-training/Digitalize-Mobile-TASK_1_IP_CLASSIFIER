from sys import argv

def solution(ip_address):
    ip,sub_mask=ip_address.split('/')
    octets=[int(x) for x in ip.split('.')]
    
    # CLASS  A
    if octets[0] <= 127: 
        ip_class='A'
        if octets[0] == 10: Designation='Private'
        else: Designation='Public'

    # CLASS B
    elif 127 < octets[0] <= 191: 
        ip_class='B'
        if (octets[0] == 172) and (16 <= octets[1] <= 31): Designation='Private'
        else: Designation='Public'
    
    # CLASS C
    elif 191 < octets[0] <= 223: 
        ip_class='C'
        if (octets[0] == 192) and (octets[1] == 168): Designation='Private'
        else: Designation='Public'
    
    # CLASS D
    elif 223 < octets[0] <= 239: 
        ip_class='D'
        Designation='Public'
    
    # CLASS E
    else: 
        ip_class='E'
        Designation='Public'

    return ip_class,Designation


if __name__ == '__main__':
    print(f"Output: Class: {solution(argv[1])[0]}, Designation: {solution(argv[1])[1]}")