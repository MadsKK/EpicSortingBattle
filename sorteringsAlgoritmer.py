
def insertionSort(liste):
    sortedList = []
    indexList = []
    for x in range(len(liste)):
        indexList += x
        for n in indexList[-x]:
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
