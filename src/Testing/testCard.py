#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

import unittest  	  	  

from Card import Card  	  	  
from RandNumberSet import RandNumberSet  	  	  


class TestCard(unittest.TestCase):  	  	  

    def setUp(self):  	  	  
        """  	  	  
        Create no fewer than 5 Card objects to test  	  	  

        Create a mixture of odd and even-sized cards  	  	  
        """
        self.ns15 = Card(1, RandNumberSet(15, 450))
        self.ns8 = Card(2, RandNumberSet(8, 200))
        self.ns3 = Card(3, RandNumberSet(3, 20))
        self.ns16 = Card(4, RandNumberSet(16, 600))
        self.ns12 = Card(5, RandNumberSet(12, 300))

    def test_len(self):  	  	  
        """Assert that each card's size is as expected"""
        self.assertEqual(len(self.ns15), 15)
        self.assertEqual(len(self.ns8), 8)
        self.assertEqual(len(self.ns3), 3)
        self.assertEqual(len(self.ns16), 16)
        self.assertEqual(len(self.ns12), 12)

    def test_id(self):  	  	  
        """Assert that each card's ID number is as expected"""
        self.assertEqual(self.ns15.getID(), 1)
        self.assertEqual(self.ns8.getID(), 2)
        self.assertEqual(self.ns3.getID(), 3)
        self.assertEqual(self.ns16.getID(), 4)
        self.assertEqual(self.ns12.getID(), 5)

    def test_freeSquares(self):  	# FAILING
        """  	  	  
        Ensure that odd-sized cards have 1 "Free!" square in the center  	  	  
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	  	  
        """
        self.assertEqual(self.ns15.numberAt(8 - 1, 8 - 1), -1)
        self.assertEqual(self.ns3.numberAt(2 - 1, 2 - 1), -1)

        for element in range(8):
            for i in range(8):
                self.assertNotEqual(self.ns8.numberAt(element, i), -1)
        for element in range(16):
            for i in range(16):
                self.assertNotEqual(self.ns16.numberAt(element, i), -1)
        for element in range(12):
            for i in range(12):
                self.assertNotEqual(self.ns12.numberAt(element, i), -1)

    def test_no_duplicates(self):
        """Ensure that Cards do not contain duplicate numbers"""
        seen = set()
        for element in range(15):
            for i in range(15):
                self.assertNotIn(self.ns15.numberAt(element, i), seen)
                seen.add(self.ns15.numberAt(element, i))
        seen = set()
        for element in range(8):
            for i in range(8):
                self.assertNotIn(self.ns8.numberAt(element, i), seen)
                seen.add(self.ns8.numberAt(element, i))
        seen = set()
        for element in range(3):
            for i in range(3):
                self.assertNotIn(self.ns3.numberAt(element, i), seen)
                seen.add(self.ns3.numberAt(element, i))
        seen = set()
        for element in range(16):
            for i in range(16):
                self.assertNotIn(self.ns16.numberAt(element, i), seen)
                seen.add(self.ns16.numberAt(element, i))
        seen = set()
        for element in range(12):
            for i in range(12):
                self.assertNotIn(self.ns12.numberAt(element, i), seen)
                seen.add(self.ns12.numberAt(element, i))


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
