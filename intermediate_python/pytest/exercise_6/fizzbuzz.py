def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    if number % 15 == 0:
        return "FizzBuzz"
    return str(number)

def print_fizzbuzz(highest_number):
    fizzbuzz_numbers = (fizzbuzz(i) for i in range(1, highest_number))
    for n in fizzbuzz_numbers:
        print(n)

if __name__ == "__main__":
    print_fizzbuzz(100)