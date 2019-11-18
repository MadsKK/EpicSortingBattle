
def insertionSort(liste):

    for i in range(1, len(liste)):
        key = liste[i]
        j = i-1
        while j >= 0 and key < liste[j]:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = key

    return liste


def selectionSort():
    pass


def bubbleSort():
    pass


def mergeSort():
    pass


if __name__ == "__main__":

    print(insertionSort(['agftd', 'ckfdfo', 'bkeoksess',
                         'fsdfsdofksdofds', 'lokesomses', 'zsfkdo', 'pfe']))
