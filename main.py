from sys import argv

def solution(ip_address):
    pass
    ip = ip_address.split('/')
    i = [i.split('.')[0] for i in ip]

    if int(i[0]) <= 127:
        ip_class = 'A'
        if int(i[0]) == 10:
            Designation = 'Private'
        else:
            Designation = 'Public'

    elif 127 < int(i[0]) <= 191:
        ip_class = 'B'
        if (int(i[0]) == 172) and (16 <= int(i[1]) < 3):
            Designation = 'Private'
        else:
            Designation = 'Public'

    elif 191 < int(i[0]) <= 223:
        ip_class = 'C'
        if (int(i[0]) == 192) and (int(i[1]) == 168):
            Designation = 'Private'
        else:
            Designation = 'Public'

    elif 223 < int(i[0]) <= 239:
        ip_class = 'D'
        Designation = 'Public'

    else:
        ip_class = 'E'
        Designation = 'Public'
    return ip_class, Designation, ip


if __name__ == '__main__':
    pass
    print(
        f"ip address: {solution(argv[1])[2][0]}\nClass: {solution(argv[1])[0]}\nDesignation: {solution(argv[1])[1]}\nSubnet Mask: {solution(argv[1])[2][1]}")
