class CheckIp:

    # first def. a flag to check the ip is in the range and start with Ture value
    # define a var to take the class name and another one to store the value either private or public

    is_ip = True
    ip_class_name = ''
    ip_designation = ''

# constructor take ip as parameter

    def __init__(self, ip):

        # split the ip that come with '/' and store it as one big var

        self.all_ip = ip.split('/')

# make all the ip address as tuple that we can do some check on it

        self.Ip = tuple(int(i) for i in self.all_ip[0].split('.'))

# if the ip has a '/' split it

        if '/' in ip:
            self.part = int(self.all_ip[1])

# first check the ip adrees is valid using is_ip
        for i in self.Ip:
            if i < 0 or i > 255:
                self.is_ip = False

# method to check the ip class

    def classip(x):
        if x.is_ip:
            if 1 <= x.Ip[0] <= 127:
                x.ip_class_name = 'A'
            elif 128 <= x.Ip[0] <= 191:
                x.ip_class_name = 'B'
            elif 192 <= x.Ip[0] <= 223:
                x.ip_class_name = 'C'
            elif 224 <= x.Ip[0] <= 239:
                x.ip_class_name = 'D'
            elif 240 <= x.Ip[0] <= 255:
                x.ip_class_name = 'E'
            else:
                print('not valid')
# check either private or public depands on first three parts
        if x.is_ip:
            if x.Ip[0] == 10 or (x.Ip[0] == 10 and x.Ip[1] < 31) or (x.Ip[0] == 192 and x.Ip[1] == 168 and
                                                                     0 <= x.Ip[2] <= 255):
                x.ip_designation = 'private'
            else:
                x.ip_designation = 'public'
