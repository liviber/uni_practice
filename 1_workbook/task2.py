



def f(x):
    return 0.25 * (x**3) + x - 2

def find_xk(a, b):
    return a - (f(a) * (b - a)) / (f(b) - f(a))

eps = 0.0001 #такая точность была в примере
left = float(input("левая граница: "))
right = float(input("правая граница: "))
xk, prev_xk = None, None


# блок проверок
if f(left) * f(right) > 0:
    print("нельзя использовать метод на этом отрезке:\n- знаки на концах отрезка совпадают")
    exit()

u = lambda g: 0 <= g <= 2
if not all([u(arg) for arg in [left, right]]):
    print("отрезок не соответствует критериям задачи: 0 <= x <= 2")
    exit()


# алгоритм
prev_xk = left
xk = find_xk(left, right)

while abs(xk - prev_xk) > eps:
    prev_xk = xk

    if f(xk) == 0:
        break

    if f(left) * f(xk) < 0:
        right = xk
    else:
        left = xk

    xk = find_xk(left, right)


print(f"* корень уравнения: {xk}\n* значение функции: {f(xk)}")




