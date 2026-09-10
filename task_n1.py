

def f(x):
    return 0.25 * (x**3) + x - 2



eps = 0.0001 #такая точность была в примере

left = float(input("левая граница: "))
right = float(input("правая граница: "))

# блок проверок
if f(left) * f(right) > 0:
    print("нельзя использовать метод на этом отрезке:\n- знаки на концах отрезка совпадают")
    exit()

u = lambda a: 0 <= a <= 2
if not all([u(arg) for arg in [left, right]]):
    print("отрезок не соответствует критериям задачи: 0 <= x <= 2")
    exit()

# алгоритм
while abs(right - left) > eps:
    middle = left + (right - left) / 2
    f_middle = f(middle)

    if f_middle == 0:
        break

    if f(left) * f_middle < 0:
        right = middle
    else:
        left = middle

X = left + (right - left) / 2

print(f"* корень уравнения: {X}\n* значение функции: {f(X)}")