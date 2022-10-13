import sys

Ip = sys.argv[1]

ip, maskaddress = Ip.split('/')
ip_split = ip.split('.')

if len(ip_split) != 4:

    print('invalid ip address')

ip_split = [int(i) for i in ip_split]

for i in ip_split:
    if i in range(0, 256):
        pass
    else:
        print('please try again ')
        exit()

# Class A
if (ip_split[0]) == 127 and (ip_split[1]) in range(0, 256):
    print('Class : A \nDesignation : Special')
elif ip_split[0] in range(0, 127):
    if ip_split[0] == 10:
        print('Class : A \nDesignation : Private')
    else:
        print('Class : A \nDesignation : Public')

# Class B
elif ip_split[0] in range(128, 192):

    if (((ip_split[0]) == 172) and (ip_split[1] in range(16, 32))) or (((ip_split[0]) == 169)):
        print('Class : B \nDesignation : Private')
    else:
        print('Class : B \nDesignation : Public')

# Class C
elif ip_split[0] in range(192, 224):
    if ((ip_split[0]) == 192 and (ip_split[1]) == 168):
        print('Class : C \nDesignation : Private')
    else:
        print('Class : C \nDesignation : Public')

# Class D
elif ip_split[0] in range(224, 240):
    print('Class : D \nDesignation : Special')

# Class E
elif ip_split[0] in range(240, 256):
    print('Class : E \nDesignation : Special')
