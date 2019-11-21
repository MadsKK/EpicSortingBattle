def insertionSort(liste):
    # Første for loop som holder styr på alle elementer
    for i in range(1, len(liste)):
        key = liste[i]
        # Gemmer det forrige element
        j = i-1
        # Hvis vi ikke er i starten, altså første element, og det nuværende
        # element er mindre end det forrige element
        while j >= 0 and key < liste[j]:
            # Sæt det nuværende element til det forrige element
            liste[j+1] = liste[j]
            # Tæller ned, så vi til sidst rammer starten. 8..7..6..5..4..3..2..1
            j -= 1
        liste[j+1] = key

    return liste


def selectionSort():
    pass


def bubbleSort(liste):
    # Første for loop som holder styr på alle elementerne
    for i in range(1, len(liste)):
        # Anden for loop som laver en bubble omkring 2 elementer
        for l in range(1, len(liste)-1):
            # Ser om det element man er nået til er større end det næste element
            if(liste[l] > liste[l+1]):
                # Bytter om på de 2 elementer
                temp = liste[l+1]
                liste[l+1] = liste[l]
                liste[l] = temp

    return liste


def mergeSort():
    pass


if __name__ == "__main__":

    print(insertionSort(['agftd', 'ckfdfo', 'bkeoksess',
                         'fsdfsdofksdofds', 'lokesomses', 'zsfkdo', 'pfe']))
    # print(selectionSort(['agftd', 'ckfdfo', 'bkeoksess',
    #                    'fsdfsdofksdofds', 'lokesomses', 'zsfkdo', 'pfe']))
