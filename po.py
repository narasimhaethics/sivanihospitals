import aiml
import sys
import json

#name = sys.stdin.readline()
def ab(abc):
    name = abc
    k = aiml.Kernel()


    k.learn("std-startup.xml")


    k.respond("load aiml b")



#while True: 
    x = k.respond(name)
    print (" ")
    print (x)
#sys.stdout.write(x)
    y = list(x.split(' '))



    c=dict((k,2) for k in y)




#dd = {'a':'1' ,'b':'2','c':'3'}

    with open('data.json', 'w') as outfile:  
        json.dump(x, outfile)
    return x


