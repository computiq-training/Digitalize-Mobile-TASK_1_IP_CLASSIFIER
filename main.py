def check_ip(ip):
    # check if ip out of the range between 0, 255
    state = True
    if ip[0] < 256 and ip[0] < 0:
        state = False
    elif ip[1] < 256 and ip[1] < 0:
        state = False
    elif ip[2] < 256 and ip[2] < 0:
        state = False
    elif ip[3] < 256 and ip[3] < 0:
        state = False
    return state

def solution(ip_address):
    if '.' in ip_address:
        # First process split the ip than,
        # find the class and,
        # set the state for the network
        ip = ip_address.split(".")
        ip1 = [ i.split('/') for i in ip ]
        ip = [int(ip1[i][0]) for i in range(3)] + [int(ip1[3][0][0])]
        if check_ip(ip):
            state = 'Public'
            Class = 'Not Valid'
            # check class 'A'
            if  0 < ip[0] < 128:
                Class = 'A'
                if ip[0] == 10:
                    state = 'Private'
            # check class 'B'
            elif 127 < ip[0] < 192:
                Class = 'B'
                if ip[0] == 172 and 15 < ip[1] < 32:
                    state = 'Private'
            # check class 'C'
            elif 191 < ip[0] < 224:
                Class = 'C'
                if ip[0] == 192 and ip[1] == 168:
                    state = 'Private'
            # check class 'D'
            elif 223 < ip[0] < 240:
                Class = 'D'
                state = 'Not Have State'
            # check class 'E'
            elif 239 < ip[0] < 256:
                Class = 'E'
                state = 'Not Have State'
            print(f'Output: Class: {Class}, Designation: {state}')
            # if this ip is not valid 
        else:
            # show massage if erorr ip address
            print(f'This IP Address: {ip_address} Is Not Valid.')


            
if __name__ == '__main__':
    # First we must Enter IP address
    ip = input('Enter the IP: ')
    # Call the check-up method
    solution(ip)

