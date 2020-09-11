def ways ( length , prev = 'a') :
    #Base Case(s)
    if length == 0:
        return 1
    if length < 0:
        return 0

    #Recursive Cases
    b = ways ( length - 1 , 'B')


    #Red Case
    if prev != 'R':
        r = ways ( length - 1 , 'R')
    else:
        r = ways ( length - 3,  'R')



    return b + r, b, r
print(ways(1))