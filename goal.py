"""this is a football game"""
from random import choice

you_score = 0
com_score = 0

n = input()
def soccregame(n,you_score,com_score):
    for i in range(n):
        print '##### this is round %d #####'%(i+1)
        print '##### score is %d : %d  #####'%(you_score , com_score)
        print ' left | center | right '
        you = raw_input()
        print 'you choice:' + you
        direction = ['left','center','right']
        com = choice(direction)
        print 'computer choice:' + com
        if you != com:
            print 'goal !!!'
            you_score += 1
        else :
            print 'oops ...'
        if you_score >= com_score:
            print '%d : %d you win!'%(you_score , com_score)
        else :
            print '%d : %d you lose!'%(you_score , com_score)

while (you_score == com_score):
    soccregame(n,you_score,com_score)
