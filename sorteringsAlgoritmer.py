
def insertionSort(liste):
    sortedList = []
    indexList = []
    for x in range(len(liste)):
        print("x1: " + str(x))
        indexList += [x]
        for n in range(indexList[-1]):
            print("x2: " + str(x))
            print("n: " + str(n))
            if x < n:

                sortedList += [liste[x]]

    return sortedList


def selectionSort():
    pass


def bubbleSort():
    pass


def mergeSort():
    pass


if __name__ == "__main__":

    print(insertionSort(['agftd', 'ckfdfo', 'bkeoksess']))
