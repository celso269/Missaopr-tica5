array = [34, 7, 23, 32, 5, 62, 14, 19, 10, 43, 2, 55, 27, 3, 50]

for i in range(len(array)):
    min_index = i
    
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print("Array ordenado utilizando Selection Sort:", array)
