import sys

count = len(sys.argv)



if sys.argv[1] < '128' :
    print (' class : A'+ '\n' +'designation : public')
elif sys.argv[1] < '192' :
    print (' class : B'+ '\n' +'designation : private')
elif sys.argv[1] < '224' :
    print (' class : C'+ '\n' +'designation : private')
elif sys.argv[1] < '240' :
    print (' class : D'+ '\n' +'designation : private')
