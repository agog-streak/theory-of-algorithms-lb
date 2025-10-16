comparisons = 0
assignments = 0
rec_calls = 0

def merge_sort(arr):
    global comparisons, assignments, rec_calls
    rec_calls += 1
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            assignments += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            assignments += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            assignments += 1
    return arr

arr = [53, 5, 44, 47, 35, 83, 82, 85, 28]
print("Оригінальний список:", arr)
sorted_arr = merge_sort(arr.copy())
print("Відсортований список:", sorted_arr)
print(f"Кількість порівнянь: {comparisons}")
print(f"Кількість присвоєнь: {assignments}")
print(f"Кількість рекурсивних викликів: {rec_calls}")