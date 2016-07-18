import string

alphas = string.letters + '_'
nums = string.digits

myInput = raw_input('a identifier:')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''"%s" is not alphabetic,
        frist symbol must be alphabetic''' % myInput[0]
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '''"%s" in "%s" index %d is not alphanumeric,remaining symbols must be alphanumeric
                '''%(otherChar,myInput,myInput.index(otherChar)+1)

