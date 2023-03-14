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

class Card():  	  	  
    COLUMN_NAMES = list("BINGOLARDYPEZMUX")  	  	  

    def __init__(self, nId, randNumSet):  	  	  
        """  	  	  
        Initialize a Bingo! card  	  	  
        """
        pass  	  	  

    def getID(self):  	  	  
        """  	  	  
        Return an integer: the ID number of the card  	  	  
        """  	  	  
        pass  	  	  

    def numberAt(self, nRow, nCol):  	  	  
        """  	  	  
        Return an integer or a string: the value in the Bingo square at (nRow, nCol)  	  	  
        """  	  	  
        pass  	  	  

    def __len__(self):  	  	  
        """  	  	  
        Return an integer: the length of one dimension of the card.  	  	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	  	  

        This method was called `getSize` in the C++ version  	  	  
        """  	  	  
        pass  	  	  

    def __str__(self):  	  	  
        """  	  	  
        Return a string: a neatly formatted, square bingo card  	  	  

        This is basically equivalent to the `operator<<` method in the C++ version  	  	  
        """  	  	  
        pass  	  	  
