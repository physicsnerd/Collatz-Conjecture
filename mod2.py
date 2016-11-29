n = []
step = 0

def lstfill(nb,ne,lst):
    while nb <= ne:
        lst.append(nb)
        nb+=1

def collatz(n, s):
    for i in n:
        s = 0
        print "starting #", i
        while i != 1:
            if i%2==0:
                i=i/2
                s+=1
                print i
                print "mod:", i%2
            else:
                i=3*i+1
                s+=1
                print i
                print "mod:", i%2
        print "steps:", s

lstfill(3,6,n)
collatz(n, step)
