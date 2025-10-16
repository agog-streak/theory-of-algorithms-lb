comparisons_iter = 0
assignments_iter = 0
merge_steps = 0  # для підрахунку кількості злиттів

def merge_sort_iterative(arr):
    global comparisons_iter, assignments_iter, merge_steps
    n = len(arr)
    curr_size = 1

    # тимчасовий масив для злиття
    temp = arr.copy()

    while curr_size < n:
        left_start = 0
        while left_start < n:
            mid = min(left_start + curr_size - 1, n - 1)
            right_end = min(left_start + 2 * curr_size - 1, n - 1)

            # інкремент кроку злиття
            merge_steps += 1

            # злиття підмасивів arr[left_start..mid] та arr[mid+1..right_end] у temp
            i, j, k = left_start, mid + 1, left_start
            while i <= mid and j <= right_end:
                comparisons_iter += 1
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                assignments_iter += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
                assignments_iter += 1

            while j <= right_end:
                temp[k] = arr[j]
                j += 1
                k += 1
                assignments_iter += 1

            left_start += 2 * curr_size

        # копіюємо назад у arr
        arr[:] = temp[:]
        curr_size *= 2

    return arr

arr = [53, 5, 44, 47, 35, 83, 82, 85, 28]
print("Оригінальний список:", arr)
sorted_arr_iter = merge_sort_iterative(arr.copy())
print("Відсортований список:", sorted_arr_iter)
print(f"Кількість порівнянь: {comparisons_iter}")
print(f"Кількість присвоєнь: {assignments_iter}")
print(f"Кількість кроків злиття: {merge_steps}")


