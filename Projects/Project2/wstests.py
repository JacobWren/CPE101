# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   WordSearch Project
# Term:         Winter 2020


import wordsearch


assert wordsearch.forward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCF") == None
assert wordsearch.forward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TBO") == '6, 2'
assert wordsearch.forward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "FGO") == '1, 2'
assert wordsearch.forward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "NFJOP") == '4, 1'


assert wordsearch.backward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TND") == '0, 6'
assert wordsearch.backward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.backward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "OJF") == '4, 4'
assert wordsearch.backward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "POJ") == '4, 5'


assert wordsearch.upward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TRF") == '6, 2'
assert wordsearch.upward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.upward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "LIST") == '6, 6'
assert wordsearch.upward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "EIF") == '3, 2'


assert wordsearch.downward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.downward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "THK") == '0, 6'
assert wordsearch.downward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "LJS") == '3, 3'
assert wordsearch.downward("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "POB") == '3, 4'


assert wordsearch.DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "LNR") == '3, 0'
assert wordsearch.DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "PI") == '4, 5'
assert wordsearch.DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "SEIL") == '0, 0'
assert wordsearch.DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "DAK") == '0, 4'


assert wordsearch.DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "LIE") == '3, 3'
assert wordsearch.DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "OBJ") == '6, 5'
assert wordsearch.DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TJO") == '3, 6'
assert wordsearch.DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "SUOG") == '4, 6'


assert wordsearch.Rev_DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.Rev_DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "HJP") == '1, 6'
assert wordsearch.Rev_DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "NEN") == '2, 3'
assert wordsearch.Rev_DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "STO") == '4, 6'
assert wordsearch.Rev_DD("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "BER") == '0, 2'


assert wordsearch.Rev_DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ABCD") == None
assert wordsearch.Rev_DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "UNF") == '6, 0'
assert wordsearch.Rev_DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "BBP") == '6, 3'
assert wordsearch.Rev_DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "MIG") == '3, 1'
assert wordsearch.Rev_DU("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "UNFLOAT") == '6, 0'


assert wordsearch.DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "SEIL") == '0, 0'
assert wordsearch.DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TCEJ") == '1, 0'
assert wordsearch.DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "RMF") == '2, 0'


assert wordsearch.DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "AFNP") == '0, 1'
assert wordsearch.DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "BGOU") == '0, 2'
assert wordsearch.DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "COJT") == '0, 3'


assert wordsearch.DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "LIES") == '3, 3'
assert wordsearch.DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "ECT") == '3, 2'
assert wordsearch.DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "SFMR") == '5, 3'


assert wordsearch.DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "PNFA") == '3, 4'
assert wordsearch.DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "OGB") == '2, 4'
assert wordsearch.DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "JOC") == '2, 5'


assert wordsearch.Rev_DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "TAO") == '0, 6'
assert wordsearch.Rev_DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.Rev_DD_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "HJP") == '1, 6'


assert wordsearch.Rev_DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "NONE") == '0, 5'
assert wordsearch.Rev_DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.Rev_DD_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "DGI") == '0, 4'


assert wordsearch.Rev_DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "UNFL") == '6, 0'
assert wordsearch.Rev_DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.Rev_DU_left("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "PJH") == '3, 4'


assert wordsearch.Rev_DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "QNEN") == '5, 0'
assert wordsearch.Rev_DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "pr") == None
assert wordsearch.Rev_DU_right("SABCDNTTEFGOAHRCINOJKLMELPUTINFJOPSQNRSBTIUVTBOOL", "CFC") == '2, 1'
