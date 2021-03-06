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

## Quiz 32
### Solution
```.html
<!-- Quiz 32-->
<!-- Inputs: encoded string characters and another string containing "E"s and "S"s which are the directions -->
<!--Outputs: Decoded message -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 32</title>
</head>
<body>
<h1>Quiz 32</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function BlackBox(string,directions){
        // Creating arrays to store initial data
        var s_letters = new Array();
        var e_letters = new Array();

        // Finding and separating "E"s from "S"s
        for(let i = 0; i < directions.length; i++){
            if(directions[i] == "E"){
                // Saving E"s in the array
                e_letters.push(string[i]);
            }
            if(directions[i] == "S"){
                // Saving "S"s in the array
                s_letters.push(string[i]);
            }
        }
        //Converting arrays into string
        let str_e_letters = e_letters.join("")
        let str_s_letters = s_letters.join("");


        var flipped_s_letters = ""
        // Fliping and saving "S"s letters
        for(let y = s_letters.length - 1; y >= 0; y--){
            flipped_s_letters += s_letters[y]
        }
        // Conbining flipped "S"s letters with "E"s letters
        var out = flipped_s_letters += str_e_letters
        //Pring the result into a console
        console.log(out);

    }
    // Testing
    BlackBox("231 :ELPMAXE!","SESSSSSSSSSSE")
    BlackBox("435","SSE")
    BlackBox(" oworllledH!","SSEEESESSESE")
    BlackBox("input","EEEEE")
    BlackBox("input","SSSSS")

</script>
</body>
</html>
```
### Testing
![Quiz 32](https://user-images.githubusercontent.com/60378207/114966001-aaad9c00-9eac-11eb-9ac1-11f33764f498.png)

## Quiz 33
### Initial flow diagram
![IMG_20210422_112242](https://user-images.githubusercontent.com/60378207/115832668-1b752b00-a44e-11eb-96f2-c81273ef30d5.jpg)

### Solution
```.html
<!-- Quiz 33-->
<!-- Inputs: a text and a specific letter-->
<!--Outputs: Counts the occurences of a specific letter in the text provided -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 33</title>
</head>
<body>
<h1>Quiz 33</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function countLetter(text,letter){
        var count = 0;
        //Going through each character in the text
        for(let i = 0; i < text.length; i++){
            //Finding and counting an occurence of a specific letter
            if(text[i] == letter){
                count++;
            }
        }
        console.log(count)
    }
    // Testing
    countLetter("Hello world! I am Timur. I like Computer Science","e")

</script>
</body>
</html>
```
### Testing
![Quiz 33](https://user-images.githubusercontent.com/60378207/115650099-8d247a80-a363-11eb-8201-a716a222a9ef.png)

## Quiz 34
### Initial Brainstorming
![IMG_20210423_134351 (1)](https://user-images.githubusercontent.com/60378207/115832339-be797500-a44d-11eb-9c08-0db1a1aa622f.jpg)

### Solution
```.html
<!-- Quiz 34-->
<!-- Inputs: array with roads that lead to cities-->
<!--Outputs: Number of cities that can be reach from city 0 -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 34</title>
</head>
<body>
<h1>Quiz 34</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function RoadsAndCities(roads_to_cities){
        var list_of_cities = new Array();

        // Number in the array - road from city N, -1 = no road
        // Index of the road - city N-1

        // Checking every road that lead to a city
        for(let i=0; i < roads_to_cities.length; i++){
            // Checking if there is a city in the list_of_cities array -> it can also be reached from city 0
            // or if the city can be reach from city 0
            if(roads_to_cities[i] == "0" || list_of_cities.includes(roads_to_cities[i])){
                // Adding a city that can be reached for later comparison
                list_of_cities.push(i)

            }

        }
        // Outputing the result
        console.log("INPUT:", roads_to_cities,"OUTPUT:", list_of_cities.length)

    }
    // Testing
    RoadsAndCities([-1,0,-1,1,2,3])
    RoadsAndCities([-1,0,1,2,3,0,2,6,7,8])
    RoadsAndCities([-1,0])
    RoadsAndCities([-1,-1,1,2,3,4,5,6,7,8,9])

    // Generating an array of numbers from -1 to 998
    var test_array = new Array()
    for(let y=-1; y < 999; y++){
        test_array.push(y);
    }
    RoadsAndCities(test_array)

</script>
</body>
</html>
```
### Testing
![Quiz 34](https://user-images.githubusercontent.com/60378207/115832244-a3a70080-a44d-11eb-8597-3e076d8f770b.png)


## Quiz 35
### Solution, works for 45, 15
```.html
<!-- Quiz 35-->
<!-- Inputs: an angle between minute and hour hand -->
<!--Outputs: time in h:mm format -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 35</title>
</head>
<body>
<h1>Quiz 35</h1>
<h3>To see results, check the console</h3>

<script>
    var testing_angle = 45
    console.log("INPUT: ", testing_angle)
    //Creating a function
    //The function will find all possible times
    function Brute_Force_time(input) {
        var array_times_hours = new Array()
        var array_times_minutes = new Array()
        for (i = 1; i < 13; i++) {

            var input_modified = input + 15

            // Finding hours
            var hours = 0
            while (input_modified > 0){
                input_modified -= 30;
                hours +=1
            }

            var minute_number = i + hours

            // Finding minute
            var degrees = 360/ (12/minute_number)
            var minute = degrees/6


            if (minute <61){
                if (minute == 60){
                    array_times_hours.push(i)
                    array_times_minutes.push(0)
                }
                else{
                    array_times_hours.push(i)
                    array_times_minutes.push(minute)
                }
            }
        }
        return [array_times_hours, array_times_minutes, array_times_hours.length]
    }

    // Creating a function
    // The angle will check if the time found has correct angle
    function Check_the_angle(hours,minutes){
        deg_hours = hours * (360/12) + (minutes * 360)/(12 * 60);
        deg_minutes = (minutes * 360)/(60);

        angle = Math.abs(deg_hours - deg_minutes);

        if (angle > 180) {
            angle = 360 - angle;
        }
    return angle

    }

    //Checking angles
    var values = Brute_Force_time(testing_angle)
    var B_hours = values[0]
    var B_minutes = values[1]
    var B_length = values[2]

    // Printing the results
    for(let i=0; i < B_length; i++){
        if(Check_the_angle(B_hours[i],B_minutes[i]) == testing_angle){
            console.log(B_hours[i] +":" + B_minutes[i])
        }
    }

</script>
</body>
</html>
```
### Testing
![Quiz 35](https://user-images.githubusercontent.com/60378207/116508877-40114d00-a8fd-11eb-8735-7ce891230ae7.png)
![Quiz 35 2](https://user-images.githubusercontent.com/60378207/116508959-66cf8380-a8fd-11eb-9da7-71241485a70e.png)


## Quiz 36
### Solution
```.html
<!-- Quiz 36-->
<!-- Inputs: arrays of number -->
<!--Outputs: calculated the mean or the median of the array -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 36</title>
</head>
<body>
<h1>Quiz 36</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function Black_box_median(array_of_numbers){
        // Sorting an array
        console.log("INPUT: ", array_of_numbers);
        for(let i=0; i< array_of_numbers.length; i++){

            for(let y=0; y< array_of_numbers.length; y++){
                // Swapping numbers in the array
                if(array_of_numbers[y] < array_of_numbers[y+1]){
                    var small_value = array_of_numbers[y]
                    var big_value =  array_of_numbers[y+1]
                    array_of_numbers[y] = big_value
                    array_of_numbers[y+1] = small_value
                }
            }
        }

        // If the length of the array is odd
        if(array_of_numbers.length % 2 != 0){
            // Finding an index of a median
            // -1 because array starts from 0
            var index_of_median = (array_of_numbers.length + 1) / 2 - 1;
            var median = array_of_numbers[index_of_median];

            console.log("OUTPUT: ", median);
        }
        // If the length of the array is even
        else {
            var mean = 0
            // Finding the sum of all the numbers in the array
            for(let z=0; z< array_of_numbers.length; z++){
                mean += array_of_numbers[z];
            }
            // Finding the mean of the array
            mean = mean / array_of_numbers.length;
            mean = Math.floor(mean);
            console.log("OUTPUT: ", mean);
        }

    }
    // Testing
    Black_box_median([3,2,1])
    Black_box_median([5,4,3,2,1])
    Black_box_median([30,2,1,2])
    Black_box_median([5,4,1,3,2,2])
    Black_box_median([22,13,4,5,1,12,10,66,9])
    Black_box_median([1,2,3,4,5,6,7])
    Black_box_median([20,18,19,16,9,8,7,6,8,2])
    Black_box_median([8,7,6,5,4,3,2,1])

</script>
</body>
</html>
```
### Testing

![Quiz 36](https://user-images.githubusercontent.com/60378207/116332507-dfa2e280-a80c-11eb-9a61-25d9a93971fd.png)


## Quiz 37
### Initial flow diagram
![IMG_20210430_161432](https://user-images.githubusercontent.com/60378207/116662830-3c4efa80-a9d1-11eb-9b89-614045caf408.jpg)

### Solution
```.html
<!-- Quiz 37-->
<!-- Inputs: string of numbers -->
<!--Outputs: the biggest difference between coherent numbers -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 37</title>
</head>
<body>
<h1>Quiz 37</h1>
<h3>To see results, check the console</h3>

<script>
    //Creating a function
    function Biggest_difference(string){
        console.log("INPUT: ", string)
        var max = 0;
        // Checking if the string's length is greater than 1
        // Otherwise there is nothing to compare so we just output the string itslef
        if(string.length > 1){
            // Going through all the numbers in the string
            for(let i=0; i< string.length; i++){
                dif = 0;

                // Calculating the difference between coherent numbers
                dif = parseInt(string[i+1]) - parseInt(string[i]);

                // Saving the biggest difference
                if(Math.abs(dif) > Math.abs(max)){
                    max = dif;
                }
            }
            console.log("OUTPUT: ", max)
        }
        else {
            console.log("OUTPUT: ", string)
        }
    }
    // Testing
    Biggest_difference("02354310");
    Biggest_difference("12386456792");
    Biggest_difference("12387356792");
    Biggest_difference("21025643894");
    Biggest_difference("0");
</script>
</body>
</html>
```
### Testing
![Screen Shot 2021-04-30 at 16 30 53](https://user-images.githubusercontent.com/60378207/116663003-7ae4b500-a9d1-11eb-8996-30fa10d870d3.png)


## Quiz 39
### Initial psudocode
![IMG_20210504_082321](https://user-images.githubusercontent.com/60378207/116948322-0acc7c80-acba-11eb-9059-4c6de13fc846.jpg)

### Solution
```.html
<!-- Quiz 39-->
<!-- Inputs: a range of numbers -->
<!--Outputs: number of Narcissistic numbers between the range -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 39</title>
</head>
<body>
<h1>Quiz 39</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function Narcissistic_num(m,n){
        console.log("INPUTS= ", m, n)

        nar_numbers = new Array();
        // Looping through all the numbers between the range provided(excluding m,n)
        for(let i=m+1; i< n;i++){
            var sum = 0
            // Convert number to string
            str_i = i.toString();
            // Finding the lenght of string(or amount of digits in the number)
            str_length = str_i.length;

            // Looping through all the digits in the number
            for(let y=0; y< str_length; y++){
                // Doing calculations, to later check if the number is narcissistic
                sum += str_i[y] ** str_length;
            }
            // Checking if the number is narcissistic
            if(sum == i){
                nar_numbers.push(i);
            }
        }
        console.log("OUPUT= ", nar_numbers.length);
    }
    // Testing
    Narcissistic_num(3,9);
    Narcissistic_num(0,500)
</script>
</body>
</html>
```
### Testing
![Quiz 39](https://user-images.githubusercontent.com/60378207/116948276-ed97ae00-acb9-11eb-88f2-1c29a9860860.png)

## Quiz 41
### Solution
```.html
<!-- Quiz 41-->
<!-- Inputs: initial sizes of particles -->
<!--Outputs: number of particles can be created by collision -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Quiz 41</title>
</head>
<body>
<h1>Quiz 41</h1>
<h3>To see results, check the console</h3>

<script>
    // Creating a function
    function Particles(l){
        console.log("INPUT: ", l);

        var new_particle = 0;
        var flag = 0;
        // Looping until all possible sizes has been added
        while (flag != 1) {
            // Finding the sizes of particles after the collision
            for (y = 0; y < l.length; y++) {
                for (i = 0; i < l.length; i++) {
                    // Calculating the size of each new particle after the collision
                    new_particle = Math.abs(l[y] - l[i + y]);
                    if (new_particle >= 1 && l.includes(new_particle) == 0) {
                        l.push(new_particle);
                    }
                    else {
                        flag = 1;
                    }
                }
            }
        }
        console.log("OUTPUT: ",l.length);
    }
    // Testing
    Particles([2,3,6]);
    Particles([6,9]);
    Particles([18,24]);
    Particles([5,6,92,2,7]);
    Particles([200,101,19,3]);

</script>
</body>
</html>
```
### Testing
![Quiz 41](https://user-images.githubusercontent.com/60378207/118612136-71908080-b7f8-11eb-9341-aa36fc7cd3fa.png)

## Quiz 45
### Solution
```.py
# Quiz 45
# Inputs:
# none

# Output:
# 10 lists with a randomly generated numbers inside
# A sum of each list

from random import randrange

# creating a function
def rand_lists():
    # creating a list of lists
    list_of_lists = [[] for i in range(10)]
    for count, list in enumerate(list_of_lists):
        n, sum = 0, 0
        
        # Generating and adding random numbers to lists
        # Finding a sum of lists
        for y in range(10):
            n = randrange(10)
            sum += n
            list.append(n)
        
        # Showing the result
        print(f"List_{count} {list_of_lists[count]} Sum = {sum}")

# Calling a function
rand_lists()
```
### Testing
![Screen Shot 2021-09-06 at 9 17 38](https://user-images.githubusercontent.com/60378207/132145414-01f58684-a1e5-4ddb-88c6-550fc52c4508.png)

## Quiz 46
### Solution
```.py
# Quiz 45
# Inputs:
# number

# Output:
# average, highest and lowest numbers

avr, highest, lowest, counter = 0, 0, 0, 0
while counter < 999:
    number = int(input("Enter a number: "))
    if number >= 0 and number % 1001:
        avr = (avr + number) / (counter + 1)
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
        counter += 1
    else:
        print("Input a number bigger than 0 and smaller than 1001")

print(f"highest - {highest}, lowest - {lowest}, avr - {avr}")
```
### Testing
![Screen Shot 2021-09-09 at 21 34 06](https://user-images.githubusercontent.com/60378207/132686664-933d182c-0911-42f5-9cd9-6ad574e635dd.png)

## Quiz 47
## Part one
### Solution
```.py
# Quiz 47
# Inputs:
# none

# Output:
# 2D array with the position of the chess board


letters = ["A","B","C","D","E","F","G","H"]
line = ""

#  counter is used to go through all the values in the letters array
for counter in range(8):
    # i is used through the numbers 1-8
    for i in range(8):
        # Combining a letters with numbers
        message = letters[counter] + str(i+1)
        # creating a line of messages
        line = line + " " + message

    line = line + "\n"

print(line)
```
### Testing
![Screen Shot 2021-09-10 at 12 12 45](https://user-images.githubusercontent.com/60378207/132793590-c204e83e-149f-4051-955c-20a2e86d13d4.png)

## Part two
### Solution
```.py
# Task create a class Array with functions get and set

class Array():
    # Initializing 
    def __init__(self, size):
        self.size: int = size
        self.data: list = [None] * size


    # Creating "get" function
    def get(self, index):
        return print(f"The value with index {index} is {self.data[index]}")


    # Creating "set" function
    def set(self, index, value):
        
        # checking if the value provided is not bigger than the size of the array
        if index <= self.size:
            self.data[index] = value
            return print(f"updated array - {self.data}")
        else:
            return print("Index out of range")

# Testing
array = Array(5)
array.set(7,7)
array.set(1,6)
array.set(2,9)
array.set(3,100)
array.set(4,-1)
array.get(0)
```
### Testing
![Screen Shot 2021-09-10 at 12 16 06](https://user-images.githubusercontent.com/60378207/132793835-d32c7411-1320-448e-918d-9a62f0f532c5.png)

## Quiz 48
## Part one
### Solution
```.py
# Quiz 48
# Inputs:
# 10 numbers from a user

# Output:
# average of the numbers

# Special requirements
# Have to use a queue

from HomeworkQueue import Queue
Q = Queue()
sum = 0
for i in range(10):
    inp = int(input("Input number: "))
    Q.enqueue(inp)
for y in range(10):
    dq = Q.deque()
    sum += int(dq)
print(f"Sum - {sum/10}")
```
### Testing
![Screen Shot 2021-09-16 at 9 19 41](https://user-images.githubusercontent.com/60378207/133530308-655cf8a4-99ad-4f33-8d54-02439f8d8029.png)

## Homework - Stack
### Solution
```.py
class Stack:
    # Initializing
    def __init__(self):
        self.data: list = []

    def push(self, value):
        self.data.append(value)
        print(f"Current stack - {self.data}")

    def pop(self):
        updated_stack = []
        if len(self.data) != 0:
            for i in range(len(self.data)-1):
                updated_stack.append(self.data[i])
            print(f"First in line - {self.data[-1]}, current stack - {updated_stack}")
            self.data = updated_stack
        else:
            return print("Stack is empty")

    def is_empty(self):
        if self.data:
            print("stack is not empty")
        else:
            print("stack is empty")

    def currrent_size(self):
        return print(f"current length - {len(self.data)}")

# Testing
stack1 = Stack()
stack1.push(3)
stack1.push(5)
stack1.pop()
stack1.pop()
stack1.push(100)
stack1.is_empty()
stack1.currrent_size()
```
### Testing
![Screen Shot 2021-09-16 at 8 51 42](https://user-images.githubusercontent.com/60378207/133527975-39e8b799-0cd5-4f9b-9c1b-4481049c2243.png)

## Quiz 49
### Solution
```.py
# Quiz 49
# Inputs:
# 10 Ib scores(1-7) from the user

# Output:
# average of the scores

# Special requirements
# Have to use a stack

from HomeworkStack import Stack

# Creating a function
def Quiz_49():
    stack = Stack()
    stack2 = Stack()
    data = []
    sum = 0
    # Getting scores from the user
    for i in range(10):
        score = int(input("Enter a score: "))
        if score >= 8 or score <= 0:
            print("Incorrect score")
        else:
            # Saving scores into a stack
            stack.push(score)

    # Popping scores from the stack and calculating the average 
    for y in range(10):
        val = stack.pop()
        sum += val
        # saving all the entered grades in a new stack
        stack2.push(val)

    return print(f"Average score is {sum/10}")

Quiz_49()
```
### Testing
![Screen Shot 2021-09-17 at 11 35 30](https://user-images.githubusercontent.com/60378207/133715340-a2e8b1d6-a67f-4d03-bca7-47963170a116.png)
