import random as r

place_names = ["Delhi","Bombay","Cape Town", "Dubai","Sri Lanka",  "London", "New York", "Indore", "Tokyo", "Sydney","Lucknow",
                "Georgia","Beijing","California","Hong Kong","Shanghai"]


if __name__ =='__main__':
    f=open("route.csv","w")

    no_of_entries = 100000
    max_entry = 15 #no of flights
    max_hop = 10 #no of hops
    min_hop = 7 #no of hops

    for _ in range(no_of_entries):

        hops = r.randint(min_hop,max_hop)
        route = set()
        while len(route)<hops+1:
            route.add(place_names[r.randint(1,max_entry)])
        route =",".join(route)
        f.write(route+"\n")
    f.close()
