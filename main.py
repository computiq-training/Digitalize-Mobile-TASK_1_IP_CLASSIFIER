import sys
def solution():

    ip = sys.argv[1]
    parts = ip.split('/')[0].split('.')
    p1, p2, p3, p4 = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
    
    if p1 == 10 or p1 == 169 and p2 == 254 or p1 == 172 and p2 in range(16, 32) or p1 == 192 and p2 == 168:
        d = 'Private'
    elif p1 == 127 and p4 != 0: d = 'Special'
    else: d = 'Public'

    Class = ''
    if   p1 in range(0  , 128):
        Class = 'A'
    elif p1 in range(128, 192):
        Class = 'B'
    elif p1 in range(192, 224):
        Class = 'C'
    elif p1 in range(224, 240):
        Class = 'D'
    else:
        Class = 'E'

    # if p1 or p2 or p3 or p4 < 0:
    #  raise ValueError("Wrong IP address, no numbers below zero are allowed.")
    # if p1 or p2 or p3 or p4 > 255:
    #  raise OverflowError("Wrong IP address, no numbers bigger than 255 are allowed.")
    # if p1 or p2 or p3 or p4 < 0 and p1 or p2 or p3 or p4 > 255:
    #  raise ValueError("Wrong IP address, no numbers below zero and over 255 are allowed.")

    print(f'Class: {Class}, Designation: {d}')
solution()
