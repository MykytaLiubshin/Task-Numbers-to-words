def create_dict():
    """
    create_dict(,/) takes nothing,
    returns a dict object, that has a representing of all the fundamental numers
    as a numeric value and as a word (sequence)
    """
    numdic = {
                "0":" zero ",
                "1":" one ",
                "2":" two ",
                "3":" three ",
                "4":" four",
                "5":" five",
                "6":" six",
                "7":" seven",
                "8":" eight",
                "9":" nine",
                "10":" ten ",
                "11":" eleven ",
                "12":" twelve ",
                "13":" thirteen ",
                "15":" fifteen ",
                "18":" eighteen ",
                "20":" twenty " ,
                "30":" thirty ",
                "50":" fifty ",
                "80":" eighty ",
                "100":" hundred ",
            }

    for i in range(2,10):
        if i > 3 and i not in [5,8]:
            numdic["1"+str(i)] = str(numdic[str(i)]+"teen")
            numdic[str(i)+"0"] = str(numdic[str(i)]+"ty")
        numdic[str(i)+"00"] = str(numdic[str(i)]+" "+ numdic["100"]+"s")
    numdic["100"] = "one " + numdic["100"]
    return numdic
    
def create_dict_s():
    """
    create_dict_s(,/) takes nothing,
    returns a dict object, that has a representing of all the needed symbols
    as a symbolic value and as a word (sequence)
    """
    sim = {
        # This is a dictionary w/ all the needed symbols
        "+":" plus ",
        "-":" minus ",
        "=":" equals ",
        "/":" divided by ",
        "*":" multyplied with ",
        " ":" ",
    }
    return sim