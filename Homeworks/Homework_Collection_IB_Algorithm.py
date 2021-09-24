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