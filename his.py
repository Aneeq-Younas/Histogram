def Histo(char):
    for i in char:

        result= " "
        measure= i

        while(measure > 0):
            result += " * "

            measure = measure -1
        print(result)

Histo([3, 2, 5, 8, 4, 10, 18, 5, 13, 7, 15, 7])






