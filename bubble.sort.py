def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

numeros = [34, 7, 23, 32, 5, 62, 14, 19, 10, 43, 2, 55, 27, 3, 50]

bubbleSort(numeros)

print("Array ordenado utilizando Bubble Sort:", numeros)