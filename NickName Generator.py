import random
import time
threecons = False
threea = False
twoa = False
threeonecons = False
threetwocons = False
twostartabnumber = 0
foura = False
fourcons = False
fivea = False
fivecons = False
fivetwocons = False
sixtwocons = False
sixa = False
sixcons = False
sixtwoa = False
fourtwocons = False
fourabnumber = 0
startabnumber = random.randint(1, 2)
if startabnumber == 1:
    onenumber = random.randint(1, 5)
    if onenumber == 1:
        oneletter = 'a'
    if onenumber == 2:
        oneletter = 'e'
    if onenumber == 3:
        oneletter = "i"
    if onenumber == 4:
        oneletter = "o"
    if onenumber == 5:
        oneletter = "u"
if startabnumber == 2:
    onenumber = random.randint(1, 21)
    if onenumber == 1:
        oneletter = "b"
    if onenumber == 2:
        oneletter = "c"
    if onenumber == 3:
        oneletter = "d"
    if onenumber == 4:
        oneletter = "f"
    if onenumber == 5:
        oneletter = "g"
    if onenumber == 6:
        oneletter = "h"
    if onenumber == 7:
        oneletter = "j"
    if onenumber == 8:
        oneletter = "k"
    if onenumber == 9:
        oneletter = "l"
    if onenumber == 10:
        oneletter = "m"
    if onenumber == 11:
        oneletter = "n"
    if onenumber == 12:
        oneletter = "p"
    if onenumber == 13:
        oneletter = "q"
    if onenumber == 14:
        oneletter = "r"
    if onenumber == 15:
        oneletter = "s"
    if onenumber == 16:
        oneletter = "t"
    if onenumber == 17:
        oneletter = "v"
    if onenumber == 18:
        oneletter = "w"
    if onenumber == 19:
        oneletter = "x"
    if onenumber == 20:
        oneletter = "y"
    if onenumber == 21:
        oneletter = "z"



if startabnumber == 1:
    if onenumber > 0:
        twostartabnumber = random.randint(1, 6)
        if twostartabnumber == 1:
            twonumber = random.randint(1, 5)
            if twonumber == 5:
                twoletter = "a"
            if twonumber == 1:
                twoletter = 'e'
            if twonumber == 2:
                twoletter = 'i'
            if twonumber == 3:
                twoletter = 'o'
            if twonumber == 4:
                twoletter = 'u'
        if twostartabnumber > 1:
            twonumber = random.randint(1, 21)
            if twonumber == 1:
                twoletter = "b"
            if twonumber == 2:
                twoletter = "c"
            if twonumber == 3:
                twoletter = "d"
            if twonumber == 4:
                twoletter = "f"
            if twonumber == 5:
                twoletter = "g"
            if twonumber == 6:
                twoletter = "h"
            if twonumber == 7:
                twoletter = "j"
            if twonumber == 8:
                twoletter = "k"
            if twonumber == 9:
                twoletter = "l"
            if twonumber == 10:
                twoletter = "m"
            if twonumber == 11:
                twoletter = "n"
            if twonumber == 12:
                twoletter = "p"
            if twonumber == 13:
                twoletter = "q"
            if twonumber == 14:
                twoletter = "r"
            if twonumber == 15:
                twoletter = "s"
            if twonumber == 16:
                twoletter = "t"
            if twonumber == 17:
                twoletter = "v"
            if twonumber == 18:
                twoletter = "w"
            if twonumber == 19:
                twoletter = "x"
            if twonumber == 20:
                twoletter = "y"
            if twonumber == 21:
                twoletter = "z"

