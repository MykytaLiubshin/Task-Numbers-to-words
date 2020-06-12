from task import wording

def wording_test():
    """
    wording_test(,/) takes no arguments,
    does 10 tests that check and validate
    the output of wording() function
    returns nothing
    """
    assert "one hundred twenty nine thousands twenty nine" == wording("129029")
    assert "two" == wording("2")
    assert "one million" == wording("1000000")
    assert "three plus seven equals ten" == wording("3 + 7 = 10")
    assert "plus divided by minus multyplied with equals" == wording("+/-*=")
    assert "one million divided by one thousand divided by one hundred equals ten" == wording("1000000 / 1000 / 100 = 10")
    assert "twelve plus nineteen minus thirteen divided by eighteen multyplied with three equals one" == wording("12 + 19 - 13 / 18 * 3 = 1")
    assert "Invalid input" == wording("one plus two equals three")
    assert "Invalid input" == wording("is this a text editor?")
    assert "Invalid input" == wording(".")
    assert "Invalid input" == wording("")

if __name__ == "__main__":
    wording_test()