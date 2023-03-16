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
from Deck import Deck  	  	  


class TestDeck(unittest.TestCase):  	  	  
    def setUp(self):  	  	  
        """  	  	  
        Create no fewer than 5 Deck objects to test  	  	  

        Create at least one Deck with the minimum number of Cards  	  	  
        Create at least one Deck with the maximum number of Cards  	  	  
        Create a mixture of large and small cards  	  	  
        """
        self.ns2 = Deck(16, 2, 600)
        self.ns8192 = Deck(3, 8192, 20)
        self.ns20 = Deck(5, 20, 60)
        self.ns1000 = Deck(14, 1000, 450)
        self.ns5 = Deck(12, 5, 300)

    def test_len(self):  	  	  
        """  	  	  
        Ensure that Decks contain the expected number of cards  	  	  
        """
        self.assertEqual(len(self.ns2), 2)
        self.assertEqual(len(self.ns8192), 8192)
        self.assertEqual(len(self.ns20), 20)
        self.assertEqual(len(self.ns1000), 1000)
        self.assertEqual(len(self.ns5), 5)

    def test_card(self):  	  	  
        """  	  	  
        Ensure that specific Cards can be accessed from within a Deck  	  	  

        Assert that requesting Cards at invalid indexes fails  	  	  
        """
        self.assertTrue(self.ns2.__getitem__, -1)
        self.assertTrue(self.ns8192.__getitem__, 8192)
        self.assertTrue(self.ns20.__getitem__, 10)
        # Asserting that requesting Cards at invalid indexes fails
        self.assertRaises(IndexError, self.ns2.__getitem__, -100)
        self.assertRaises(IndexError, self.ns1000.__getitem__, 1001)


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
