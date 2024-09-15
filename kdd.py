import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def medir_tempo(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

lista_palavras = []

with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        lista_palavras.extend(palavras)

lista_bubble_sort = lista_palavras.copy()
tempo_bubble_sort = medir_tempo(bubble_sort, lista_bubble_sort)
print("Ordenação com Bubble Sort:")
print(lista_bubble_sort)
print(f"Tempo de execução: {tempo_bubble_sort:.6f} segundos")

lista_selection_sort = lista_palavras.copy()
tempo_selection_sort = medir_tempo(selection_sort, lista_selection_sort)
print("\nOrdenação com Selection Sort:")
print(lista_selection_sort)
print(f"Tempo de execução: {tempo_selection_sort:.6f} segundos")

lista_sort = lista_palavras.copy()
tempo_sort = medir_tempo(lambda arr: arr.sort(), lista_sort)
print("\nOrdenação com o método sort():")
print(lista_sort)
print(f"Tempo de execução: {tempo_sort:.6f} segundos")

with open('texto_ordenado.txt', 'w') as arquivo:
    for palavra in lista_sort:
        arquivo.write(palavra + '\n')

print("\nPalavras ordenadas foram salvas em 'texto_ordenado.txt'.")
