def evenlyDivisibleElement (x, y=list()):
    '''This function prints out the list of integers that
evenly divide an integer from a list of integer'''
    a = list()
    for i in range(len(y)):
        if x % y[i] == 0:
            a.append(y[i])
    return a
