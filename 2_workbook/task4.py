from math import ceil


class Task4:
    def __init__(self, initial_arr):
        self.initial_arr = initial_arr
        self.sorted_arr = []
        self.counts = []

    def binary_insert(self, target):
        # код из первой задачи который вставляет элемент на подходящее ему место
        left = 0
        right = len(self.sorted_arr) - 1

        while left <= right: # код из примера
            mid = (left + right) // 2

            if self.sorted_arr[mid] == target:
                return [0, mid]

            if self.sorted_arr[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        # возврат позиции для вставки просто заменен на изменение самого списка
        t = ceil((left + right) / 2)
        self.sorted_arr = self.sorted_arr[:t] + [target] + self.sorted_arr[t:]
        return None # pycharm без этого return помечает предыдущую строку

    def binary_search(self, target) -> int:
        # в пояснении не нуждается
        left = 0
        right = len(self.sorted_arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.sorted_arr[mid] == target:
                return mid
            if self.sorted_arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def count_smaller_elements_at_right(self, target) -> int:
        # для входного элемента target находит кол-во меньших значений справа в списке
        return len(self.sorted_arr[:self.binary_search(target)])

    def find_counts(self) -> list[int]:
        for element in self.initial_arr[::-1]:
            self.binary_insert(element)
            self.counts.append(self.count_smaller_elements_at_right(element))
        return self.counts[::-1]

T4 = Task4([0,0,0,0,0])
print(T4.find_counts())

'''
смысл:
записывается отсортированный список уже пройденных элементов (т.е тех что справа)
это позволяет для каждого нового элемента слева быстро находить кол-во меньших его через бинарный поиск

# Примеры выводай:

# []
[]

# [1]
[0]

# [4,3,2,1]
[3,2,1,0]

# [4,30,20,109,65,23]
[0, 2, 0, 2, 1, 0]

# [0,0,0,0,0]
[0,0,0,0,0]

'''

