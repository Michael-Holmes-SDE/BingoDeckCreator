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
import math

class Card():


    def __init__(self, nId, randNumSet):  	  	  
        """  	  	  
        Initialize a Bingo! card  	  	  
        """
        self.__m_nId = nId
        self.__m_arrNums = []
        self.__m_randNumSet = randNumSet
        self.__m_randNumSet.shuffle()
        randNums = "Let's get numbers"
        while randNums != None:
            numToAdd = self.__m_randNumSet.getNextRow()
            if numToAdd != None:
                self.__m_arrNums.append(numToAdd)
            randNums = numToAdd

    def getID(self):
        return self.__m_nId

    def numberAt(self, nRow, nCol):  	  	  
        """  	  	  
        Return an integer or a string: the value in the Bingo square at (nRow, nCol)  	  	  
        """
        length = self.__len__() ** 2
        if length % 2 != 0:
            element = math.ceil(self.__len__() / 2)
            i = math.ceil(self.__len__() / 2)
            self.__m_arrNums[element - 1][i - 1] = -1
        return self.__m_arrNums[nRow][nCol]

    def __len__(self):  	  	  
        """  	  	  
        Return an integer: the length of one dimension of the card.  	  	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	  	  

        This method was called `getSize` in the C++ version  	  	  
        """
        return len(self.__m_arrNums)

    def __str__(self):
        """  	  	  
        Return a string: a neatly formatted, square bingo card  	  	  

        This is basically equivalent to the `operator<<` method in the C++ version  	  	  
        """
        COLUMN_NAMES = list("BINGOLARDYPEZMUX")
        returnString = ""
        returnString += f"Card {self.getID()}\n"
        printDivider = "\n+" + ("-----+" * len(self))
        for element in range(len(self)):
            returnString += f"   {COLUMN_NAMES[element]}  "
        returnString += printDivider
        for element in range(len(self)):
            for i in range(len(self)):
                if i == 0:
                    returnString += "\n|"
                if self.numberAt(element, i) > 0:
                    returnString += "{:^5}|".format(self.numberAt(element, i))
                elif self.numberAt(element, i) < 0:
                    returnString += "FREE!|"
                if i == len(self) - 1:
                    returnString += printDivider
        returnString += "\n"
        return returnString
