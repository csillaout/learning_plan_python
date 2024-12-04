from fizzbuzz import fizzbuzz, print_fizzbuzz
#1-> 1 ok
#2-> 2 ok 
#3-> fizz
#5-> buzz
#15-> fizzbuzz
#print up to 100


def test_fizzbuzz_one_is_one():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == '2'

def test_fizzbuzz_three_is_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_five_is_fizz():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz_fifteen_is_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"


def test_print_fizzbuzz(capsys):
    print_fizzbuzz(3)
    captured_stdout = capsys.readouterr().out
    assert captured_stdout == "1\n2\nFizz\n"