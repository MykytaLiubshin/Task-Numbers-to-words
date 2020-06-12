from dicts import create_dict,create_dict_s
from re import sub

NUMBERS = create_dict()
SYMBOLS = create_dict_s()
ALPHA = "1234567890+-*/= "

def splitting(string):
    """
    splitting(string,/)
    takes a string
    returns it splitted by it's symbols and the set of symbols
    """
    s = list(filter( lambda x: x in SYMBOLS , string))

    for i in s:
        string = ' '.join(string.split(str(i)))
    return string.split(' '),s

def sym_to_word(string):

    """
    sym_to_word(string,/)
    converter takes a list 
    returns a string, that has all of it's
    symbols replaced with words
    """

    return list( map( lambda x: SYMBOLS[str(x)] if x in SYMBOLS else x, string ) )

def check_spec(num):
    """
    check_spec(num,/) 
    takes a string,
    returns a string, with number combinations 10,1 - 10,9
    replaced with their representing from 10 to 19
    e.g. 10,7 -> 17
    """
    h = [str(10+i) for i in range(10)]
    if len(num)>1:
        if num[-2]+num[-1] in h:
            num[-2]+=num[-1]
            del num[-1]
    return num

def zeroing(num,leng,numset):
    """
    zeroing(num,leng,numset,/) takes a string, it's length and the standard numset
    Returns a list of strings, which is readable for the dictionary.
    """
    i = 0
    while i<=len(num)-1:
        if num[i] != '0' and i != len(num)-1:
            num[i] = num[i] + "0"*(leng - i -1)
        elif num[i] == "0":
            del num[i]
            i-=1
            leng-=1
        i += 1
    return num

def num_to_word(num):
    """
    num_to_word(num,/) takes a string,
    Returns a string that represends a number in words
    """

    if num in NUMBERS:
        return NUMBERS[num]

    num = list( map( 
        lambda x: NUMBERS[str(x)],
         zeroing(check_spec(
             list(num)),
             len(num),
             NUMBERS) ) )

    return " ".join(num)
def long_num(num):
    if num == "1000000":
            return " one million "
    elif int(num)>10**6:
        return "This number is too big"
    #thousands
    th_val = str(num)[0:-3]
    th = num_to_word(str(num)[0:-3])

    ones = num_to_word(str(num)[-3:len(num)])

    th = th + " thousands " if int(th_val) > 1 else th + " thousand "
    return(th + ones)

def assembler(num):
    """
    assembler(num,/)
    Returns a number in words.
    """
    if len(str(num))>3:
        return long_num(num)
    else:
        return(num_to_word(str(num)))

def cleaner(string):
    """
    cleaner(string,/) takes a string
    Returns a string, cleared from whitespaces and "zero"s
    """
    string = list(filter(
        lambda x : x != '' or x != " ",
        list(string)
        ))

    return string if len(string) != 0 else ""

def fin_clean(ans):
    """
    fin_clean(ans,/) takes a final version of the output
    returns it without whitespaces at the beginning and in the end
    """
    if ans[0] == ' ':
        ans = ans[1:len(ans)]
    if ans[-1]==' ':
        ans = ans[0:len(ans)-1]
    
    if "  " in ans:
        i = 0
        while i <len(ans)-1:
            if ans[i] + ans[i+1] == "  ":
                ans = ans[0:i] + ans[i+1:len(ans)]
                i-=1
            i+=1
    return ans

def wording(string):
    """
    wording(string,/) takes a string
    Returns a string that represands the full sentance
    """
    
    if not string:
        return "Invalid input"

    for i in string:
        if i not in ALPHA:
            return "Invalid input"

    string,s = splitting(string)
    if s != []:
        s = cleaner(sym_to_word(s))
    
    num = cleaner(
    list( map(
        lambda x: assembler(x),
        string
    ) ))

    if "This number is too big" in num:
        return "Invalid input"
    
    ans = ""
    j,k = 0,0

    for i in range(len(num)+len(s)):
        if j<len(num):
            ans += num[j]
            j+=1
        if k<len(s):
            ans += s[k]
            k += 1
    ans = fin_clean(ans)
    return ans