if startabnumber == 2:
    twoa = True
    if onenumber < 14:
        twonumber = random.randint(1, 5)
        if twonumber == 1:
            twoletter = "a"
        if twonumber == 2:
            twoletter = "e"
        if twonumber == 3:
            twoletter = "i"
        if twonumber == 4:
            twoletter = "o"
        if twonumber == 5:
            twoletter = "u"

    if onenumber == 14:
        twonumber = random.randint(1, 6)
        if twonumber == 1:
            twoletter = "a"
        if twonumber == 2:
            twoletter = "e"
        if twonumber == 3:
            twoletter = "i"
        if twonumber == 4:
            twoletter = "o"
        if twonumber == 5:
            twoletter = "u"
        if twonumber == 6:
            twoletter = "r"

    if onenumber == 15:
        twonumber = random.randint(1, 7)
        if twonumber == 1:
            twoletter = "a"
        if twonumber == 2:
            twoletter = "e"
        if twonumber == 3:
            twoletter = "i"
        if twonumber == 4:
            twoletter = "o"
        if twonumber == 5:
            twoletter = "u"
        if twonumber == 6:
            twoletter = "s"
        if twonumber == 7:
            twoletter = "h"

    if onenumber > 15:
        twonumber = random.randint(1, 5)
        if twonumber == 1:
            twoletter = "a"
        if twonumber == 2:
            twoletter = "e"
        if twonumber == 3:
            twoletter = "i"
        if twonumber == 4:
            twoletter = "o"
        if twonumber == 5:
            twoletter = "u"


if twoa == True:
    threenumber = random.randint(1, 21)
    threecons = True
    if threenumber == 1:
        threeletter = "b"
    if threenumber == 2:
        threeletter = "c"
    if threenumber == 3:
        threeletter = "d"
    if threenumber == 4:
        threeletter = "f"
    if threenumber == 5:
        threeletter = "g"
    if threenumber == 6:
        threeletter = "h"
    if threenumber == 7:
        threeletter = "j"
    if threenumber == 8:
        threeletter = "k"
    if threenumber == 9:
        threeletter = "l"
    if threenumber == 10:
        threeletter = "m"
    if threenumber == 11:
        threeletter = "n"
    if threenumber == 12:
        threeletter = "p"
    if threenumber == 13:
        threeletter = "q"
    if threenumber == 14:
        threeletter = "r"
    if threenumber == 15:
        threeletter = "s"
    if threenumber == 16:
        threeletter = "t"
    if threenumber == 17:
        threeletter = "v"
    if threenumber == 18:
        threeletter = "w"
    if threenumber == 19:
        threeletter = "x"
    if threenumber == 20:
        threeletter = "y"
    if threenumber == 21:
        threeletter = "z"

if twostartabnumber == 1:
    threenumber = random.randint(1, 21)
    threecons = True
    if threenumber == 1:
        threeletter = "b"
    if threenumber == 2:
        threeletter = "c"
    if threenumber == 3:
        threeletter = "d"
    if threenumber == 4:
        threeletter = "f"
    if threenumber == 5:
        threeletter = "g"
    if threenumber == 6:
        threeletter = "h"
    if threenumber == 7:
        threeletter = "j"
    if threenumber == 8:
        threeletter = "k"
    if threenumber == 9:
        threeletter = "l"
    if threenumber == 10:
        threeletter = "m"
    if threenumber == 11:
        threeletter = "n"
    if threenumber == 12:
        threeletter = "p"
    if threenumber == 13:
        threeletter = "q"
    if threenumber == 14:
        threeletter = "r"
    if threenumber == 15:
        threeletter = "s"
    if threenumber == 16:
        threeletter = "t"
    if threenumber == 17:
        threeletter = "v"
    if threenumber == 18:
        threeletter = "w"
    if threenumber == 19:
        threeletter = "x"
    if threenumber == 20:
        threeletter = "y"
    if threenumber == 21:
        threeletter = "z"

if twostartabnumber > 1:
    if twonumber < 14:
        threenumber = random.randint(1, 5)
        if threenumber == 1:
            threeletter = "a"
        if threenumber == 2:
            threeletter = "e"
        if threenumber == 3:
            threeletter = "i"
        if threenumber == 4:
            threeletter = "o"
        if threenumber == 5:
            threeletter = "u"
    
    if twonumber == 14:
        threenumber = random.randint(1, 6)
        if threenumber == 1:
            threeletter = "a"
        if threenumber == 2:
            threeletter = "e"
        if threenumber == 3:
            threeletter = "i"
        if threenumber == 4:
            threeletter = "o"
        if threenumber == 5:
            threeletter = "u"
        if threenumber == 6:
            threeletter = "r"

    if twonumber == 15:
        threenumber = random.randint(1, 7)
        if threenumber == 1:
            threeletter = "a"
        if threenumber == 2:
            threeletter = "e"
        if threenumber == 3:
            threeletter = "i"
        if threenumber == 4:
            threeletter = "o"
        if threenumber == 5:
            threeletter = "u"
        if threenumber == 6:
            threeletter = "s"
        if threenumber == 7:
            threeletter = "h"
        
    if twonumber > 15:
        threenumber = random.randint(1, 5)
        if threenumber == 1:
            threeletter = "a"
        if threenumber == 2:
            threeletter = "e"
        if threenumber == 3:
            threeletter = "i"
        if threenumber == 4:
            threeletter = "o"
        if threenumber == 5:
            threeletter = "u"
    
    if threenumber < 6:
        threea = True

    if threenumber > 5:
        threetwocons = True



