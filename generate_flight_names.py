import random as r


if __name__ =='__main__':
    f=open("flight.csv","w")

    no_of_entries = 50


    fl = set()
    while len(fl)<no_of_entries:
        fl.add( r.randint(200,500))


    for i in fl:
        a = r.randint(5,10)      
        b = r.randint(9,13)
        c = "6E " + str(i) + "," + str(a) + "," + str(b) + "\n"
        f.write(c)
    print fl
    f.close()
