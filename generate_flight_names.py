import random as r

# place_names = ["Delhi","Bombay","Cape Town", "Dubai","Sri Lanka",  "London", "New York", "Indore", "Tokyo", "Sydney","Lucknow",
#                 "Georgia","Beijing","California","Hong Kong","Shanghai"]


if __name__ =='__main__':
    f=open("flight.csv","w")

    no_of_entries = 50
    # max_entry = 15 #no of flights
    # max_hop = 10 #no of hops
    # min_hop = 7 #no of hops

    # for _ in range(no_of_entries):


    fl = set()
    while len(fl)<no_of_entries:
        fl.add( r.randint(200,500))

    # data = list()
    for i in fl:
        a = r.randint(5,10)      # value*10^4
        b = r.randint(9,13)
        c = "6E " + str(i) + "," + str(a) + "," + str(b) + "\n"
        f.write(c)
    print fl
    f.close()