if threecons == True:
    if threenumber == 1:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 2:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 3:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 4:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 5:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 6:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 7:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"
    
    if threenumber == 8:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 9:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 10:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 11:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 12:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 13:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 14:
        fournumber = random.randint(1, 6)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"
        if fournumber == 6:
            fourletter = "r"

    if threenumber == 15:
        fournumber = random.randint(1, 7)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"
        if fournumber == 6:
            fourletter = "s"
        if fournumber == 7:
            fourletter = "h"

    if threenumber == 16:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 17:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 18:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 19:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 20:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if threenumber == 21:
        fournumber = random.randint(1, 5)
        if fournumber == 1:
            fourletter = "a"
        if fournumber == 2:
            fourletter = "e"
        if fournumber == 3:
            fourletter = "i"
        if fournumber == 4:
            fourletter = "o"
        if fournumber == 5:
            fourletter = "u"

    if fournumber < 6:
        foura = True
    if fournumber > 5:
        fourtwocons = True

if threea == True:
    fourcons = True
    fournumber = random.randint(1, 21)
    if fournumber == 1:
        fourletter = "b"
    if fournumber == 2:
        fourletter = "c"
    if fournumber == 3:
        fourletter = "d"
    if fournumber == 4:
        fourletter = "f"
    if fournumber == 5:
        fourletter = "g"
    if fournumber == 6:
        fourletter = "h"
    if fournumber == 7:
        fourletter = "j"
    if fournumber == 8:
        fourletter = "k"
    if fournumber == 9:
        fourletter = "l"
    if fournumber == 10:
        fourletter = "m"
    if fournumber == 11:
        fourletter = "n"
    if fournumber == 12:
        fourletter = "p"
    if fournumber == 13:
        fourletter = "q"
    if fournumber == 14:
        fourletter = "r"
    if fournumber == 15:
        fourletter = "s"
    if fournumber == 16:
        fourletter = "t"
    if fournumber == 17:
        fourletter = "v"
    if fournumber == 18:
        fourletter = "w"
    if fournumber == 19:
        fourletter = "x"
    if fournumber == 20:
        fourletter = "y"
    if fournumber == 21:
        fourletter = "z"


if threetwocons == True:
    foura = True
    fournumber = random.randint(1, 5)
    if fournumber == 1:
        fourletter = "a"
    if fournumber == 2:
        fourletter = "e"
    if fournumber == 3:
        fourletter = "i"
    if fournumber == 4:
        fourletter = "o"
    if fournumber == 5:
        fourletter = "u"


