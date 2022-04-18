#Write your code below this row 👇

numbers = range(1, 101)

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        number = ("Buzz")    
    else:
        print(number)


















































"""## FizzBuzz

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game. 

> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz"""