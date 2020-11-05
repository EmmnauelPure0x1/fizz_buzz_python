class FizzBuzz:
    def listed(self):
        list_num = []
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                list_num.append("fizzbuzz")
            elif number % 3 == 0:
                list_num.append("fizz")
            elif number % 5 == 0:
                list_num.append("buzz")
            else:
                list_num.append(number)
        return(list_num)

obj = FizzBuzz()
# print(obj.listed())

for i in obj.listed():
    print(i)