if foura == True:
    fiveabnumber = random.randint(1, 6)
    if fiveabnumber > 1:
        fivecons = True
        fivenumber = random.randint(1, 21)
        if fivenumber == 1:
            fiveletter = "b"
        if fivenumber == 2:
            fiveletter = "c"
        if fivenumber == 3:
            fiveletter = "d"
        if fivenumber == 4:
            fiveletter = "f"
        if fivenumber == 5:
            fiveletter = "g"
        if fivenumber == 6:
            fiveletter = "h"
        if fivenumber == 7:
            fiveletter = "j"
        if fivenumber == 8:
            fiveletter = "k"
        if fivenumber == 9:
            fiveletter = "l"
        if fivenumber == 10:
            fiveletter = "m"
        if fivenumber == 11:
            fiveletter = "n"
        if fivenumber == 12:
            fiveletter = "p"
        if fivenumber == 13:
            fiveletter = "q"
        if fivenumber == 14:
            fiveletter = "r"
        if fivenumber == 15:
            fiveletter = "s"
        if fivenumber == 16:
            fiveletter = "t"
        if fivenumber == 17:
            fiveletter = "v"
        if fivenumber == 18:
            fiveletter = "w"
        if fivenumber == 19:
            fiveletter = "x"
        if fivenumber == 20:
            fiveletter = "y"
        if fivenumber == 21:
            fiveletter = "z"
    if fiveabnumber == 1:
        fivea = True
        fivenumber = random.randint(1, 5)
        if fivenumber == 1:
            fiveletter = "a"
        if fivenumber == 2:
            fiveletter = "e"
        if fivenumber == 3:
            fiveletter = "i"
        if fivenumber == 4:
            fiveletter = "o"
        if fivenumber == 5:
            fiveletter = "u"

if fourcons == True:
    if fournumber < 14:
        fivenumber = random.randint(1, 5)
        if fivenumber == 1:
            fiveletter = "a"
        if fivenumber == 2:
            fiveletter = "e"
        if fivenumber == 3:
            fiveletter = "i"
        if fivenumber == 4:
            fiveletter = "o"
        if fivenumber == 5:
            fiveletter = "u"

    if fournumber == 14:
        fivenumber = random.randint(1, 6)
        if fivenumber == 1:
            fiveletter = "a"
        if fivenumber == 2:
            fiveletter = "e"
        if fivenumber == 3:
            fiveletter = "i"
        if fivenumber == 4:
            fiveletter = "o"
        if fivenumber == 5:
            fiveletter = "u"
        if fivenumber == 6:
            fiveletter = "r"

    if fournumber == 15:
        fivenumber = random.randint(1, 7)
        if fivenumber == 1:
            fiveletter = "a"
        if fivenumber == 2:
            fiveletter = "e"
        if fivenumber == 3:
            fiveletter = "i"
        if fivenumber == 4:
            fiveletter = "o"
        if fivenumber == 5:
            fiveletter = "u"
        if fivenumber == 6:
            fiveletter = "s"
        if fivenumber == 7:
            fiveletter = "h"

    if fournumber > 15:
        fivenumber = random.randint(1, 5)
        if fivenumber == 1:
            fiveletter = "a"
        if fivenumber == 2:
            fiveletter = "e"
        if fivenumber == 3:
            fiveletter = "i"
        if fivenumber == 4:
            fiveletter = "o"
        if fivenumber == 5:
            fiveletter = "u"

    if fivenumber > 5:
        fivetwocons = True
    if fivenumber < 6:
        fivea = True

if fourtwocons == True:
    fivea = True
    fivenumber = random.randint(1, 5)
    if fivenumber == 1:
        fiveletter = "a"
    if fivenumber == 2:
        fiveletter = "e"
    if fivenumber == 3:
        fiveletter = "i"
    if fivenumber == 4:
        fiveletter = "o"
    if fivenumber == 5:
        fiveletter = "u"



if fivecons == True:
    if fivenumber < 14:
        sixnumber = random.randint(1, 5)
        if sixnumber == 1:
            sixletter = "a"
        if sixnumber == 2:
            sixletter = "e"
        if sixnumber == 3:
            sixletter = "i"
        if sixnumber == 4:
            sixletter = "o"
        if sixnumber == 5:
            sixletter = "u"

    if fivenumber == 14:
        sixnumber = random.randint(1, 6)
        if sixnumber == 1:
            sixletter = "a"
        if sixnumber == 2:
            sixletter = "e"
        if sixnumber == 3:
            sixletter = "i"
        if sixnumber == 4:
            sixletter = "o"
        if sixnumber == 5:
            sixletter = "u"
        if sixnumber == 6:
            sixletter = "r"

    if fivenumber == 15:
        sixnumber = random.randint(1, 7)
        if sixnumber == 1:
            sixletter = "a"
        if sixnumber == 2:
            sixletter = "e"
        if sixnumber == 3:
            sixletter = "i"
        if sixnumber == 4:
            sixletter = "o"
        if sixnumber == 5:
            sixletter = "u"
        if sixnumber == 6:
            sixletter = "s"
        if sixnumber == 7:
            sixletter = "h"
    
    if fivenumber > 15:
        sixnumber = random.randint(1, 5)
        if sixnumber == 1:
            sixletter = "a"
        if sixnumber == 2:
            sixletter = "e"
        if sixnumber == 3:
            sixletter = "i"
        if sixnumber == 4:
            sixletter = "o"
        if sixnumber == 5:
            sixletter = "u"

    if sixnumber < 6:
        sixa = True
    if sixnumber > 5:
        sixtwocons = True
    

