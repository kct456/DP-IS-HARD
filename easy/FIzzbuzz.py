'''
Variant of fizzbuzz

Time: O(n), where n is the length of divisbleCheck and correspondingWord : We need to iterate through divisibleCheck and correspondingWord
Space: O(1) : Doesn't use extra space
'''

def fizzBuzz(num: int, divisbleCheck: list, correspondingWord: list):
    resultWord = ''
    for index, divisor in enumerate(divisbleCheck) :
        if num % divisor == 0:
            resultWord += correspondingWord[index]
    return resultWord if resultWord != '' else num

# Example call to the method
fizzBuzz(15, [3, 5, 7], ["fizz", "buzz", "zazz"])