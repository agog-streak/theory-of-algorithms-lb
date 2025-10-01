def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    a = arr.copy()

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            assignments += 3  # 3 присвоювання при обміні
    return a, comparisons, assignments


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    a = arr.copy()

    for i in range(1, n):
        key = a[i]
        assignments += 1  # key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                assignments += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        assignments += 1
    return a, comparisons, assignments


# Тестування
A = [53, 5, 44, 47, 35, 83, 82, 85, 28]

sorted_sel, cmp_sel, asg_sel = selection_sort(A)
print("Selection Sort:")
print("Sorted:", sorted_sel)
print("Comparisons:", cmp_sel)
print("Assignments", asg_sel)

sorted_ins, cmp_ins, asg_ins = insertion_sort(A)
print("\nInsertion Sort:")
print("Sorted:", sorted_ins)
print("Comprassion:", cmp_ins)
print("Assignments:", asg_ins)


