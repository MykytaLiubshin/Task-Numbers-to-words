from dicts import create_dict,create_dict_s
from re import sub

def splitting(string):
    #splitting takes a string and returns it splitted by it's symbols and the set of symbols OK
    symbols,s = create_dict_s(),[]
    for i in string:
        if i in symbols:
            s.append(i)
            string = ' '.join(string.split(str(i)))
    return string.split(' '),s

def sym_to_word(string):
    #symbol to word converter takes a list and replaces all of it's symbols w/ words OK
    sym = create_dict_s()
    for i in range(len(string)):
        if string[i] in sym:
            string[i] = sym[str(string[i])]
    return string

def check_spec(num):
    #Check for spec takes a string, searches if there are fundamental numbers in it
    #Fundamental number - these ones that in words are not made by a combination of others OK
    h = [str(10+i) for i in range(10)]
    if len(num)>1:
        if num[-2]+num[-1] in h:
            num[-2]+=num[-1]
            del num[-1]
    return num

def zeroing(num,leng,numset):
    #Zeroing takes a string, it's length and the standard numset
    #Returns a readable (for the dictionary) list of strings  OK
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
    #Number to word converter takes a string as an arg
    #Returns a string that represends a number in words OK
    numset = create_dict()

    if num in numset:
        return numset[num]

    num,leng = check_spec(list(num)),len(num)
    num = zeroing(num,leng,numset)

    for i in range(len(num)):
        num[i] = numset[str(num[i])]
    return " ".join(num)


def assembler(num):
    #Assembler "deassebles" the number if needed and "assebles" it back 
    #Takes a string as an arg
    #Returns the full number, that is readible for people OK
    if len(str(num))>3:
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
    else:
        return(num_to_word(str(num)))

def cleaner(string):
    #Cleaner takes a string as an argument
    #Returns a string, cleared from whitespaces and "zero"s OK
    i = 0
    while i <= len(string) - 1:
        if string[i] == '' or string[i] == " ":
            del string[i]
            i -= 1
        i += 1
    
    if len(string[0])>6 and "zero" in string[0]:
        string = sub(r'zero', '', string[0])

    return string
def fin_clean(ans):
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
    #Wording takes a string as an arg
    #Returns a string that represands the full sentance OK
    #Valudation Check below
    alpha = "1234567890+-*/= "
    for i in string:
        if i not in alpha:
            return "Invalid Input"

    string,s = splitting(string)
    if s != []:
        s = cleaner(sym_to_word(s))

    num = [assembler(i) for i in string]
    num = cleaner(num)

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