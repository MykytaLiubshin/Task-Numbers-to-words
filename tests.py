from task import wording

def test():
    assert "one hundred twenty nine thousands twenty nine" == wording("129029")
    assert "two" == wording("2")
    assert "one million" == wording("1000000")
    assert "three plus seven equals ten" == wording("3 + 7 = 10")
    assert "one million divided by one thousand divided by one hundred equals ten" == wording("1000000 / 1000 / 100 = 10")
    assert "twelve plus nineteen minus thirteen divided by eighteen multyplied with three equals one" == wording("12 + 19 - 13 / 18 * 3 = 1")
test()