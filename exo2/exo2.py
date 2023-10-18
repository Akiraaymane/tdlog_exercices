"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
import sys
def unit_tour(liste):
    a=0
    for list in liste :
        if len(list[0])<len(list[1]):
            return(False)
            sys.exit()
        else:
            for i in range(len(list[1])):
                if list[0][-1-i]== list[1][-1-i]:
                    a=a+1
    c=0
    for list in liste:
        c=c+len(list[1]) 
    if a==c:
        return(True)
    else:
        return(False)                   
    

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)


#print(fixed_tests_False[0][1][-1])
#print(unit_tour(fixed_tests_True))