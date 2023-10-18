import unittest

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

from exo2 import unit_tour

class Exo2Test(unittest.TestCase):

    def test_unit_tour(self):
        
        self.assertEqual(unit_tour(fixed_tests_True),True)
        self.assertEqual(unit_tour(fixed_tests_False),False)


a = Exo2Test()
a.test_unit_tour()