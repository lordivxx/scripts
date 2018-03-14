#!/usr/bin/env python



# Beast game by Charles Forsyth 2017
# Use and advancement of the IVXX Class

####### Load modules ##########
import time
import os
import sys
import random



def fight(bhp,batk,bdef,mhp,matk,mdef):
    while bhp > 0 and mhp > 0:
        #battack = random.randint(1, int(batk))
        #mattack = random.randint(1, int(matk))
        #bdef = random.randint(1, int(bdef))
        #mdef = random.randint(1, int(mdef))

        bhp = int(bhp) - random.randint(1, int(matk)) + random.randint(1, int(bdef))
        mhp = int(mhp) - random.randint(1, int(batk)) + random.randint(1, int(mdef))
        #bhp = int(bhp) - mattack + bdef
        #mhp = int(mhp) - battack + mdef
        
        if bhp > mhp:
           
           winning = "Beast"
           howmuch = bhp - mhp

        if mhp > bhp:

           winning = "Monster"
           howmuch = mhp - bhp
           
        howmuchlen = len(str(howmuch))
        howmuch = howmuch / howmuchlen
        
        #print (str(bhp),str(mhp),winning + "by" + str(howmuch)) 
        
        #os.system('clear')
        #sys.stdout.write("\r")
        #print winning + " by " + str(howmuch) 
        #sys.stdout.write("[%-20s]" % ('='*howmuch))
        #sys.stdout.write("[%-20s] %d%%" % ('='*howmuch, 5*howmuch))

        #sys.stdout.flush()
        #time.sleep(0.25)
    return bhp,mhp




print (fight(10000,25,25,10000,25,25))
