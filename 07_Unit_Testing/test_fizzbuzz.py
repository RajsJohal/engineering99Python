from fizzbuzz import *

#user input --> max number to hit
#verify_digits
# monkeypatch - throwing in inputs to the input function to test user inputs


# produces correct output

def test_fizzbuzz_output_3_returns_fizz():
    assert fizzbuzz_output(3) == "Fizz"

def test_fizzbuzz_output_5_returns_buzz():
    assert fizzbuzz_output(5) == "Buzz"

def test_fizzbuzz_output_15_returns_buzz():
    assert fizzbuzz_output(15) == "FizzBuzz"



