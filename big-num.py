step = 0
steprecord = []
n = (391581*(10**65086))-1

def collatz(i, s):
    s = 0
    while i != 1:
      steprecord.append(i)
	    if i%2==0:
          i=i/2
          s+=1
      else:
          i=3*i+1
          s+=1
    print "steps:", s

collatz(n, step)
