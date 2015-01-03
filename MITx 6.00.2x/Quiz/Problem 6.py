def probTest(limit):
    n = 1
    
    while (5/float(6))**(n-1)*1/6 >= limit:
        n+=1

    return n
