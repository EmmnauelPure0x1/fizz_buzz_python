# Fizz Buzz!

## Summary

* Super simple game that will substitute multiples of three and five for fizz and buzz respectfully, and fizzbuzz for multiples of the two.

## Tasks

**Core:**
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz" instead of the number
* For numbers which are multiples of both three and five print "FizzBuzz".

**Extra:**
* Make a new fizzbuzz file and make it functional
* Make it so we we can decide which numbers to substitute for fizz and buzz using functions

## Code

```python
# FizzBuzz Class creation
class FizzBuzz:

    def listed(self):
        # list creation
        list_num = []
        # creating a for loop to count from 1 to 101 and storing the value in number
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                # declaring that if the modulo operator can be applied to the the value of number and equal 0
                # then on this occasion substitute number with fizzbuzz
                list_num.append("fizzbuzz")
                # appending the result to the list
            elif number % 3 == 0:
                list_num.append("fizz")
            elif number % 5 == 0:
                list_num.append("buzz")
            # if the number isn't a multiple of 3 or 5 the number is appended normally.
            else:
                list_num.append(number)
        return(list_num)


# assigning variable to obj
obj = FizzBuzz()

# printing the class instance's methods
print(obj.listed())

# for looping over obj.listed method and printing it.
for i in obj.listed():
    print(i)


```