
from enum import Enum

class State(Enum):
    LEFT = 0
    RIGHT = 1


class Task3:
    def __init__(self, arr:list[int]):
        self.arr = arr

    def extended_binary_search(self, p1:State) -> int:
        left = 0
        right = len(self.arr) - 1

        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if self.arr[mid] == 0:
                result = mid

                match p1:
                    case State.LEFT:
                      right = mid - 1
                    case State.RIGHT:
                      left = mid + 1


            elif self.arr[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1

        return result if result > 0 else left

    def left_binary_search(self) -> int:
        return self.extended_binary_search(State.LEFT)

    def right_binary_search(self) -> int:
        return self.extended_binary_search(State.RIGHT)

    def find_lines_with_equal_operand(self) -> list:
        return [
            self.arr[:self.left_binary_search()],
            self.arr[self.right_binary_search():]
        ]

    def find_main_operand_count(self) -> int:
        negative, positive = self.find_lines_with_equal_operand()
        positive = positive if positive and positive[0] != 0 else positive[1:]

        return max(map(len, [negative, positive]))

T3 = Task3([-45, -32, 0, 0, 0, 1, 5, 6, 7, 89, 676])
print(T3.find_main_operand_count())



'''
#Примеры вывода:

# штатная работа для [-45, -32, 1, 5, 6, 7, 89, 676]:
6

# один элемент [34]
1

# пустой список []
0

# добавление нулей (т.к они и не положительные и не отрицательные, то никак не влияют на результат)
для списка [ -45, -32, 0, 0, 0, 1, 5, 6, 7, 89, 676]
1
'''