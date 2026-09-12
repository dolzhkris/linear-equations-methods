Ag = [[1.6, 1.0, 0.4, 0.3],
     [1.2, 0.2, -0.6, 0.7],
     [2.7, -0.8, 2.2, -2.4],
     [1.7, 0.2, -3.5, -1.2]]

Bg = [1.1, 0.2, 0.3, 0.1]

Az = [[1.8, 1.7, -0.2, 0.2],
      [0.8, 2.2, 0.1, 1.0],
      [-0.3, 0.1, 3.0, 2.0],
      [0.1, 0.3, 1.1, -1.9]]

Bz = [0.1, 2.0, 0.1, 0.1]

def gauss_method(matrix, vector):
    n = len(matrix)
    for i in range(n):
        # Поиск макс. эл. в стобце
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        # Прямой ход
        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            vector[k] += c * vector[i]

    x = [0 for _ in range(n)]
 # Обратный ход
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            vector[k] -= matrix[k][i] * x[i]
    return x

result = gauss_method(Ag, Bg)
print("Решение системы уравнений методом Гаусса:\n", result)

def seidel(Az, Bz, x0, EPS = 1e-6, max_iter = 100):
    n = len(Az)
    x = x0[:]
    for iter_count in range(max_iter):
        x_new = x[:]
        for i in range(n):
            sum_ = sum(Az[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (Bz[i] - sum_) / Az[i][i]
        # Проверяем критерий остановки
        if all(abs(x_new[i] - x[i]) < EPS for i in range(n)):
            return x_new
        x = x_new
    return x

x0 = [0, 0, 0, 0]
solution = seidel(Az, Bz, x0)
print("Решение системы уравнений методом Зейделя:\n", solution)
