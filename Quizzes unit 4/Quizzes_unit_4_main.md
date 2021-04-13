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
![Quiz 30](https://user-images.githubusercontent.com/60378207/114351751-01ae2b00-9ba6-11eb-946f-b7b74bcd3c8f.png)

## Quiz 31
### Solution
```.html
<!-- Quiz 31-->
<!-- Inputs: string of votes(Name voted for Name/ Name skipped)-->
<!--Outputs: determened which person was ejected(most votes)
if the number of voted is bigger than skipped peolple-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 31</title>
</head>
<body>
    <h1>Quiz 31</h1>
    <h3>To see results, check the console</h3>

    <script>
        // Creating a function
        function saboteur(array_of_votes) {
            // Creating arrays
            var people_who_voted = new Array();
            var people_who_skipped = new Array();

            for (var i = 0; i < array_of_votes.length; i++) {

                // Checking if each input has " voted for ".
                // If so, this means the person after " voted for " is selected by voting
                // https://www.w3schools.com/jsref/jsref_includes_array.asp
                var test = array_of_votes[i].includes(" voted for ")
                if(array_of_votes[i].includes(" voted for ") == true) {

                    //  Spilt the string to get the names of the voter and person who is voted
                    //  https://www.w3schools.com/jsref/jsref_split.asp
                    var vote = array_of_votes[i].split(" voted for ");

                    // Saving a selected person by voting into an array
                    // https://stackoverflow.com/questions/18546038/store-javascript-variable-into-array
                    people_who_voted.push(vote[1]);
                }
                else{
                    // If some input doesn't contain " voted for " it means that the person skipped voting
                    var skipped = array_of_votes[i].split(" skipped voting");
                    // Saving the name of the person who skipped
                    people_who_skipped.push(skipped[0])
                }
            }
            // Adding a flag variable to make sure that the counting
            // process is happening only when needed
            var flag = 0;
            if(people_who_skipped.length > people_who_voted.length){
                console.log("No one was ejected (Skipped)");
                flag ++;
            }
            if(people_who_skipped.length == people_who_voted.length){
                console.log("No one was ejected (Tie)");
                flag ++;
            }
            if(flag == 0) {

                var max_occurrence = 0;
                var most_voted_person = "";
                // Checking counting the number of occurrences(votes for a particular person) for each person
                for (var y = 0; y < people_who_voted.length; y++) {
                    var votes_for_an_each_person = 0;
                    var votes_for_an_each_person = people_who_voted.filter((v) => (v === people_who_voted[y])).length;

                    // Saving the biggest number of occurrences
                    // and the person who got the most occurrences
                    if (votes_for_an_each_person > max_occurrence) {
                        max_occurrence = votes_for_an_each_person
                        most_voted_person = people_who_voted[y]
                    }
                }
                // Outputing the person who mostly voted for(got the biggest number of occurrences)
                var ejected_person = most_voted_person + " was ejected"
                console.log(ejected_person);

            }

        }
    // Testing
        saboteur(array_of_votes = ["Green voted for Black", "Black voted for Blue", "Brown voted for Blue", "Blue voted for Black", "Cyan skipped voting", "Lime voted for Black"])
        saboteur(array_of_votes = ["Cyan skipped voting", "Cyan skipped voting", "Cyan skipped voting", "Blue voted for Black", "Cyan skipped voting", "Lime voted for Black"])
        saboteur(array_of_votes = ["Black voted for Blue", "Cyan skipped voting", "Cyan skipped voting", "Blue voted for Black", "Cyan skipped voting", "Lime voted for Black"])

    </script>
</body>
</html>
```
### Testing
![Quiz 31](https://user-images.githubusercontent.com/60378207/114541426-ad807500-9c91-11eb-867c-7f45cc0f351f.png)


