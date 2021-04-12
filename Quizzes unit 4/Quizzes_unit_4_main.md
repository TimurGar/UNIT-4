# Quizzes UNIT-4
## Quiz 28
### Solution
### HTML
```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="quiz_28_style_sheet.css">
    <title>Quiz 28</title>
</head>
<body>
    <div>
        <h1>Quiz 28</h1>
        <img src="backgroung_img.jpg" alt="" id="backgroung-img">
        <img src="Quiz 28.png" alt="" id="code">
        <img src="Flow diagram.jpg" alt="" id="flow">

    </div>
</body>
</html>
```
### CSS
```.css
#backgroung-img{
    alignment: center;
    width: 100%;
    max-width: 1800px;
    height: auto;
    max-height: 850px;
}
h1{
    position: absolute;
    color: white;
    font-family: sans-serif;
    top: 5%;
    left: 45%;
}
#code{
    width: 100%;
    max-width: 600px;
    height: auto;
    max-height: 900px;

    position: absolute;
    top: 65%;
    left: 25%;
    transform: translate(-50%, -50%);
}
#flow{
    width: 100%;
    max-width: 500px;
    height: auto;
    max-height: 800px;

    position: absolute;
    top: 65%;
    left: 70%;
    transform: translate(-50%, -50%);
}
```
## Result
![Quiz 28 r](https://user-images.githubusercontent.com/60378207/113653481-e1c3c680-96d0-11eb-9e36-ce3bff79bd57.png)


## Quiz 29
### Initial Flow diagram
![170995002_359152632094324_8264247836928379369_n](https://user-images.githubusercontent.com/60378207/114350870-c6f7c300-9ba4-11eb-8040-9eb6bdb3d24d.jpg)

### Solution
```.py
# Quiz 27
# Inputs:
# Total number of LEDs in a strip,
# number of sections tested,
# results of the section test

# Output:
# string with the status of each LED in a strip

class Quiz_29():
    # initializing
    def __init__(self,n,m, results):
        self.n = n
        self.m = m
        self.results = results

    # Main algorithm
    def LED_test(self):
        out = []

        # assigning "not enough info" status by default
        for x in range(self.n):
            out.append("?")

        for i in self.results:
            # Separating range of tested LEDs from status of the LEDs,
            # and storing them into corresponding variables
            tested_range,status = i.split(":")
            # Separating the start of the range from the end,
            # and storing them into corresponding variables
            tested_range_start,tested_range_end = tested_range.split("-")
            # 3, 4

            # Checking the status of tested LEDs
            if status == "PASS":
                tested_out = "V"
            if status == "FAIL":
                tested_out = "X"

            # Finding the corresponding LEDs that were tested
            # and changing their status depending on the result
            for i in range(int(tested_range_start),int(tested_range_end)+1):
                out[i] = tested_out

        # Converting "out" to a string
        print("".join(out))

# Testing
test1 = Quiz_29(10,2,["3-4:PASS", "6-7:PASS"]).LED_test()
test2 = Quiz_29(10,2,["1-2:PASS", "5-6:PASS"]).LED_test()
test3 = Quiz_29(8,3,["1-1:PASS","3-3:FAIL", "7-7:FAIL"]).LED_test()
test4 = Quiz_29(12,3,["1-5:PASS","0-0:FAIL", "6-11:PASS"]).LED_test()

```
### Testing
![Quiz 29](https://user-images.githubusercontent.com/60378207/114259919-6a61a000-9a0c-11eb-84e4-6cf12626bd9e.png)

## Quiz 30
### Initial Flow diagram
![IMG_20210412_134503](https://user-images.githubusercontent.com/60378207/114350975-eb539f80-9ba4-11eb-94e6-0dc7ab673ce2.jpg)

### Solution
```.py
# Quiz 30
# Inputs:
# Number

# Output:
# number of divisors of the number that are divisible by 2

class Quiz_30():
    # initializing
    def __init__(self,num):
        self.num = num

    def findTwoDivisors(self):
        divisors = 0
        # Checking if the number is divisible by 2
        # If not, it will not have divitors of 2
        if self.num % 2 == 0:
            # Finding and counting divisors that are divisible by 2
            for i in range(1, self.num + 1):
                if self.num % i == 0 and i % 2 == 0:
                    divisors += 1

        print(divisors)

# Testing
test1 = Quiz_30(8).findTwoDivisors()
test2 = Quiz_30(9).findTwoDivisors()
test3 = Quiz_30(158260522).findTwoDivisors()
test4 = Quiz_30(861648772).findTwoDivisors()
test5 = Quiz_30(569097293).findTwoDivisors()


```
### Testing
![Quiz 30](https://user-images.githubusercontent.com/60378207/114350559-4fc22f00-9ba4-11eb-8d85-b542a7b0929a.png)

