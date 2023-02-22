l = input('Введите список чисел, разделённых пробелом\n')
list_ = l.split()
arr_ = list(map(int, list_))
print(arr_)


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
arr = merge_sort(arr_)
print(arr)

elem = int(input('Введите искомое число\n'))

i = 0
j = len(arr) - 1
print(i, j)
message = 'Отсутствует элемент, удовлетворяющий условиям поиска'
def binary_search(array, element, i, j):

    if i > j:
        return message

    middle = (i + j) // 2
    if i >= middle >= j:
        return message
    elif array[middle] < element <= array[middle+1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, i, middle - 1)
    else:
        return binary_search(array, element, middle + 1, j)
print(binary_search(arr, elem, i, j))
