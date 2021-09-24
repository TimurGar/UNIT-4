# Homeworks
## Data structures
### Collection
### Part one
```.py
# Creating a class
class Collection():
    # Initializing
    def __init__(self):
        self.data: list = []
        self.current_index: int = 0

    def addItem(self, value):
        self.data.append(value)
        print(f"{value} has been added ")

    def getNext(self):
        print(f"Next = {self.data[self.current_index]}")        # Fix here
        # val = self.data[self.current_index]
        self.current_index += 1
        # return val


    def resetNext(self):
        self.current_index = 0
        print(f"index set to {self.current_index}")

    def hasNext(self):
        if self.current_index == len(self.data):
            print("False")
            #return False
        else:
            print("True")
            #return True

# Testing
collection1 = Collection()
collection1.addItem("Paul")
collection1.addItem("Rugo")
collection1.addItem("David")
collection1.getNext()
collection1.getNext()
collection1.getNext()
collection1.hasNext()
collection1.resetNext()
collection1.getNext()
collection1.hasNext()
```
### Test
![Screen Shot 2021-09-24 at 14 02 31](https://user-images.githubusercontent.com/60378207/134620917-cec90624-6714-43b9-8d88-4d5ece75ae9e.png)

### Part two
```.py
# Collection testing(IB program) 

from HomeworkCollection import Collection

LIST = []
COUNT = 0
NAMES = Collection()
NAMES.addItem("Paul")
NAMES.addItem("Rugo")
NAMES.addItem("David")
NAMES.addItem("Paul")
NAMES.addItem("Rugo")
NAMES.addItem("David")

while NAMES.hasNext():
    DATA = NAMES.getNext()
    FOUND = False

    for POS in range(COUNT):
        if DATA == LIST[POS]:
            FOUND = True

    if FOUND == False:
        LIST.append(0)
        LIST[COUNT] = DATA
        COUNT += 1

print(LIST)
```
### Test
![Screen Shot 2021-09-24 at 13 51 19](https://user-images.githubusercontent.com/60378207/134620099-4a04ccdb-063f-4cab-a410-62c939422381.png)

