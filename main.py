import sys

# convert ip to list
#----------------------
def convert2list(ip):
    ip2=[]
    temp=''
    for i in range(0,len(ip)):
        if(ip[i]!='.'):
            temp+=ip[i]
        else:
            ip2.append(temp)
            temp='' 
    ip2.append(temp)
    ip2=[int(x) for x in ip2]
    return ip2
#--------------------
# address to string
#--------------------
def a2s(a):
    x=''
    for i in range(0,len(a)):
        x=x+str(a[i])+'.'
    return x
#------------------------
# check the ip address type A B C OR D
#------------------------
def check(x):
    if(x in range(0,128)):
        return 'A'
    elif(x in range(128,192)):
        return 'B'
    elif(x in range(192,224)):
        return 'C'
    elif(x in range(224,240)):
        return 'D'
    else:
        return 'nothing found'

# assignment for netid and hostid

def finder(ipclass,ipl):
    if(ipclass=='A'):
        netid=a2s(ipl[:1])
        hostid=a2s(ipl[1:])
    elif(ipclass=='B'):
        netid=a2s(ipl[0:2])
        hostid=a2s(ipl[2:])
    elif(ipclass=='C'):
        netid=a2s(ipl[0:3])
        hostid=a2s(ipl[3:])
    else:
        print("CLASS D/E not divided in net & Host id")
        
    print("NetID = " ,netid)
    print("HostID = " ,hostid)
    
ip= sys.argv[1]
ipl = convert2list(ip)
ipclass=check(ipl[0])
finder(ipclass,ipl)
print("Class = " ,ipclass)   
