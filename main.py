from sys import argv
import network as net


class Classify:
    IP_parameter = str(argv[1])
    # IP_parameter = '192.168.1.17/24'
    # create new instance
    myNetwork = net.Network(IP_parameter)

    # this method to determine the class type by prefix // not accurate
    if myNetwork.prefix is not None:
        print(f"using prefix this is class {myNetwork.class_type()}")

    # this method run if only IP
    myNetwork.ip_type()
    print(f"IP designation is {myNetwork.designation_type}")
    print(f"IP is of Class {myNetwork.class_type}")


if __name__ == '__main__':
    pass
