class ClassifyIP:

    check_ip = True
    class_type = ''
    designation_type = ''
    
    def __init__(self, IP):

        try:

            # split IP with Prefix
            self.full_ip = IP.split('/')

            # make the IP as tuple
            self.ip = tuple(int(part) for part in self.full_ip[0].split('.'))

            # check if IP is a valid address
            for ip in self.ip:
                if ip < 0 or ip > 255:
                    # if the ip address outside range 
                    self.check_ip = False

            # Check if the IP Address have a prefix
            if '/' in IP:
                self.prefix = int(self.full_ip[1])

        except:
            print('Wrong IP Address')


    # Check IP Class 
    def ip_class(self):
        try:
            if self.check_ip:
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
                return 'invalid ip address'
        except:
            print("Error IP Address")