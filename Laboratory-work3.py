comparisons = 0
assignments = 0

def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    global assignments
    arr[i], arr[j] = arr[j], arr[i]
    assignments += 3  # три операції присвоєння

def sink(arr, i, n):
    """Процедура 'занурення' елемента вниз по купі."""
    global comparisons, assignments
    k = i
    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента
        assignments += 1  # присвоєння j
        if j >= n:
            comparisons += 1
            break

        # Знаходимо індекс найбільшого дочірнього елемента
        comparisons += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            comparisons += 1
            j += 1
            assignments += 1

        comparisons += 1
        if arr[k] >= arr[j]:
            break

        swap(arr, k, j)
        k = j
        assignments += 1

def heapsort(arr):
    """Алгоритм пірамідального сортування з підрахунком операцій."""
    global comparisons, assignments
    n = len(arr)
    print(f"Початковий масив: {arr}\n")
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        sink(arr, i, n)
    print(f"\nМасив після побудови купи: {arr}\n")

    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        n -= 1
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        sink(arr, 0, n)
        print(f"Масив на поточному кроці: {arr}\n")

    print(f"Загальна кількість порівнянь: {comparisons}")
    print(f"Загальна кількість присвоєнь: {assignments}")
    return arr

# Моделювання
A = [53, 5, 44, 47, 35, 83, 82, 85, 28]
sorted_A = heapsort(A)
print(f"Відсортований масив: {sorted_A}")