if fivetwocons == True:
    sixa = True
    sixnumber = random.randint(1, 5)
    if sixnumber == 1:
        sixletter = "a"
    if sixnumber == 2:
        sixletter = "e"
    if sixnumber == 3:
        sixletter = "i"
    if sixnumber == 4:
        sixletter = "o"
    if sixnumber == 5:
        sixletter = "u"

if fivea == True:
    sixabnumber = random.randint(1, 6)
    if sixabnumber == 1:
        sixtwoa = True
        sixnumber = random.randint(1, 5)
        if sixnumber == 1:
            sixletter = "a"
        if sixnumber == 2:
            sixletter = "e"
        if sixnumber == 3:
            sixletter = "i"
        if sixnumber == 4:
            sixletter = "o"
        if sixnumber == 5:
            sixletter = "u"

    if sixabnumber > 1:
        sixnumber = random.randint(1, 21)
        sixcons = True
        if sixnumber == 1:
            sixletter = "b"
        if sixnumber == 2:
            sixletter = "c"
        if sixnumber == 3:
            sixletter = "d"
        if sixnumber == 4:
            sixletter = "f"
        if sixnumber == 5:
            sixletter = "g"
        if sixnumber == 6:
            sixletter = "h"
        if sixnumber == 7:
            sixletter = "j"
        if sixnumber == 8:
            sixletter = "k"
        if sixnumber == 9:
            sixletter = "l"
        if sixnumber == 10:
            sixletter = "m"
        if sixnumber == 11:
            sixletter = "n"
        if sixnumber == 12:
            sixletter = "p"
        if sixnumber == 13:
            sixletter = "q"
        if sixnumber == 14:
            sixletter = "r"
        if sixnumber == 15:
            sixletter = "s"
        if sixnumber == 16:
            sixletter = "t"
        if sixnumber == 17:
            sixletter = "v"
        if sixnumber == 18:
            sixletter = "w"
        if sixnumber == 19:
            sixletter = "x"
        if sixnumber == 20:
            sixletter = "y"
        if sixnumber == 21:
            sixletter = "z"


if sixa == True:
    sevenabnumber = random.randint(1, 6)
    if sevenabnumber == 1:
        sevennumber = random.randint(1, 5)
        if sevennumber == 1:
            sevenletter = "a"
        if sevennumber == 2:
            sevenletter = "e"
        if sevennumber == 3:
            sevenletter = "i"
        if sevennumber == 4:
            sevenletter = "o"
        if sevennumber == 5:
            sevenletter = "u"
    
    if sevenabnumber > 1:
        sevennumber = random.randint(1, 21)
        if sevennumber == 1:
            sevenletter = "b"
        if sevennumber == 2:
            sevenletter = "c"
        if sevennumber == 3:
            sevenletter = "d"
        if sevennumber == 4:
            sevenletter = "f"
        if sevennumber == 5:
            sevenletter = "g"
        if sevennumber == 6:
            sevenletter = "h"
        if sevennumber == 7:
            sevenletter = "j"
        if sevennumber == 8:
            sevenletter = "k"
        if sevennumber == 9:
            sevenletter = "l"
        if sevennumber == 10:
            sevenletter = "m"
        if sevennumber == 11:
            sevenletter = "n"
        if sevennumber == 12:
            sevenletter = "p"
        if sevennumber == 13:
            sevenletter = "q"
        if sevennumber == 14:
            sevenletter = "r"
        if sevennumber == 15:
            sevenletter = "s"
        if sevennumber == 16:
            sevenletter = "t"
        if sevennumber == 17:
            sevenletter = "v"
        if sevennumber == 18:
            sevenletter = "w"
        if sevennumber == 19:
            sevenletter = "x"
        if sevennumber == 20:
            sevenletter = "y"
        if sevennumber == 21:
            sevenletter = "z"

