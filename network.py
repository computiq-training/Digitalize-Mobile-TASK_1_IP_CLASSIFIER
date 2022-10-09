class Network:
    designation_type = ''
    correct_ip = True
    class_type = ''
    prefix = None

    def __init__(self, p_IP):
        try:

            # split the the string into IP and Prefix
            self.full_ip = p_IP.split('/')
            # make the IP as tuple
            self.ip = tuple(int(part) for part in self.full_ip[0].split('.'))

            # check if IP is a valid address
            for ip in self.ip:
                if ip < 0 or ip > 255:
                    self.correct_ip = False

            # check if the args have a prefix
            if '/' in p_IP:
                self.prefix = int(self.full_ip[1])
            # else:
            # print('there is no prefix provided //optional message')
        except:
            print('something went wrong')

    # check prefix
    def class_type(self):
        try:
            if self.prefix is not None:
                if self.prefix == 8:
                    return 'A'
                elif self.prefix == 16:
                    return 'B'
                elif self.prefix == 24:
                    return 'C'
                else:
                    return 'D or E'
        except:
            print('There is no prefix provided')

    # check IP class and prefix
    def ip_type(self):
        try:
            if self.correct_ip:
                if 1 <= self.ip[0] <= 127:
                    self.class_type = 'A'
                elif 128 <= self.ip[0] <= 191:
                    self.class_type = 'B'
                elif 192 <= self.ip[0] <= 223:
                    self.class_type = 'C'
                elif 224 <= self.ip[0] <= 239:
                    self.class_type = 'E'
                else:
                    self.class_type = 'D'

                if self.ip[0] == 10 or (self.ip[0] == 172 and 16 <= self.ip[1] <= 31) or self.ip[
                    0] == 192 and self.ip[1] == 168 \
                        and 0 <= self.ip[2] <= 255:
                    self.designation_type = 'Private'
                else:
                    self.designation_type = 'Public'
            else:
                return 'invalid ip'
        except:
            print("Error")
