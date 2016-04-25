#! /usr/bin/python

for i in range(1, 101):
        if i%3==0:
                if i%5 == 0:
                        print 'fizzbuzz'

                else:# will only print if not disible by 5 
                        print 'fizz'

        elif i%5 == 0: # if disivible by 5 
                print 'buzz'

        else: # Anything that was not divisible
                print i
