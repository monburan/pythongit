from random import randint

print "This program will make a number(1~100)"
print "try to hit this number..."

randint_num = randint(1,100)
bingo = 2

while bingo == 2:

    input_num = raw_input(The number you want:)

	if (randint_num == int(input_num)):
	    print "congratulation! this number is %d"%(int(input_num))
            bingo = 1

        if (randint_num != int(input_num)):
	    if (randint_num < int(input_num)):
	    	print "warning ! this number too big..."
    	    else:
		print "warning ! this number too small..."
