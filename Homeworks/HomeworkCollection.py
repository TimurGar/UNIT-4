class Collection():
    def __init__(self):
        self.data: list = []
        self.current_index: int = 0

    def addItem(self, value):
        self.data.append(value)
        print(f"{value} has been added ")

    def getNext(self):
        # print(f"Next = {self.data[self.current_index]}")        # Fix here
        val = self.data[self.current_index]
        self.current_index += 1
        return val


    def resetNext(self):
        self.current_index = 0
        print(f"index set to {self.current_index}")

    def hasNext(self):
        if self.current_index == len(self.data):
            # print("False")
            return False
        else:
            # print("True")
            return True

# collection1 = Collection()
# collection1.addItem("Paul")
# collection1.addItem("Rugo")
# collection1.addItem("David")
# collection1.getNext()
# collection1.getNext()
# collection1.getNext()
# collection1.hasNext()
# collection1.resetNext()
# collection1.getNext()
# collection1.hasNext()
