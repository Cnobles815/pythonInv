import string
import sys

from pip._vendor.distlib.compat import raw_input

sessions = 0
attempts = 5

def reverserMethod():
    global sessions
    global attempts

    sessions += 1
    greeting()
    count = sessions
    sentence = input()
    input_words = sentence.split(" ")
    input_words = input_words[-1::-1]
    reversal = ' '.join(input_words)
    if reversal == 'x' or reversal == 'x'.swapcase() or counter(count) >= attempts:
        return sys.exit
    if reversal == '' or reversal.isspace():
        print("I can't reverse empty space. Nice try.")
        counter(count)
    if reversal.isnumeric():
        print("I could reverse a number for you, but that wasn't what you were asked to do so no.")
        counter(count)
    else:
        print(reversal)
        counter(count)
    reverserMethod()


def greeting():
    global sessions
    global attempts

    print("Type the sentence you want to reverse.")


def counter(number):
    result = number + 1
    return result


def echo(message, num_of_times=1):
    for x in range(num_of_times):
        print(message)


def kwarg_example(*args, **kwargs):
    print("Arguments")
    for arg in args:
        print(arg)
    print("KeyWord Arguments")
    for x in kwargs:
        print(x, " ",  kwargs[x] )

def char_in_string(c, st):
    return c in st

arr = "Hello World"

print(
    arr[2:-1]
)

