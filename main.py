def ways ( length ) :
    #Base Case(s)
    if length == 0:
        return 1
    if length < 0:
        return 0

    #Recursive Cases
    b = ways ( length - 1 , 'B')


    #Red Case
    r = ways()



    return b + r
print(ways(1))
#1) You can take two arguments, but it'll be simpler if you only take one.

#2) You use a/B/R inconsistently.

#3) Your red cases aren't quite thought out correctly.