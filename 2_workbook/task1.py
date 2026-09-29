


class Task1:
    def __init__(self, arr):
        if len(arr) >= 2 and arr[1] < arr[0]:
            print(f"элементы отстортированы в обратном порядке - список заменен на обратный")
            arr = arr[::-1]
        self.arr = arr


    def binary_search(self, target) -> int:
        left = 0
        right = len(self.arr) - 1

        while left <= right: # код из примера
            mid = (left + right) // 2

            if self.arr[mid] == target:
                return mid

            if self.arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # вставка элемента если его нет
        self.arr = self.arr[:left] + [target] + self.arr[left:]
        return left

initial_arr = [4]
target = int(input(f"Поиск в {initial_arr}\nчисло для поиска: "))



T1 = Task1(initial_arr)
print(T1.binary_search(target), T1.arr)


'''
Примеры вывода

Поиск в [1, 2, 3, 4, 5]
число для поиска: 2
1 [1, 2, 3, 4, 5]

Поиск в [1, 2, 3, 5, 6, 8]
число для поиска: 4
3 [1, 2, 3, 4, 5, 6, 8]

Поиск в [1, 2, 3, 5, 6, 8]
число для поиска: -65
0 [-65, 1, 2, 3, 5, 6, 8]

Поиск в [1, 2, 3, 4, 5]
число для поиска: 87
5 [1, 2, 3, 4, 5, 87]

Поиск в []
число для поиска: 4
0 [4]

Поиск в [4]
число для поиска: 4
0 [4]
'''