if sixtwoa == True:
    sevennumber = random.randint(1, 21)
    if sevennumber == 1:
        sevenletter = "b"
    if sevennumber == 2:
        sevenletter = "c"
    if sevennumber == 3:
        sevenletter = "d"
    if sevennumber == 4:
        sevenletter = "f"
    if sevennumber == 5:
        sevenletter = "g"
    if sevennumber == 6:
        sevenletter = "h"
    if sevennumber == 7:
        sevenletter = "j"
    if sevennumber == 8:
        sevenletter = "k"
    if sevennumber == 9:
        sevenletter = "l"
    if sevennumber == 10:
        sevenletter = "m"
    if sevennumber == 11:
        sevenletter = "n"
    if sevennumber == 12:
        sevenletter = "p"
    if sevennumber == 13:
        sevenletter = "q"
    if sevennumber == 14:
        sevenletter = "r"
    if sevennumber == 15:
        sevenletter = "s"
    if sevennumber == 16:
        sevenletter = "t"
    if sevennumber == 17:
        sevenletter = "v"
    if sevennumber == 18:
        sevenletter = "w"
    if sevennumber == 19:
        sevenletter = "x"
    if sevennumber == 20:
        sevenletter = "y"
    if sevennumber == 21:
        sevenletter = "z"

if sixcons == True:
    if sixnumber < 14:
        sevennumber = random.randint(1, 5)
        if sevennumber == 1:
            sevenletter = "a"
        if sevennumber == 2:
            sevenletter = "e"
        if sevennumber == 3:
            sevenletter = "i"
        if sevennumber == 4:
            sevenletter = "o"
        if sevennumber == 5:
            sevenletter = "u"

    if sixnumber == 14:
        sevennumber = random.randint(1, 6)
        if sevennumber == 1:
            sevenletter = "a"
        if sevennumber == 2:
            sevenletter = "e"
        if sevennumber == 3:
            sevenletter = "i"
        if sevennumber == 4:
            sevenletter = "o"
        if sevennumber == 5:
            sevenletter = "u"
        if sevennumber == 6:
            sevenletter = "r"

    if sixnumber == 15:
        sevennumber = random.randint(1, 7)
        if sevennumber == 1:
            sevenletter = "a"
        if sevennumber == 2:
            sevenletter = "e"
        if sevennumber == 3:
            sevenletter = "i"
        if sevennumber == 4:
            sevenletter = "o"
        if sevennumber == 5:
            sevenletter = "u"
        if sevennumber == 6:
            sevenletter = "s"
        if sevennumber == 7:
            sevenletter = "h"

    if sixnumber > 15:
        sevennumber = random.randint(1, 5)
        if sevennumber == 1:
            sevenletter = "a"
        if sevennumber == 2:
            sevenletter = "e"
        if sevennumber == 3:
            sevenletter = "i"
        if sevennumber == 4:
            sevenletter = "o"
        if sevennumber == 5:
            sevenletter = "u"

if sixtwocons == True:
    sevennumber = random.randint(1, 5)
    if sevennumber == 1:
        sevenletter = "a"
    if sevennumber == 2:
        sevenletter = "e"
    if sevennumber == 3:
        sevenletter = "i"
    if sevennumber == 4:
        sevenletter = "o"
    if sevennumber == 5:
        sevenletter = "u"


quantletter = int(input("Pick a number between 3 and 7 (that will be the number of letters in the username): "))
if quantletter == 3:
    print(oneletter + twoletter + threeletter)
if quantletter == 4:
    print(oneletter + twoletter + threeletter + fourletter)
if quantletter == 5:
    print(oneletter + twoletter + threeletter + fourletter + fiveletter)
if quantletter == 6:
    print(oneletter + twoletter + threeletter + fourletter + fiveletter + sixletter)
if quantletter == 7:
    print(oneletter + twoletter + threeletter + fourletter + fiveletter + sixletter + sevenletter)
print("The word above is the generated nickname, the program will close in 60 seconds")
time.sleep(60)
