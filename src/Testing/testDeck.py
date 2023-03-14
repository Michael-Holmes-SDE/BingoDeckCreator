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
        self.assertTrue(False, "TODO: implement this test")  	  	  

    def test_len(self):  	  	  
        """  	  	  
        Ensure that Decks contain the expected number of cards  	  	  
        """  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  

    def test_card(self):  	  	  
        """  	  	  
        Ensure that specific Cards can be accessed from within a Deck  	  	  

        Assert that requesting Cards at invalid indexes fails  	  	  
        """  	  	  
        self.assertTrue(False, "TODO: implement this test")  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
