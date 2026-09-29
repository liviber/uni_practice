



class Task2:

    def __init__(self, initial_arr):
        self.arr = initial_arr

    def check_condition(self) -> bool:
        changed_direction = False

        previous_element = None
        for element in self.arr:
            if previous_element and previous_element > element:
                changed_direction = True
            if previous_element and changed_direction and previous_element < element:
                return False
            previous_element = element

        return True

initial_arr = []

T2 = Task2(initial_arr)
print(T2.check_condition())



'''
Примеры вывода

Для [1, 2, 3, 4, 3, 2, 1]
True

Для [1, 2, 3, 4]
True

Для [4, 3, 2, 1]
True

Для [1,2,3,4,3,2,5,1]
False

Для [4, 3, 2, 1, 2, 3, 4]
False

Для [1]
True

Для []
True
'''



