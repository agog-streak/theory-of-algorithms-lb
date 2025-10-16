comparisons = 0
assignments = 0
rec_calls = 0

def quick_sort(arr, low, high):
    global comparisons, assignments, rec_calls
    rec_calls += 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)
    return arr

def partition(arr, low, high):
    global comparisons, assignments
    pivot = arr[(low + high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            comparisons += 1
            i += 1
        comparisons += 1
        j -= 1
        while arr[j] > pivot:
            comparisons += 1
            j -= 1
        comparisons += 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        assignments += 2

arr = [53, 5, 44, 47, 35, 83, 82, 85, 28]
print("Оригінальний список:", arr)
sorted_arr = quick_sort(arr.copy(), 0, len(arr)-1)
print("Відсортований список:", sorted_arr)
print(f"Кількість порівнянь: {comparisons}")
print(f"Кількість присвоєнь: {assignments}")
print(f"Кількість рекурсивних викликів: {rec_calls}")
